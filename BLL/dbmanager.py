#Libraries used for dbmanager.py
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Dbmanager(object):

	#The function gives access to the database from the mainwindow.py
	def database(self):
		connection = sqlite3.connect("Database_Layer/urlData.db")
		return connection

	#The function lets the user enter a phishing website to the database.
	def inputdb(self, insert):
		connection = sqlite3.connect("Database_Layer/urlData.db")
		data = insert
		bad = 0
		if data != "":
			input = connection.cursor()
			input.execute("INSERT INTO URL (URLs, Condition) VALUES (?, ?)",(data, bad))
			print("Suspicious website has been inserted.")
			connection.commit()
			connection.close()
		else:
			print("Invalid output")

	#The function presents the graph comparing the quantity of submitted websites in the database.
	def graphdb(self):
		connection = sqlite3.connect("Database_Layer/urlData.db")
		c = connection.cursor()
		c.execute("SELECT URLs FROM URL WHERE URL.Condition='0'")
		data = c.fetchall()
		phishy = len(data)

		c2 = connection.cursor()
		c2.execute("SELECT URLs FROM URL WHERE URL.Condition='1'")
		data2 = c2.fetchall()
		safe = len(data2)

		status = ['Fraud', 'Safe']
		quantity = [phishy, safe]
		ypos = np.arange(len(status))
		plt.title('Suspicious Websites Analysis')
		plt.xlabel('Status')
		plt.ylabel('Quantity')
		plt.bar(ypos, quantity, color=('Orange', 'Blue'))
		plt.xticks(ypos, status)
		plt.show()

		
