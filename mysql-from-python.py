import os
import datetime
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS
            Friends(name char(20), age int, DOB datetime);""")
        for row in cursor:
            print(row)
finally:
    connection.close()
