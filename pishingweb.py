import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

urlData = pd.read_csv("urldata.csv")
print(urlData.head())#print lang yung head ng csv data

#hihimayin lang nento yung mga strings 
def makeTokens(f):
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

#kukunin dito yung mga website pati yung label nila.
y = urlData["label"] #kukunin niya yung label na good/bad sa urldata.csv
urlList = urlData["url"] #kukuinin niya lahat ng mga website either good or bad

#dito na papasok yung machine learning gagamit ng regression para malaman kung good or bad
vector = TfidfVectorizer(tokenizer=makeTokens)
x = vector.fit_transform(urlList)
xLR, xTest, yLR, yTest = train_test_split(x, y, test_size=0.2, random_state=42)
regression = LogisticRegression()
regression.fit(xLR, yLR)
print("Accuracy ", regression.score(xTest, yTest))#print yung accuracy ng makukuha niya 
x_pred = ["online.bpi.com.ph/portalserver/onlinebanking/sign-in","google.com","facebook.com/login","sanagustinturismo.co/Facebook/", "facebook.pcriot.com/login.php"]
x_pred1 = vector.transform(x_pred)
news = regression.predict(x_pred1) #ito na yung mga label kung bad/good. 

print(news)#print kung bad or good in order
 
