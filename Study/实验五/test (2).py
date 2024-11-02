from sqlite3 import *

conn = connect('schooldb.db')
cur = conn.cursor()
sql = '''

    '''
cur.execute(sql)
conn.commit()
sql = 'select * from bumenTable'
cur.execute(sql)
data = cur.fetchall()
print(data)
cur.close()
conn.close()
