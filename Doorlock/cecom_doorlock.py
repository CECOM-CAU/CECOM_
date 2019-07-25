import sqlite3
conn = sqlite3.connect("test.db")

curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS user")
curs.execute("CREATE TABLE user(Name, Student_ID);")

sql = "INSERT INTO user(Name, Student_ID) VALUES(?,?)"
data = (
    ('정','20191234'),
    ('민','20191235'),
    ('수','20191236'),
)
curs.executemany(sql, data)

name, studentid = input("insert Name, Student_ID:").split(",")
curs.execute(sql,(name,studentid))

curs.execute("select*from user")
data = curs.fetchall()
print(data)

student_ID = input("student ID:")

def check(data1, studentID):
    for x in data1:
        if studentID == x[1]:
            return studentID
    return False

print(check(data, student_ID))


delete_ID = input("delete ID:")

curs.execute("DELETE FROM user WHERE Student_ID =?",(delete_ID,))


curs.execute("select*from user")
data1 = curs.fetchall()
print(data1)

conn.close()