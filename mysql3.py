# import pymysql.cursors
import pymysql

connection = pymysql.connect(host='localhost',
                        user='root',
                        password='admin',
                        database='demo1')
                        # cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT * FROM student"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

