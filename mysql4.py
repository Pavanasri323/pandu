import pymysql

db = pymysql.connect(host='localhost',
                        user='root',
                        password='admin',
                        database='demo1',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
#query = 'INSERT INTO student VALUES("John","Dell",24,"08")'
#query = 'DELETE from student where age>25'
# query = 'UPDATE STUDENT SET fname = "Ben" where regnum = "08"'
query = 'CREATE TABLE pavanasri(fname varchar(50), lname varchar(50), empnum int)'
try:
    cursor.execute(query)
    db.commit()
except:
    db.rollback()
db.close()
