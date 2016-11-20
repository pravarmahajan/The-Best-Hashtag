from twitter import *
import twitter_config
import json

oauth = OAuth (twitter_config.ACCESS_TOKEN,
			   twitter_config.ACCESS_SECRET,
			   twitter_config.CONSUMER_KEY,
			   twitter_config.CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

with open('hashtags.dat', 'r') as f:
    hashtags = json.load(f)

