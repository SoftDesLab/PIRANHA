import unittest
import sqlite3

from dbmanager import Dbmanager

class DbManagerTestCase(unittest.TestCase):
    
    def test_database(self):
        clas = dbmanager()
        clas.database()
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
        
    def test_connection(self):
        clas = dbmanager()
        clas.inputdb('www.gogle.com')
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
    
    def test_connection(self):
        clas = dbmanager()
        clas.graphdb()
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
        
if __name__ == '__main__':
     unittest.main()
    



        
