import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import mysql.connector
from mysql.connector import Error

from TweepyStreamer import StdOutListener
from Model import Model

def main():
    # Processing stored data and storing them in the MySQL table 
    obj = Model() 
    conn = mysql.connector.connect(host='localhost', database='nlp', user='root', password='root')
    sql_Query = "select * from tweets"
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql_Query)
    
    for i in range(1,1501):
        row = obj.getTweets(conn,cursor)
        obj.storeSentimentMYSQL(conn,row)
        print(i, "Record is entered successfully")
    
    # closing the connection
    cursor.close()
    conn.close()
    #### """
 
    # Streaming tweets and storing them into MySQL table
    #obj = StdOutListener()
    #obj.streamer()
    ####

if __name__ == "__main__": 
    # calling main function 
    main() 