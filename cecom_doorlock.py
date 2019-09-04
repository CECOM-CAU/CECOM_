import sqlite3

conn = sqlite3.connect("test.db")
curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS User")
curs.execute("CREATE TABLE if not exists User(Student_ID, Name);")

def userRegister(name, id):
    conn = sqlite3.connect("test.db")
    curs = conn.cursor()
    curs.execute("select*from User")
    data = curs.fetchall()
    for x in data:
        if(x == id):
            return 'x'

    curs.execute("INSERT INTO user(Student_ID,Name) VALUES("+ id + "," + name + ")")
    print(data)
    conn.commit()
    curs.close()
    conn.close()
    return data


def userDelete(id):
    conn = sqlite3.connect("test.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM User WHERE Student_ID =?",(delete_ID,))
    curs.execute("select*from User")
    data1 = curs.fetchall()
    conn.commit()
    curs.close()
    conn.close()
    print(data1)
