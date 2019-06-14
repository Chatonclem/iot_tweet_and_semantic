# IOT_TWEET_AND_SEMANTIC
Visualisation avec LEDS des sentiments de tweet

## Description
Programme qui visualise sur une matrice LED le sentiment des tweets reçus. Le projet utilise l'API AWS comprehend.

## Groupe
Antoine LEVY,  Clementine THORNARY, Slaheddine BEJAOUI, Alexandre GARCIAS

## Etat de l'existant

https://www.sitepoint.com/home-made-twitter-and-gmail-notifications-with-php-and-arduino/

## Dependencies

**tweepy** twitter library  

**boto3 awscli** AWS Comprehend library

**gTTS** Google text to speech library

**Gpio** Library to manage I/O to turn on/off the leds

## Installation 

**Install git and mpg321 :**

	apt-get install git mpg321

**Upgrade python3 :**

	apt-get upgrade python3

**Install the dependencies :**

	pip install tweepy boto3 awscli gtts

**Clone the git repository :**

	git clone https://github.com/Chatonclem/iot_tweet_and_semantic.git

## Utilisation

* The script will recover tweets from twitter considering the hashtag
* It will request AWS comprehend api to detect language and sentiment
* The leds will be turn on depending on the sentiment
* The tweet will be read by the speaker
* The leds will finaly turn off

**Before using the script, you will have to set the twitter credentials !** If you don't have any, look at this : https://developer.twitter.com/

**Launch the script**

	python ~/iot_tweet_and_semantic/main.py

**You can specify a specific hashtag : **

	python ~/iot_tweet_and_semantic/main.py hashtag

**You can activate a verbose mode for DEBUG like this : **

	python ~/iot_tweet_and_semantic/main.py hashtag debug
