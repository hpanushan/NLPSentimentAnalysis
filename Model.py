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

    def getTweets(self, cursor):
        # Main function to fetch tweets into MySQL database
        tweets = {}
        try:
            for i in range(1,10): 
                record = cursor.fetchone()[2]
                tweets[record] = self.getTweetSentiment(record)
            cursor.close()
            return tweets
        
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 

def main():
# creating object of TwitterClient Class 
    api = Model() 
    conn = mysql.connector.connect(host='localhost', database='nlp', user='root', password='root')
    sql_Query = "select * from tweets"
    cursor = conn.cursor(buffered=True)
    cursor.execute(sql_Query)
    print(api.getTweets(cursor))

if __name__ == "__main__": 
    # calling main function 
    main() 