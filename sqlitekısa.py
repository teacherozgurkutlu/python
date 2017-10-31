# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:27:09 2017

@author: k
"""

import sqlite3
db = sqlite3.connect('ilkdata.db')
cursor = db.cursor()

cursor.execute('''SELECT * FROM t''')

for row in cursor.fetchall():
   
    print('{0} : {1}, {2}'.format(row[0], row[1], row[1]))