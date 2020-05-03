#Libraries used for data_extraction.py
import pandas as pd
import numpy as np
import sqlite3
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from dbmanager import Dbmanager

class Data_extraction(object):
    
    #The function allows the class to initialize the attributes of the class.
    def __init__(self):
        super().__init__()
        self.urlData = pd.read_sql_query("SELECT * FROM Url", Dbmanager.database(self))
    #The function converts the URL to streams of tokens; each token is a separated by word and punctuations

    #The function will test the dataset then predicts the URL if it is SAFE or NOT.
    def prediction(self, urlInput):
        y = self.urlData["Condition"] 
        urlList = self.urlData["URLs"] 

        vector = TfidfVectorizer()
        x = vector.fit_transform(urlList)
        xLR, xTest, yLR, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
        regression = LogisticRegression()
        regression.fit(xLR, yLR)
        print("Accuracy: ", regression.score(xTest, yTest) * 100)
        url = urlInput.strip().split()
        urlTok = vector.transform(url)
        value = regression.predict(urlTok) 
        return value

