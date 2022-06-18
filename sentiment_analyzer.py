
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
import hazm
# from cleantext import clean
# import plotly.express as px
import plotly.graph_objects as go
from tqdm.notebook import tqdm
import os
import re
import json
import copy
import collections



"""## PyTorch"""

from transformers import BertConfig, BertTokenizer
from transformers import BertModel

from transformers import AdamW
from transformers import get_linear_schedule_with_warmup

import torch
import torch.nn as nn
import torch.nn.functional as F

"""### Configuration"""

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f'device: {device}')

train_on_gpu = torch.cuda.is_available()

if not train_on_gpu:
    print('CUDA is not available.  Training on CPU ...')
else:
    print('CUDA is available!  Training on GPU ...')

# general config
MAX_LEN = 128
BATCH_SIZE = 16
CLIP = 0.0
# MODEL_NAME_OR_PATH = 'HooshvareLab/bert-fa-base-uncased'
MODEL_PATH = '/content/drive/MyDrive/sntiment_telegram/model'
# create a key finder based on label 2 id and id to label
labels = ["nerual","positive","negative"]
label2id = {label: i for i, label in enumerate(labels)}
id2label = {v: k for k, v in label2id.items()}
config = BertConfig.from_pretrained(
    MODEL_NAME_OR_PATH, **{
        'label2id': label2id,
        'id2label': id2label,
    })

class SentimentModel(nn.Module):
    def __init__(self, config):
        super(SentimentModel, self).__init__()
        self.bert = BertModel.from_pretrained(MODEL_NAME_OR_PATH)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
    
    def forward(self, input_ids, attention_mask, token_type_ids):
        pooled_output = self.bert(
            input_ids=input_ids, 
            attention_mask=attention_mask, 
            token_type_ids=token_type_ids).pooler_output
        # print(pooled_output)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits

import torch, gc

gc.collect()
torch.cuda.empty_cache()
pt_model = None

class TaaghcheDataset(torch.utils.data.Dataset):
    """ Create a PyTorch dataset for Taaghche. """

    def __init__(self, tokenizer, comments, max_len=128):
        self.comments = comments
        self.tokenizer = tokenizer
        self.max_len = max_len
    
    def __len__(self):
        return len(self.comments)

    def __getitem__(self, item):
        comment = str(self.comments[item])

        encoding = self.tokenizer.encode_plus(
            comment,
            add_special_tokens=True,
            truncation=True,
            max_length=self.max_len,
            return_token_type_ids=True,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt')
        
        inputs = {
            'comment': comment,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'token_type_ids': encoding['token_type_ids'].flatten(),
        }

        return inputs


def create_data_loader(x, tokenizer, max_len, batch_size):
    dataset = TaaghcheDataset(
        comments=x,
        tokenizer=tokenizer,
        max_len=max_len, 
      )
    
    return torch.utils.data.DataLoader(dataset, batch_size=batch_size)

def predict_op(model, 
             data_loader
          ):
    
    model.eval()
    model.to(device)
    losses = []
    y_pred = []
    y_true = []

    for dl in tqdm(data_loader, total=len(data_loader), desc="Training... "):
        step += 1
        # print(step)
        input_ids = dl['input_ids']
        attention_mask = dl['attention_mask']
        token_type_ids = dl['token_type_ids']
        # move tensors to GPU if CUDA is available
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        token_type_ids = token_type_ids.to(device)
        # print("here")
        # compute predicted outputs by passing inputs to the model
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids)
        # print("here")
        # convert output probabilities to predicted class
        _, preds = torch.max(outputs, dim=1)
        y_pred.extend(preds.cpu().data)
        # print(preds)
    return y_pred

def sentiment_analyzer(data):
        tokenizer = BertTokenizer.from_pretrained(MODEL_NAME_OR_PATH)
        model = SentimentModel(config = config)
        model.load_state_dict(torch.load("/content/drive/MyDrive/sntiment_telegram/model/pytorch_model.bin"))
        data_loader = create_data_loader(data, tokenizer, MAX_LEN, BATCH_SIZE)
        p = predict_op(model, data_loader)
        return p 