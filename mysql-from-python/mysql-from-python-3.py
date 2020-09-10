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
        sql="select * from Genre;"
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int,DOB datetime);""")
                        #note that the above will still display a warning (not error) if the
                        #table already exists
        for row in cursor:
            print(row)
finally:
    #close connection
    connection.close()

    #see file for explanation re cloud 9 being replaced with github
    #
