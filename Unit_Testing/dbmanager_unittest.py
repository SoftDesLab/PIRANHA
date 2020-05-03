import unittest
import sqlite3
import sys
#Insert path of Application_Layer to run python scripts
sys.path.insert(0, "/home/dominic/PIRANHA/Application_Layer")
from dbmanager import Dbmanager

class DbManagerTestCase(unittest.TestCase):
    
    def test_database(self):
        clas = Dbmanager()
        clas.database()
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
        
    def test_connection(self):
        clas = Dbmanager()
        clas.inputdb('www.google.com')
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
    
    def test_connection(self):
        clas = Dbmanager()
        clas.graphdb()
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
        
if __name__ == '__main__':
     unittest.main()
    



        
