import sqlite3
from datetime import datetime

import pyodbc
from pandas import read_sql


class Connector:
    def __init__(self):
        # conn = sqlite3.connect(database_url)
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=EPRUPETW06EE;'
                              'Database=TRN;'
                              'Trusted_Connection=yes;')
        self.cursor = conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]


