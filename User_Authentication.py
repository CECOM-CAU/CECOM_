from datetime import datetime
import sqlite3



def Authentication(id):
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM User")

    sqlData = curs.fetchall()
    for i in sqlData:
        print(i[0])
        print(type(i[0]))
        print(id)
        print(type(id))
        if str(id) in str(i):
            conn.commit()
            curs.close()
            conn.close()
            conn = sqlite3.connect("fileLogDB.db")
            curs = conn.cursor()
            curs.execute("SELECT * FROM fileLogDB")
            curs.execute("insert into fileLogDB values ('" + id + "', '" + str(datetime.now())[:19] + "', '" +"출석" + "')")
            conn.commit()
            conn.close()
            return id

    conn.commit()
    curs.close()
    conn.close()
    return 'X'





