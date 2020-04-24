#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------

import tweepy
import os
import re
import time
import csv
import polly
from termcolor import cprint
#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")

isSpeaking = False

class Bot:
    def __init__(self):
        consumer_key = "GCViBeSbRGBnQQVCnU2axVVlC"
        consumer_secret = "wG4HOficnoHmvJiSE47J0rPWKy3MDzOat7eLbMbq5mpeswNT0Y"
        access_key = "785797820691472384-01wOyhACcO128k4HsPgr7Bh41WbMmUU"
        access_secret = "By0LJ26nTCpg0dremL8QvryveXqwbNdf8BnulUo6ciWjU"
        try:
            auth = tweepy.OAuthHandler(consumer_key,
                                       consumer_secret)
            auth.set_access_token(access_key, access_secret)

            self.client = tweepy.API(auth)
            if not self.client.verify_credentials():
                raise tweepy.TweepError
        except tweepy.TweepError as e:
            print('ERROR : connection failed. Check your OAuth keys.')
        else:
            print('Connected as @{}, you can start to tweet !'.format(self.client.me().screen_name))
            self.client_id = self.client.me().id
        


    def get_last_tweet(self):
        timeline = []
        while(True):
            tweet = self.client.user_timeline(id = 'realdonaldtrump', tweet_mode="extended")[0]
            result = tweet.full_text
            if "http" not in result:
                result = re.sub(r"http\S+", "", tweet.full_text)
                
                if result not in timeline:
                    timeline.append(result)
                    if "https" in result:

                        pass
                    if("RT" in result):
                        cprint("RT: " + result, 'green')

                        result = result.replace('RT', 'Retweeted')
                        #polly.synthesize('realDonaldTrump has' + result)
                    else:
                        cprint(result, 'green')
                        #polly.synthesize(result)
                time.sleep(15)
            

