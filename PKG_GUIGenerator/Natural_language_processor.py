# for Tokenizer
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation

# for Stemmer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk


class Tokenizer:

    def __init__(self, query):
        self.__query = query
        self.__token = []
        self.__token_without_stopword = []
        self.__token_without_punctuation = []

    def getTokens(self):
        # map function apply the given  function to given data
        self.__token = list(map(str.lower, word_tokenize(self.__query)))
        return self.__token

    def removeStopword(self):
        token = self.__token
        stop_words = set(stopwords.words('english'))
        self.__token_without_stopword = [word for word in token if word not in stop_words]
        # compare two string use rather nested for loop
        return self.__token_without_stopword

    def removePunctuation(self):
        self.__token_without_punctuation = [word for word in self.__token if word not in set(punctuation)]
        # compare two string use rather nested for loop
        return self.__token_without_punctuation


class Stemminer:

    def __init__(self, query):
        self.__token = query

    def get_stemming(self):
        stem_token = []
        ps = PorterStemmer()

        for word in self.__token:
            stem_token.append(ps.stem(word))

        return stem_token

    def get_lemmatizing(self):
        lem_token = []
        wnl = WordNetLemmatizer()

        for word in self.__token:
            lem_token.append(wnl.lemmatize(word,'n'))

        return lem_token

    def get_pos_tags(self):
        tagged = nltk.pos_tag(self.__token)
        return tagged