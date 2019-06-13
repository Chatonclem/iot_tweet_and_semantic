import boto3
import tweepy
from gtts import gTTS
import os

# # !/usr/bin/env python3.6
# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(16, GPIO.OUT)
# GPIO.setup(20, GPIO.OUT)
# GPIO.setup(21, GPIO.OUT)

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
    text = tweet._json["text"]
    print(">>> DEBUG text : " + str(text))
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
    lang = json.loads(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True, indent=4))["Languages"][0]["LanguageCode"]
    print(">>> DEBUG language : " + str(lang))
    sentiment = json.loads(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode=lang), sort_keys=True, indent=4))["Sentiment"]
    if sentiment == "NEGATIVE":
        print(">>> DEBUG Sentiment : " + str(sentiment))
        # GPIO.output(16, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(16, GPIO.LOW)
    elif sentiment == "POSITIVE":
        print(">>> DEBUG Sentiment : " + str(sentiment))
        # GPIO.output(20, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(20, GPIO.LOW)
    elif sentiment == "NEUTRAL":
        print(">>> DEBUG Sentiment : " + str(sentiment))
        # GPIO.output(21, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(21, GPIO.LOW)
    else:
        print(">>> DEBUG Sentiment : " + str(sentiment))
        # GPIO.output(16, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(16, GPIO.LOW)
        # GPIO.output(20, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(20, GPIO.LOW)
        # GPIO.output(21, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(21, GPIO.LOW)

    tts=gTTS(text=text,lang=lang)
    tts.save("test.mp3")
    os.system("start test.mp3")