import mysql.connector
from mysql.connector import Error
try:
    conn = mysql.connector.connect(host='localhost', database='nlp', user='root', password='root')
   
    sql_Query = "select * from tweets"
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql_Query)

    # Reading first row of the table
    record1 = cursor.fetchone()
    print (record1[2])
    # Reading second row of the table
    record2 = cursor.fetchone()
    print (record2[2])

    cursor.close()
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(conn.is_connected()):
        conn.close()
        print("connection is closed")