import pickle
import twitter_process_data
import sys
import requests
import json
import pandas

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('knn.pkl', 'rb') as f:
    nn_obj = pickle.load(f)

with open('dataset.pkl', 'rb') as f:
    tweet_data_vectorized, tags = pickle.load(f)

#new_tweet = sys.argv[1:].join(' ')
new_tweet = 'hackathon 2016 at ohio'
new_tweet = twitter_process_data.clean_tweet(new_tweet)
transformed_tweet = vectorizer.transform([new_tweet])
distances, indices = nn_obj.kneighbors(transformed_tweet)

answer_set = set()
for i in range(10):
    answer_set.add('#'+tags[indices[0, i]])

#top_trending = requests.request(method='GET',url=
#'http://ec2-54-214-119-83.us-west-2.compute.amazonaws.com/hackathon
# /getLatestTweets.php')
#top_trending = json.loads(top_trending)['result']
#d = pandas.dataframe(top_trending)
#print('nothing')