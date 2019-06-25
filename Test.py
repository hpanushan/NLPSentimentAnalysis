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
        try:
            # call twitter api to fetch tweets 
            fetched_tweet = self.api.search(q = query, count=count) 
            
            if len(fetched_tweet)==1:
            
                parsed_tweet = {}

                # saving text of tweet 
                parsed_tweet['id'] = fetched_tweet[0].id
                parsed_tweet['text'] = fetched_tweet[0].text 
                parsed_tweet['followers_count'] = fetched_tweet[0].user.followers_count
                
                return parsed_tweet 
            else: pass
            # return parsed tweets
        
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 


def main():
# creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    prevTweet = {}
    while (True):
        tweet = api.getTweetws(query = 'microsoft',count=1) 
        if (prevTweet==tweet): pass
        else:
            prevTweet = tweet
            print(tweet) 

if __name__ == "__main__": 
    # calling main function 
    main()
    
