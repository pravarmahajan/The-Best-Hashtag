import pickle
import twitter_process_data

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('knn.pkl', 'rb') as f:
    nn_obj = pickle.load(f)

with open('dataset.pkl', 'rb') as f:
    tweet_data_vectorized, tags = pickle.load(f)

new_tweet = 'england are giving a good fight'
new_tweet = twitter_process_data.clean_tweet(new_tweet)
transformed_tweet = vectorizer.transform([new_tweet])
distances, indices = nn_obj.kneighbors(transformed_tweet)

for i in range(10):
    print(tags[indices[0, i]])