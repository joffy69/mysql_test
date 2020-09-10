import os
import datetime
import pymysql

# get username 
username=os.getenv("root") 
#this can be anything in original it was "C9_USER"

#connect to the database
connection = pymysql.connect(host='localhost',
user=username,
password='',
db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        
        cursor.execute("update Friends set age=%s where name=%s;",(23, 'Bob'))
        connection.commit()
        
finally:
    #close connection
    connection.close()

    #see file for explanation re cloud 9 being replaced with github
    #
