import sqlite3
import datetime
conn = sqlite3.connect('password.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Questions(ID INT, question TEXT, company TEXT,category TEXT,last_entry TEXT,count INTEGER)')
create_table()
def data_entry():
    c.execute('SELECT * FROM Questions')
    print('what questions did you have??')
    Question = raw_input()
    print('id?')
    ID=int(raw_input())
    print('company')
    company=raw_input()
    print('category??')
    category = raw_input()
    p
    c.execute('INSERT INTO Questions(ID,question,company,category,last_entry)VALUES(?,?,?,?,?)',(ID,Question,company,category,0))
    conn.commit()
c.execute('SELECT * FROM Questions')
x = int(raw_input('what do you want to do? 1- add a question'))
if(x==1):
    data_entry()
