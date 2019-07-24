import sqlite3 as lite

conn = lite.connect('test.db')
curs = conn.cursor()


curs.fetchall()
conn.commit()
curs.close()
conn.close()
