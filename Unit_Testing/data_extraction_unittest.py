import unittest
import pandas as pd
import numpy as np
import sqlite3
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sys
#Insert path of Application_Layer to run python scripts
sys.path.insert(0, "/home/paradox/Local_Repo/Project/PIRANHA/Application_Layer")
from data_extraction import Data_extraction
from dbmanager import Dbmanager

class DataExtractionTestCase(unittest.TestCase):

    def test_init(self):
        clas = Data_extraction()
        clas.__init__()
        self.assertTrue('self.urlData = pd.read_sql_query("SELECT * FROM Url", Dbmanager.database(self))')
    
if __name__ == '__main__':
     unittest.main()