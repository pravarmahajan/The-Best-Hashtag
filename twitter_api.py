from collections import defaultdict
from twitter import *
import twitter_config
import time
import twitter_process_data
import requests
import json

lat, long = 40.0162680,-83.0151910

def authenticate():
    oauth = OAuth (twitter_config.ACCESS_TOKEN,
                   twitter_config.ACCESS_SECRET,
                   twitter_config.CONSUMER_KEY,
                   twitter_config.CONSUMER_SECRET)
    twitter_handle = Twitter(auth=oauth)
    return twitter_handle

def get_trending_topics(twitter_handle, loc):
    filename = 'data/hashtags.dat'
    response = twitter_handle.trends.closest(lat = loc[0], long = loc[1])
    woeid = response[0]['woeid']
    trends = twitter_handle.trends.place(_id=woeid)
    cur_time = int(time.time())
    hashtags = list()

    for trend in trends[0]['trends']:
        if trend['name'].startswith('#'):
            if all(ord(c) < 128 for c in trend['name']):
                hashtags.append({'hash_tag': trend['name'][1:], 'time': cur_time})
    response = requests.post(twitter_config.database_url,
                             data={'data': json.dumps(hashtags)})

    return hashtags

def get_and_save_tweets_for_hashtags(twitter_handle, hashtags):
    new_dict = defaultdict(set)
    data = []
    for ht in hashtags:
        tweets = twitter_handle.search.tweets(q='#' + ht, result_type='recent',
                                       lang='en',
                                       count=5)

        for tweet in tweets['statuses']:
            for h in tweet['entities']['hashtags']:
                cleaned_tweet = twitter_process_data.clean_tweet(
                    tweet['text']).strip()
                new_dict[h['text']].add(cleaned_tweet)

    for (tag, tweets) in new_dict.items():
        if all(ord(c) < 128 for c in tag):
            for tweet in tweets:
                data.append(tag)
                data.append(tweet)

    with open('data/all_tweets3.dat', 'a') as f:
        f.writelines('\n'.join(data))

def main():
    twitter_handle = authenticate()
    while True:
        hashtags = get_trending_topics(twitter_handle, (lat, long))
        hashtags = [ht['hash_tag'] for ht in hashtags]
        get_and_save_tweets_for_hashtags(twitter_handle, hashtags)
        time.sleep(300)

if __name__ == "__main__":
    main()