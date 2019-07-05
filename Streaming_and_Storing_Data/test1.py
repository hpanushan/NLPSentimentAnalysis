import csv
import time
import tweepy
from twython import Twython
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

import Credentials

# Reading tweet text from twitter id
def readTweetText(twitterObj,tweet_id):
    tweet = twitterObj.show_status(id=tweet_id)
    return tweet['text']

# Reading tweet object from twitter id
def readTweet(twitterObj,tweet_id):
    tweet = twitterObj.show_status(id=tweet_id)
    return tweet

# This method reads corpus document and store its rows in created corpus list as dictionary type
# Each row corresponds to the one dictionary data
def readCorpus(corpusFile):
    # List to store tweets
    corpus = []
    
    # Read the corpus.csv file and store each row inside the corpus list
    with open(corpusFile,'r') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in lineReader:
            corpus.append({"tweet_id":row[2], "label":row[1], "topic":row[0]})
    return corpus

# Adding text content of tweet to each dictionary of the row
def buidTrainingSet(twitterObj, corpusFile, tweetDataFile):
    
    # Getting a list that contains rows as dictionaries
    corpus = readCorpus(corpusFile)
    trainingDataSet = []

    for tweet in corpus:
        try:
            # Reading text content of tweet object and adding it to dictionary
            tweet["text"] = readTweetText(twitterObj, int(tweet["tweet_id"]))
            print("Tweet fetched")
            trainingDataSet.append(tweet)
        except: continue

# Storing fetched tweet text and other data into MySQL table for further analysis
def storeMYSQL(dictData,label):
    try:
        connection = mysql.connector.connect(host='localhost', database='nlp', user='root', password='root')
        sql_insert_query = """ INSERT INTO `training_dataset` (`user_id`, `user_name`, `tweet_id`, `text`, `label`) VALUES ("{}","{}","{}","{}","{}")""".format(dictData["user"]["id_str"],dictData["user"]["screen_name"],dictData["id_str"],dictData["text"],label)
        cursor = connection.cursor()
        cursor.execute(sql_insert_query)
        connection.commit()
        print ("Record inserted successfully")

    except mysql.connector.Error as error :
        connection.rollback()                                   #rollback if any exception occured
        print("Failed inserting record with {}".format(error))
        
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            
# Mian function to execute
def main():
    # Twitter API authentication
    CONSUMER_KEY = Credentials.CONSUMER_KEY
    CONSUMER_SECRET = Credentials.CONSUMER_KEY_SECRET
    OAUTH_TOKEN = Credentials.ACCESS_TOKEN
    OAUTH_TOKEN_SECRET = Credentials.ACCESS_TOKEN_SECRET
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    # Getting a list that contains each row of corpus file as dictionary
    corpus = readCorpus('D:/Work/NLP_Final/Processing_and_Storing_Results/corpus.csv')
    
    # Read each row in corpus document
    for tweet in corpus:
        try:
            dictData = readTweet(twitter,tweet["tweet_id"])     # Reading tweet object by using its id
            label = tweet["label"]                              # Read the respective label value of the row
            storeMYSQL(dictData,label)                          # Store both label and tweet text
        except: continue

# The starting point of the script        
if __name__ == "__main__": 
    # calling main function 
    main()
    



