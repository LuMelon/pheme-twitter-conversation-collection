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

tweetid = sys.argv[1]
config = configparser.ConfigParser()
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
	tweet = twitter.show_status(id=tweetid)
	print(json.dumps(tweet))
	# with open("test.json", "r") as fr:
	# 	dic = json.load(fr)
	# print(json.dumps(dic))
except:
	print("Error")
	sys.exit()
