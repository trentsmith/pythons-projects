import sqlite3
conn = sqlite3.connect('password.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS PASSWORD(username TEXT, password TEXT, website TEXT)')
def data_entry():
    username = raw_input('what is your username. /n')
    password = raw_input('what is your password. /n')
    website = raw_input('what is the website???/n')
    c.execute('INSERT INTO PASSWORD(username,password,website)VALUES(?,?,?)',(username,password,website))
    conn.commit()
create_table()
p=0
while p!=1:
    print('hello would would you like to do?? 1- selecting a password 2- inserting a password 3-close 4-delete a value')
    action = int(raw_input())
    if action == 1:
        x= raw_input('what is your password?')
        c.execute('Select * FROM PASSWORD WHERE password = ?',(x,))
        print(c.fetchall())
    elif action == 2: 
        data_entry()
    elif action ==3:
        c.close()
        p=1
    elif action == 4:
        x = input('what is the input you want to delete??')
        c.execute('DELETE FROM PASSWORD WHERE PASSWORD = '+x)
