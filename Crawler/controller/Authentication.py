"""
  _____               _     _____ _            ____
 |_   _| __ _   _ ___| |_  |_   _| |__   ___  / ___|  ___  _   _ _ __ ___ ___
   | || '__| | | / __| __|   | | | '_ \ / _ \ \___ \ / _ \| | | | '__/ __/ _ \
   | || |  | |_| \__ \ |_    | | | | | |  __/  ___) | (_) | |_| | | | (_|  __/
   |_||_|   \__,_|___/\__|   |_| |_| |_|\___| |____/ \___/ \__,_|_|  \___\___|

Created by Daniel Slobben, Michael van der Veen & Margot Verleg

Creation Date: 
    
Class: 
    
Contributors:

Description:

ChangeLog:

"""
import tweepy
import time
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


class Authentication:
    def __init__(self):
        print(time.ctime(time.time()) + ": AUTH/INFO: Loggin in")
        self.auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
        self.auth.set_access_token(key=access_token, secret=access_token_secret)

        self.api = tweepy.API(self.auth)

        self.public_tweets = self.api.home_timeline()
        for tweet in self.public_tweets:
            print(time.ctime(time.time()) + ": TIMELINE: "+tweet.text)
