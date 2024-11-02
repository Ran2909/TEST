import sqlite3 as sql

conn=sql.connect('workers.db')
cur=conn.cursor()

with conn:
    cur.execute('''SELECT worker FROM products WHERE department='sales' ''')
    workers=cur.fetchall()
    name=[]
    for i in workers:
        name.append(i[0])
    print(name)





