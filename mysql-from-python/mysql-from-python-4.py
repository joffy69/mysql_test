import os
import pymysql
# get username 
username=os.getenv("root") #this can be anything in original it was "C9_USER"

#connect to the database
connection = pymysql.connect(host='localhost',
user=username,
password='',
db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        row=("Bob",21,"1990-02-06 23:04:56")
        cursor.execute("insert into Friends values(%s,%s,%s);",row)
        connection.commit()
        
finally:
    #close connection
    connection.close()

    #see file for explanation re cloud 9 being replaced with github
    #
