import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.model_selection import train_test_split
import seaborn as sns

def __init__(self):
	pass
	
def database(self):
	connection = sqlite3.connect("urlData.db")
	return connection

def inputdb(insert):
	data = insert
	input = database().cursor()
	input.execute("INSERT INTO URL VALUES(?,?)",(data, 0))

def graphdb(self):
	pass

# insert = input("Insert URLs:")
# inputdb(insert)
# test_percentage = .2
# conn = sqlite3.connect('urlData.db')
# query = "SELECT Condition FROM URL"
# TM = pd.read_sql(query, conn)
# sns.countplot(x="Condition", y="URLs", data=TM)
# TM1 = TM.head(100)
# # plt.scatter(TM1['URLs'], TM1['Condition'])
# plt.xlabel("QUANTITY", fontsize=16)
# plt.ylabel("STATUS", fontsize = 16)
# plt.title("Phishing Website Detection", fontsize =25)
# plt.show()

# dataset = database()
# test_df = train_test_split(dataset, test_size=test_percentage, random_state=42)
# count_train_class = pd.valuecounts(train_df['Class'])
# count_train_class.plot(kind='bar, fontsize=16')
# plt.title("Website Extraction", fontsize=16)
# plt.xticks(rotation='horizontal')
# plt.xlabel("Class", fontsize=20)
# plt.ylabel("Class Count", fontsize=20)
# plt.show()

# connection = sqlite3.connect("urlData.db")
# # query = "SELECT URLs FROM URL WHERE URL.Condition='0'"
# # result = connection.execute(query)
# c = connection.cursor()

# def graph_data():
# 	c.execute('SELECT Condition FROM URL')

# # "SELECT URLs FROM URL WHERE URL.Condition='0'

# insert = (input("ENTER URL:"))
# input = database().cursor()
# input.execute("INSERT INTO URL VALUES(" + insert + ", 0)")

