import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import mysql.connector
from mysql.connector import Error

class Model(object):
    # Twitter class for sentiment analysis

    def __init__(self):
        pass

    def getTweets(self, conn, cursor):
        # Main function to fetch tweets into MySQL database
        try:
            record = cursor.fetchone()
            return record
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 

    def cleanTweet(self,tweet):
        # Removing links and mentions in tweet text 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

    def getTweetSentiment(self,tweet):
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.cleanTweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def storeSentimentMYSQL(self,conn,row):
        try:
            #column values of new table
            user_id = row[1]
            user_name = row[2]
            tweet_id = row[3]
            text = row[4]
            sentiment = self.getTweetSentiment(text)

            sql_insert_query = """ INSERT INTO `sentiment` (`user_id`, `user_name`, `tweet_id`, `text`, `sentiment`) VALUES ("{}","{}","{}","{}","{}")""".format(user_id,user_name,tweet_id,text,sentiment)
            cursor = conn.cursor()
            cursor.execute(sql_insert_query)
            conn.commit()
        except mysql.connector.Error as error :
            conn.rollback() #rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))
        finally:
            #closing database connection.
            if(conn.is_connected()):
                pass