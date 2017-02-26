import sqlite3
import datetime
conn=sqlite3.connect('robot.db')
c = conn.cursor()
#create table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS hello1(output TEXT,input2 TEXT)')
def data():
    x=raw_input('HELLO MY NAME IS NOISEBOT I LIKE TO MAKE NOISE HOW DO YOU FEEL??')
#print the first output than inputs the input2 and tests for error
    try:
        c.execute('SELECT output FROM hello1 where input2='+x)
        print(c.fetchall())
        x=raw_input()
    except:
         print('what do you want me to say??')
         y = raw_input()
         print('what is your response')
         x=raw_input()
         c.execute('INSERT INTO hello1(output,input2)VALUES(?,?)',(y,x))
         ##delete the one where input2=2
         conn.commit()
    mainloop(x,y)
def mainloop(x,y):
    p=0
    #add a closing statement
    while(p!=1):
        print(c.fetchall())
        try:
            c.execute('SELECT output FROM hello1 where input2 = '+x)
            x=raw_input()
        except:
            print("what should I say???")
            y = raw_input()
            print('what is your response')
            x=raw_input()
            c.execute('INSERT INTO hello1(output,input2)VALUES(?,?)',(x,y))
create_table()
data()
