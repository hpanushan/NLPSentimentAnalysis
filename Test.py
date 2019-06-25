import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

import Credentials

class TwitterClient(object):
    # Twitter class for sentiment analysis

    def __init__(self):
        # Class constructor

        # Keys and tokens to access tweeter api
        consumerKey = Credentials.CONSUMER_KEY
        consumerSecret = Credentials.CONSUMER_KEY_SECRET
        accessToken = Credentials.ACCESS_TOKEN
        accessTokenSecret = Credentials.ACCESS_TOKEN_SECRET

        # Attempting authentication
        try:
            # Create OAuthHandler object
            self.auth = OAuthHandler(consumerKey,consumerSecret)
            # Set access token
            self.auth.set_access_token(accessToken,accessTokenSecret)
            # Create tweepy API object to fetch
            self.api = tweepy.API(self.auth)
            print("Authentication is Successful")

        except:
            print("Error : Authentication Failed")

    def getTweetws(self, query, count):
        # Main function to fetch tweets and parse
        
        # Empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count=count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {}
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets 
        
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 

def main():
# creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.getTweetws(query = 'trumph', count=100) 
    return tweets

if __name__ == "__main__": 
    # calling main function 
    print(main()[50])