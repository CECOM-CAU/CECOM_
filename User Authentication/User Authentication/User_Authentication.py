import sqlite3 as lite

conn = lite.connect('test.db')
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS User")
curs.execute("CREATE TABLE User('UserName', 'Student_ID')")
curs.execute("INSERT INTO User VALUES('허준구', '20164352')")

curs.execute("SELECT * FROM User")

sqlData = curs.fetchall()
print(sqlData)


testData = '20164352'

def Authentication(sqlData, testData):
    for i in sqlData:
        if testData in i:
            return testData
        else:
            return False



print(Authentication(sqlData,testData))


conn.commit()
curs.close()
conn.close()

