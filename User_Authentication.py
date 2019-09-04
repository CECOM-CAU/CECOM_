import sqlite3 as lite

def Authentication(id):
    conn = lite.connect('test.db')
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





