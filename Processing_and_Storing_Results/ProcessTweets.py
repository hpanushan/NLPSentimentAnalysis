import re
from nltk.tokenize import word_tokenize
from string import punctuation 
from nltk.corpus import stopwords 

# Class to clean the tweet text
class PreProcessTweets:
    # Creating stopwords set
    def __init__(self):
        self.stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER','URL'])
    
    # Cleaning one tweet text
    def cleanTweet(self, tweet):
        tweet = tweet.lower()                                               # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)   # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)                         # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)                          # remove the # in #hashtag
        tweet = word_tokenize(tweet)                                        # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self.stopwords]

    # Read tweets and process tweets by above method
    def processTweets(self, list_of_tweets):
        processedTweets=[]
        for tweet in list_of_tweets:
            processedTweets.append(self.cleanTweet(tweet["text"]))
        return processedTweets



