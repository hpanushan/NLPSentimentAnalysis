import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def storeSentimentMYSQL(conn,row):
    try:
        obj = Model()
        #column values of new table
        user_id = row[3]
        user_name = row[4]
        tweet_id = row[1]
        text = row[2]
        sentiment = obj.getTweetSentiment(row[2])

        sql_insert_query = """ INSERT INTO `sentiment` (`user_id`, `user_name`, `tweet_id`, `text`, `sentiment`) VALUES ("{}","{}","{}","{}","{}")""".format(user_id,user_name,tweet_id,text,sentiment)
        cursor = conn.cursor()
        cursor.execute(sql_insert_query)
        conn.commit()
        print ("Record inserted successfully into python_users table")
    except mysql.connector.Error as error :
        conn.rollback() #rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        #closing database connection.
        if(conn.is_connected()):
            cursor.close()
            conn.close()