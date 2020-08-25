import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor() as cursor:
        row = cursor.execute(
            "DELETE FROM Friends WHERE name = %s;", 'Gunther')
        connection.commit()
finally:
    connection.close()
