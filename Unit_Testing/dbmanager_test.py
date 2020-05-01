import unittest
import sqlite3

from dbmanager import dbmanager

class DbManagerTestCase(unittest.TestCase):
    
    def test_connection(self):
        clas = dbmanager()
        clas.inputdb('www.gogle.com')
        self.assertTrue('connection = sqlite3.connect("urlData.db")')
       
if __name__ == '__main__':
     unittest.main()
    



        
