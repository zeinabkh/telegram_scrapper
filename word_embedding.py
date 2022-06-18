from gensim.models import Word2Vec, TfidfModel
from gensim.corpora import  Dictionary
import numpy as np
from tqdm import tqdm
# load_data, read docs file and every file consider as a item by content and label
# input: path if data file
# output: return the list that contain docs and their labels.
# get word embedding by skip gram.
# use gensim.word2vec


def skip_gram(news_list):
    docs_list = list(map(lambda x: x['content'], news_list))
    skip_gram = Word2Vec(docs_list,min_count=1,vector_size=300, workers=3, window =5, sg = 1)
    return skip_gram

# represent  documents as vectors that are construct from the average of word vectors in each document.
def representation_of_doc_1(c,news_list,word_vec):
    docs_vector = []
    for doc in news_list:
        vector = np.zeros(c)
        for word in doc["content"]:
            try:
                vector += word_vec[word]
            except KeyError:
                continue
        vector /= len(doc["content"])
        docs_vector.append(vector)
    return docs_vector


# represent  documents as vectors that are construct from the average of word vectors in each document use TF.
def representation_of_doc_2(c,docs,dictionary,BoW_corpus, word_vec, labels):
    tfidf = TfidfModel(BoW_corpus)
    docs_vector = []
    labels_list = []
    for doc, l in zip(BoW_corpus,labels):
        tf_idf_vec = tfidf[doc]
        # print(tf_idf_vec)
        vector = np.zeros(c)
        count = 0
        for word_tfidf in tf_idf_vec:
            try:

                vector += word_tfidf[1] * np.array(word_vec[dictionary[word_tfidf[0]]])
                count += word_tfidf[1]
            except KeyError:
                continue
            except ValueError:
                # print(word_tfidf[1], np.array(word_vec[dictionary[word_tfidf[0]]]), dictionary[word_tfidf[0]])
                continue
            except TypeError:
                print(type(word_vec[dictionary[word_tfidf[0]]]), word_vec[dictionary[word_tfidf[0]]])
        if count != 0:
            labels_list.append(l)
            docs_vector.append(vector/count)
    return docs_vector, labels_list


def hamshari_doc_vec_process(path):
    word_vec = {}
    file_reader = open(path,encoding="utf-8")
    data_stream = file_reader.read().split("\n")
    for w in data_stream[1:]:
      word = w.split(" ")
      if len(word) > 0:
        word_vec[word[0]] = [float(v) for v in word[1:] if len(v) > 0]
    return word_vec






