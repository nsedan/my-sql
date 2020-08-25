import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [(51, 'Joey'),
                (52, 'Ross'),
                (50, 'Rachel'),
                (50, 'Monica'),
                (53, 'Phoebe'),
                (52, 'Chandler')]
        cursor.executemany(
            "UPDATE Friends SET age = %s WHERE name = %s;", rows)
        connection.commit()
finally:
    connection.close()
