import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def storeMYSQL(dictData):
    try:
        connection = mysql.connector.connect(host='localhost', database='nlp', user='root', password='root')
        sql_insert_query = """ INSERT INTO `tweets` (`user_id`, `user_name`, `tweet_id`, `text`) VALUES ("{}","{}","{}","{}")""".format(dictData["user"]["id_str"],dictData["user"]["screen_name"],dictData["id_str"],dictData["text"])
        cursor = connection.cursor()
        cursor.execute(sql_insert_query)
        connection.commit()
        print ("Record inserted successfully into python_users table")

    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
        
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            