from twitter import *
import json
import twitter_config
import requests

oauth = OAuth (twitter_config.ACCESS_TOKEN,
			   twitter_config.ACCESS_SECRET,
			   twitter_config.CONSUMER_KEY,
			   twitter_config.CONSUMER_SECRET)
twitter = Twitter(auth=oauth)
lat, long = 40.0162680,-83.0151910
response = twitter.trends.closest(lat=lat, long=long)
woeid = response[0]['woeid']
trends = twitter.trends.place(_id=woeid)
hashtags = [trend['name'] for trend in trends[0]['trends'] if
            trend['name'].startswith('#')]
print('\n'.join(hashtags))