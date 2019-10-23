import json
import tweepy
import sys
import pprint
import os
import configparser
import time

tweetid = sys.argv[1]

config = configparser.ConfigParser()
config.read('tweepy.ini')

consumer_key = config.get('Twitter', 'consumer_key')
consumer_secret = config.get('Twitter', 'consumer_secret')
access_key = config.get('Twitter', 'access_key')
access_secret = config.get('Twitter', 'access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

try:
	tweets = api._statuses_lookup(id=tweetid)
	for tweet in tweets:
		print(json.dumps(tweet.json))
	print(tweet)
except:
	raise
	sys.exit()



import json
import sys
import pprint
import os
import configparser
import time
import json
from twython import Twython
import os
import numpy as np
import random
import time
import pickle

tweetids = sys.argv[1]
idlist = tweetids.strip().split(",")
# config = configparser.ConfigParser()
# config.read('twitter.ini')
# consumer_key = config.get('Twitter', 'consumer_key')
# consumer_secret = config.get('Twitter', 'consumer_secret')
# access_key = config.get('Twitter', 'access_key')
# access_secret = config.get('Twitter', 'access_secret')
# twitter = Twython(
#         consumer_key, consumer_secret,
#         access_key, access_secret
#     )
with open("twitter.handler", "rb") as fr:
    twitter = pickle.load(fr)


try:
	tweets = [twitter.show_status(id=tweetid) for tweetid in idlist]
	print('\n'.join([json.dumps(tweet) for tweet in tweets]))
	# with open("test.json", "r") as fr:
	# 	dic = json.load(fr)
	# print(json.dumps(dic))
except:
	print("Error")
	sys.exit()