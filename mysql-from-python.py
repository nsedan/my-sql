import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_friends = ['Joey', 'Phoebe', 'Rachel',
                           'Monica', 'Ross', 'Chandler']
        format_strings = ",".join(['%s']*len(list_of_friends))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_friends)
        connection.commit()
finally:
    connection.close()
