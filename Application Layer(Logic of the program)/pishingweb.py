import pandas as pd
import numpy as np
import sqlite3
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import dbmanager

class Pishingweb(object):

    def __init__(self):
        super().__init__()
        self.urlData = pd.read_sql_query("SELECT * FROM Url", dbmanager.database(self))

    def makeTokens(self, f):
        tkns_BySlash = str(f.encode('utf-8')).split('/')
        total_Tokens = []
        for i in tkns_BySlash:
            tokens = str(i).split('-')
            tkns_ByDot = []
            for j in range(0,len(tokens)):
                temp_Tokens = str(tokens[j]).split('.')
                tkns_ByDot = tkns_ByDot + temp_Tokens
            total_Tokens = total_Tokens + tokens + tkns_ByDot
        total_Tokens = list(set(total_Tokens))
        if "com" in total_Tokens:
            total_Tokens.remove('com')
        return total_Tokens

    def prediction(self, urlInput):
        y = self.urlData["Condition"] 
        urlList = self.urlData["URLs"] 

        vector = TfidfVectorizer(tokenizer=self.makeTokens)
        x = vector.fit_transform(urlList)
        xLR, xTest, yLR, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
        regression = LogisticRegression()
        regression.fit(xLR, yLR)
        print("Accuracy ", regression.score(xTest, yTest) * 100)

        url = urlInput.strip().split()
        urlTok = vector.transform(url)
        value = regression.predict(urlTok) 
        return value

