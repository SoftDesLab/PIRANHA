import pandas as pd
import numpy as np
import sqlite3
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class Pishingweb:

    def __init__(self):
        super().__init__()
        cnx = sqlite3.connect('urlData.db')
        self.urlData = pd.read_sql_query("SELECT * FROM Url", cnx)


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

    def accuracy(self, urlInput):
        y = self.urlData["Condition"] #kukunin niya yung label na good/bad sa urldata.csv
        urlList = self.urlData["URLs"] #kukuinin niya lahat ng mga website either good or bad

#dito na papasok yung machine learning gagamit ng regression para malaman kung good or bad
        vector = TfidfVectorizer(tokenizer=self.makeTokens)
        x = vector.fit_transform(urlList)
        xLR, xTest, yLR, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
        regression = LogisticRegression()
        regression.fit(xLR, yLR)
        print("Accuracy ", regression.score(xTest, yTest))#print yung accuracy ng makukuha niya 


        #x_pred = ["online.bpi.com.ph/portalserver/onlinebanking/sign-in","google.com","facebook.com/login","sanagustinturismo.co/Facebook/", "facebook.pcriot.com/login.php"]
        url = urlInput.strip().split()
    
        urlTok = vector.transform(url)
        condition = regression.predict(urlTok) #ito na yung mga label kung bad/good. 
        if condition == [1]:
            print('\n',urlInput, " is safe to use.\n")
            return condition
        else:
            print('\n',urlInput, " is not safe to use.\n")
            return condition
        

        #created P.I.R.A.N.H.A.
        """cre:nathan"""