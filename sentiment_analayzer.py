import pandas as pd
from hazm import Normalizer, Stemmer, WordTokenizer
from word_embedding import *
from tqdm import tqdm

class Sentiment_model:
    def __init__(self,txt_data, labels):
            self.texts = txt_data
            self.labels = labels
            self.word2id = {}
            self.id2word = {}
            self.vocab = []
            self.min_len = 3
            self.max_len = 30


    def process_text(self):
        self.texts_id = []
        self.labels_process = []
        # print(len(self.texts))
        for i, text in enumerate(self.texts):
            print(i)
            new_text = Normalizer().normalize(str(text))
            words = WordTokenizer().tokenize(new_text)
            for word in words:
                s_words = Stemmer().stem(word)
                # print(s_words)
                if s_words not in self.vocab:
                    self.vocab.append(s_words)
            self.texts[i]= new_text
        self.vocab = sorted(self.vocab)
        print(self.vocab)
        self.word2id = {w: i+1 for i, w in enumerate(self.vocab)}
        self.word2id["UNK"]  = len(self.vocab)
        self.id2word = {i+1: w for i, w in enumerate(self.vocab) }
        self.id2word[len(self.vocab)] = 'UNK'
        l = 0
        for text,label in zip(self.texts,self.labels):
            words = WordTokenizer().tokenize(str(text))
            words_digit = []
            for word in words:
                s_words = Stemmer().stem(word)
                id = self.word2id[s_words]
                words_digit.append(id)

            l = len(words_digit)
            if l < self.min_len:
                continue
            elif l < self.max_len :
                while len(words_digit)< self.max_len:
                    words_digit.append(0)
                self.labels_process.append(label)
            else:
                words_digit = words_digit[:self.max_len]
                self.labels_process.append(label)
            print(len(words_digit))
            self.texts_id.append(words_digit)
        print(l / len(self.texts))

def text_2_token(texts):
    tokens_texts = []
    for i, text in tqdm(enumerate(texts)):

        new_text = Normalizer().normalize(str(text))
        words = WordTokenizer().tokenize(new_text)
        list_s_words = []
        for word in words:
            s_words = Stemmer().stem(word)
            list_s_words.append(s_words)
        tokens_texts.append(list_s_words)
    return tokens_texts



from sklearn.model_selection import  train_test_split
from sklearn.tree import  DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
if __name__ == '__main__':
    text_datas = pd.read_excel("labeled_data2.xlsx",index_col=None)
    # print(text_datas.columns)
    texts = text_datas.iloc[:, 1].to_numpy()
    # print(texts)
    labels =  text_datas.iloc[:, 2].to_numpy()
    # print(labels)
    sm = Sentiment_model(texts, labels)
    ####################################### word2vec
    t_texts = text_2_token(texts)
    dictionary = Dictionary(t_texts)
    BoW_corpus = [dictionary.doc2bow(text) for text in t_texts]
    hamshari_word_vec = hamshari_doc_vec_process("G:\master_matus\99_2\\NLP\HWS\hamshahri.fa.text.300.vec")
    X, Y = representation_of_doc_2(300, texts, dictionary, BoW_corpus, hamshari_word_vec,sm.labels)

    #######################################
    # sm.process_text()
    # X = sm.texts_id
    # Y = sm.labels_process
    # print(X)
    x_train, x_test, y_train, y_test = train_test_split(X, Y)
    dt = DecisionTreeClassifier()
    dt.fit(x_train, y_train)
    y_predict = dt.predict(x_test)
    print(classification_report(y_test,y_predict))
    dt = SVC()
    dt.fit(x_train, y_train)
    y_predict = dt.predict(x_test)
    print(classification_report(y_test,y_predict))











