# IOT_TWEET_AND_SEMANTIC
Visualisation avec LEDS des sentiments de tweet

## Description
Programme qui visualise sur une matrice LED le sentiment des tweets reçus. Le projet utilise l'API AWS comprehend.

## Groupe
Antoine LEVY,  Clementine THORNARY, Slaheddine BEJAOUI, Alexandre GARCIAS

## Etat de l'existant

https://www.sitepoint.com/home-made-twitter-and-gmail-notifications-with-php-and-arduino/

## Dependencies

**tweepy boto3 awscli gTTS Gpio**

## Installation 

**Install git and :**

	apt-get install git

**Upgrade python3 :**

suivre ces étapes : 

https://gist.github.com/SeppPenner/6a5a30ebc8f79936fa136c524417761d

**Install miniconda :**

	wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
	md5sum Miniconda3-latest-Linux-armv7l.sh
	bash Miniconda3-latest-Linux-armv7l.sh

**Create a conda env :**

	conda create -n iotenv python=3.4

**Activate your conda env :**

	conda activate iotenv

**Install the dependencies :**

	pip install tweepy boto3 awscli gtts

**Clone the git repository :**

	git clone https://github.com/Chatonclem/iot_tweet_and_semantic.git

## Utilisation

**Launch the script**

python ~/iot_tweet_and_semantic/main.py
