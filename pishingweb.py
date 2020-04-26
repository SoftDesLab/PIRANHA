import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class Pishingweb:

    def __init__(self):
        self.urlData = pd.read_csv("urldata.csv")


#hihimayin lang nento yung mga strings 
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
    def vectoran(self):
        vector = TfidfVectorizer(tokenizer=self.makeTokens)
        return vector

    def accuracy(self):
        y = self.urlData["label"] #Get Status[Good/Bad] in urldata.csv
        urlList = self.urlData["url"] #Get websites[Good/Bad]
        #dito na papasok yung machine learning gagamit ng regression para malaman kung good or bad
        
        x = self.vectoran().transform(urlList)
        xLR, xTest, yLR, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
        regression = LogisticRegression()
        regression.fit(xLR, yLR)
        regScore = regression.score(xTest, yTest)
        print("Accuracy ", regScore)#print yung accuracy ng makukuha niya 
        return regression

'''   
    def prediction(self, vector):
        x_pred = Ui_MainWindow.scanning().strip().split()    
        x_pred1 = vector.transform(x_pred)
        news = accuracy().predict(x_pred1) #ito na yung mga label kung bad/good.
        print(news)#print kung bad or good in order
        return news 
'''
