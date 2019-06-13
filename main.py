import boto3
import tweepy
try:
    import json
except ImportError:
    import simplejson as json

# Variables that contains the user credentials to access Twitter API
TWITTER_ACCESS_TOKEN = 'XXX'
TWITTER_ACCESS_SECRET = 'XXX'
TWITTER_CONSUMER_KEY = 'XXX'
TWITTER_CONSUMER_SECRET = 'XXX'
# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

for tweet in tweepy.Cursor(api.search, q='#trump').items(1):
    print(tweet._json["text"])
    # clean_text = re.sub('[^A-Za-z0-9]+', '', status._json["text"])
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
    print(json.dumps(comprehend.detect_sentiment(Text=tweet._json["text"], LanguageCode='en'), sort_keys=True, indent=4))
