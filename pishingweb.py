import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class Pishingweb:

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
