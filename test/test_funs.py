# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""
import sys
sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject')
import funs

address = "localhost"
user = "root"
password = ""
database = "devops"
table = "TESTING"

def test_testConnection():  
    assert funs.testConnection(address, user, password, "incorrect_db_name") == False
    assert funs.testConnection(address, user, "incorrect_password", database) == False
    assert funs.testConnection(address, "wrong_user", password, database) == False
    assert funs.testConnection("made_up_address", user, password, database) == False
    assert funs.testConnection(address, user, password, database) == True
    


