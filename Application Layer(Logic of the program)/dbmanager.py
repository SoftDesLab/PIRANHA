import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.model_selection import train_test_split
import seaborn as sns

class dbmanager(object):
	def database(self):
		connection = sqlite3.connect("urlData.db")
		return connection

	def inputdb(self, insert):
		connection = sqlite3.connect("urlData.db")
		data = insert
		bad = 0
		input = connection.cursor()
		input.execute("INSERT INTO URL (URLs, Condition) VALUES (?, ?)",(data, bad))
		connection.commit()
		connection.close()

	def graphdb(self):
		query = "SELECT COUNT(Condition), Condition from URL group by Condition"
		TM = pd.read_sql(query,database(self))
		