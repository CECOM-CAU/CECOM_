import sqlite3

conn = sqlite3.connect("test.db")
curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS User")
curs.execute("CREATE TABLE if not exists Iser(Student_ID, Name);")

def Authentication(id):
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM User")

    sqlData = curs.fetchall()
    for i in sqlData:
        if id in i:
            conn.commit()
            curs.close()
            conn.close()
            return id

    conn.commit()
    curs.close()
    conn.close()
    return 'X'





