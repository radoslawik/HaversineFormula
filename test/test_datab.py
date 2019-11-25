# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""


import sys

#################### MAKE CHANGES HERE #########################
address = "localhost" # address of the database
user = "root" # your username
password = "" # your password
database = "devops" # your database name
table = "TESTING" # table name to store names and numbers (default "TESTING")
sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject') # path to testing file ("datab.py")
########################### END ###############################

#import testing module
import datab


def test_testConnection():  
    assert datab.testConnection(address, user, password, "incorrect_db_name") == False # in case of wrong database name
    assert datab.testConnection(address, user, "incorrect_password", database) == False # in case of incorrect password
    assert datab.testConnection(address, "wrong_user", password, database) == False # in case of wrong login
    assert datab.testConnection("made_up_address", user, password, database) == False # in case of wrong database address
    assert datab.testConnection(address, user, password, database) == True # correct data
    
def test_createTable():  
    assert datab.createTable(address, user, password, database, table) == True # correct data
    assert datab.createTable(address, user, password, database, "") == False # empty table name
    
def test_insertIntoTable():
    assert datab.insertIntoTable(address, user, password, database, table, "Paris", "48.85", "2.35") == True # query executed with success
    assert datab.insertIntoTable(address, user, password, database, table, "Rome", "41.89", "12.51") == True # query executed with success 
    assert datab.insertIntoTable(address, user, password, database, table, "Cracow", "50.04", "19.94") == True # query executed with success 
    assert datab.insertIntoTable(address, user, password, database, table, "Berlin", "integer", "2") == False # second parameter is not decimal
    assert datab.insertIntoTable(address, user, password, database, table, "Rio", "", "30.20") == False # second parameter is not decimal
    assert datab.insertIntoTable(address, user, password, database, table, "Rio", "9999.99", "30.20") == False # second parameter is too big
    
def test_selectFromTable():
    assert datab.selectFromTable(address, user, password, database, "") == None # no table specified
    assert datab.selectFromTable(address, user, password, database, table) != None # correct data
    

