from twitter import *
import twitter_config
import time
import re
import string

lat, long = 40.0162680,-83.0151910

def authenticate():
    oauth = OAuth (twitter_config.ACCESS_TOKEN,
                   twitter_config.ACCESS_SECRET,
                   twitter_config.CONSUMER_KEY,
                   twitter_config.CONSUMER_SECRET)
    twitter_handle = Twitter(auth=oauth)
    return twitter_handle

def get_trending_topics(twitter_handle, loc):
    response = twitter_handle.trends.closest(lat = loc[0], long = loc[1])
    woeid = response[0]['woeid']
    trends = twitter_handle.trends.place(_id=woeid)
    cur_time = int(time.time())
    hashtags = [trend['name'][1:] + '\t' + str(cur_time)
                for trend in trends[0]['trends']
                if trend['name'].startswith('#')]

    with open('data/hashtags.dat', 'a') as f:
        f.writelines('\n'.join(hashtags))

    return hashtags

def get_and_save_tweets_for_hashtags(twitter_handle, hashtags):
    for ht in hashtags:
        tweets = twitter_handle.search.tweets(q='#' + ht, result_type='recent',
                                       lang='en',
                                       count=50)
        tweet_data = [tweet['text'] for tweet in tweets['statuses']]
        other_hashtags = [h for tweet in tweets['statuses']
                          for h in tweet['entities']['hashtags']]
        with open('data/'+ ht + '_tweet.dat', 'a') as f:
            f.writelines('\n'.join(tweet_data))

def main():
    twitter_handle = authenticate()
    while True:
        hashtags = get_trending_topics(twitter_handle, (lat, long))
        hashtags = [ht.split('\t')[0].lower() for ht in hashtags]
        get_and_save_tweets_for_hashtags(twitter_handle, hashtags)
        time.sleep(300)

if __name__ == "__main__":
    main()