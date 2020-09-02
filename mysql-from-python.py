import os
import pymysql
# get username 
username=os.getenv("root")

#connect to the database
connection = pymysql.connect(host='localhost',
user=username,
password='',
db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        sql="select * from Artist;"
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
finally:
    #close connection
    connection.close()

    #see file for explanation re cloud 9 being replaced with github
    #
