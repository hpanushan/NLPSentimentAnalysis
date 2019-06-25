from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from StoringMySQL import storeMYSQL
import json

import Credentials

class StdOutListener(StreamListener):

    def on_data(self, data):
        dictData = json.loads(data)                 # Convert string into dictionary
        storeMYSQL(dictData)             # Adding data to MySQL database
        return True
    
    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
    ## Filtering the tweets
    stream.filter(track = ["donald trump"])