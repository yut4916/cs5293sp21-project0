import pytest

import os.path
from os import path

import sqlite3

def test_test():
    # I am testing my knowledge of how to write a test :)
    result = "echo"
    assert result == "echo"

# fetchData()
def test_f1():
    assert path.exists("/tmp/data.pdf")

# readData()
def test_f2():
    # Check if the output is actually clean data, like we expect?
    assert True

# createDB()
def test_f3():
    # Is there a file called "normanpd.db"?
    dbExists = path.exists("normanpd.db")
    assert dbExists

    if dbExists:
        # Is there a table in our database called "incidents"?
        con = sqlite3.connect("normanpd.db")
        cur = con.cursor()
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='incidents'")
        tableExists = cur.fetchone()[0]
        con.close()
        assert tableExists == 1

# populateDB()
def test_f4():
    con = sqlite3.connect("normanpd.db")
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM incidents")
    numRecords = cur.fetchone()[0]
    con.close()
    assert numRecords > 0

# countNature()
def test_f5():
    # Compare sum of natures to sum of rows?
    assert True

