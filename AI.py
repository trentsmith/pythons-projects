import sqlite3
import datetime
conn=sqlite3.connect('robot.db')
c=conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS hello(input TEXT, output TEXT,emotion TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS smalltalk(input TEXT, output TEXT,emotion TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS conclusion(input TEXT, output TEXT,emotion TEXT)')
create_table()
