from sqlite3 import *

conn = connect('studentdb.db')
cur = conn.cursor()

#sql = "update student set sage=sage+1"
sql = '''
       create table course(
       cno varchar,
       cname varchar,
       credit int)
       '''
cur.execute(sql)
conn.commit()
data = cur.fetchall()
print(data)
sql = '''
      insert into course values 
      ('001','Python程序设计',2)
      '''
cur.execute(sql)
conn.commit()
sql = 'select * from course'
cur.execute(sql)
data = cur.fetchall()
print(data)
cur.close()
conn.close()
