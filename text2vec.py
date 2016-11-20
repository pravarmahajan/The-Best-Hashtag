from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import glob
import twitter_process_data
import time
import pickle
from sklearn.neighbors import NearestNeighbors

while(True):
    files = glob.glob('data/*.txt')
    twitter_data = list()
    tags = list()

    for file in files:
        with open(file, 'r') as f:
            lines = list(map(str.strip, f.readlines()))
            num_lines = len(lines)/2
            hashtags = lines[::2]
            tweets = lines[1::2]
            for tweet in tweets:
                twitter_data.append(twitter_process_data.clean_tweet(tweet))
            tags.extend(hashtags)

    vectorizer = TfidfVectorizer(
                       lowercase=True,
                       stop_words=nltk.corpus.stopwords.words('english'),
                       strip_accents='ascii',
                       min_df=1)

    tweet_data_vectorized = vectorizer.fit_transform(twitter_data)

    nn_obj = NearestNeighbors(n_neighbors=15, metric='cosine',
                              algorithm='brute').fit(tweet_data_vectorized)

    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

    with open('dataset.pkl', 'wb') as f:
        pickle.dump([tweet_data_vectorized, tags], f)

    with open('knn.pkl', 'wb') as f:
        pickle.dump(nn_obj, f)
    print('Running...')
    time.sleep(1800)