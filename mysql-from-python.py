import os
import datetime
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(
            "UPDATE Friends SET age = 30 WHERE name = 'Monica';")
        connection.commit()
finally:
    connection.close()
