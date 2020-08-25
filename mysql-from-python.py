import os
import datetime
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        row = [('Rachel', 29, "1971-03-02 00:00:00"),
               ('Ross', 31, "1968-05-02 00:00:00"),
               ('Phoebe', 32, "1967-05-10 00:00:00"),
               ('Chandler', 31, "1968-06-02 00:00:00"),
               ('Monica', 29, "1971-12-01 00:00:00")]
        cursor.executemany(
            "INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()
finally:
    connection.close()
