import sqlite3 as lite

conn = lite.connect('test.db')
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS User")
curs.execute("CREATE TABLE User('UserName', 'Student_ID')")
curs.execute("INSERT INTO User VALUES('허준구', '20164352')")

curs.execute("SELECT * FROM User")

sqlData = curs.fetchall()
print(sqlData)





conn.commit()
curs.close()
conn.close()

