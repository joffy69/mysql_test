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
        list_of_names=['Jane','Fred']
        #prepare a string with the same number of placeholders as in list-of-names
        format_strings=','.join(['%s']*len(list_of_names))
        cursor.execute("delete from Friends where name in ({});".format(format_strings),list_of_names)
        connection.commit()
        
finally:
    #close connection
    connection.close()

    #see file for explanation re cloud 9 being replaced with github
    #
