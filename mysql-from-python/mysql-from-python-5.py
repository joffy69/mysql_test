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
        rows=[("Jane",21,"1990-02-06 23:04:56"),
             ("Jim", 56,"1955-05-09 23:04:56"),
             ("Fred", 100, "1911-09-12 23:03:56"),
             ("Bob", 22, "1989-04-06 12:02:52")]
        cursor.executemany("insert into Friends values(%s,%s,%s);",rows)
        connection.commit()
        
finally:
    #close connection
    connection.close()

    #see file for explanation re cloud 9 being replaced with github
    #
