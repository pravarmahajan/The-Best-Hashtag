def remove_RT(tweet_text):
    tweet_text = re.sub(twitter_config.RT_regex, "", tweet_text)
    return tweet_text


def remove_hashtag(tweet_text):
    tweet_text = re.sub(twitter_config.hashtag_pattern, "", tweet_text)
    return tweet_text

def remove_at_username(tweet_text):  # removes @username
    tweet_text = re.sub(twitter_config.at_reference_pattern, "", tweet_text)
    return tweet_text

def remove_punctuations(tweet_text):
    table = str.maketrans({key: None for key in string.punctuation})
    return tweet_text.translate(table)

def remove_http(tweet_text):
        return re.sub(twitter_config.http_regex, '', tweet_text,
               flags=re.MULTILINE)

def remove_non_alphanumeric(tweet_text):
    alphanum_regex = "[^A-Za-z0-9\s]+"
    tweet_text = re.sub(alphanum_regex, "", tweet_text)
    return tweet_text

def clean_tweet(tweet_text):
    tweet_text = tweet_text['text']
    tweet_text = remove_hashtag(tweet_text)
    tweet_text = remove_at_username(tweet_text)
    tweet_text = remove_RT(tweet_text)
    tweet_text = remove_http(tweet_text)
    tweet_text = remove_punctuations(tweet_text)
    tweet_text = remove_non_alphanumeric(tweet_text)
    return tweet_text