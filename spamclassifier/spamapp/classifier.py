import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
import re

class SpamClassifer():

    special_char = ['\\' + x.strip() for x in open('spamapp/model/special-chars.txt').readlines()] + ["[0-9]", "-"]
    stop_words = set(stopwords.words('english'))
    loaded_vectorizer = pickle.load(open('spamapp/model/spam_vectorizer.sav', 'rb'))
    loaded_clf = pickle.load(open('spamapp/model/spam_classifier.sav', 'rb'))
    # def load_classifier():
    #     with open('./model/special-chars.txt') as f:
    #         special_char = ['\\' + x.strip() for x in f.readlines()]
    #     special_char =  special_char+ ["[0-9]", "-"] # -  is for this corrupt data only

    #     stop_words = set(stopwords.words('english'))

    #     loaded_vectorizer = pickle.load(open('./model/spam_vectorizer.sav', 'rb'))
    #     loaded_clf = pickle.load(open('./model/spam_classifier.sav', 'rb'))
    @staticmethod
    def remove_special_char(element):
        if re.search('|'.join(SpamClassifer.special_char), element):
            return False
        else:
            return True

    @staticmethod
    def tokenize(raw):
        tokens = word_tokenize(raw) 
        tokens = list(filter(SpamClassifer.remove_special_char, tokens))
        return tokens

    @staticmethod
    def remove_stop_words(word_tokens):
        return [w for w in word_tokens if not w in SpamClassifer.stop_words] 

    @staticmethod
    def classify(mail):
        token = SpamClassifer.tokenize(mail)
        token_no_stop_words = SpamClassifer.remove_stop_words(token)
        sentence_no_stop_words = ' '.join(token_no_stop_words)
        data = SpamClassifer.loaded_vectorizer.transform([sentence_no_stop_words])
        result = SpamClassifer.loaded_clf.predict(data)[0]   
        return result