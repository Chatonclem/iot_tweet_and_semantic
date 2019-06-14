import sys
import boto3
from gtts import gTTS
import os
import RPi.GPIO as GPIO
import time
import wget

try:
    import json
except ImportError:
    import simplejson as json
    
def analyze_speech(file_name):
    s3 = boto3.resource('s3')

    #response = s3.create_bucket(
    #    ACL='public-read-write',
    #    Bucket='buckiot-5ibd',
    #CreateBucketConfiguration={
    #        'LocationConstraint': 'eu-west-1'
    #    }
    #)

    s3.meta.client.upload_file(name_file_mp3, 'buckiot-5ibd', name_file_mp3)

    transcribe = boto3.client('transcribe')

    response2 = transcribe.start_transcription_job(
        TranscriptionJobName='speech-to-text-iot_' + name_file_mp3,
        LanguageCode='fr-FR',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': 'https://s3-eu-west-1.amazonaws.com/buckiot-5ibd/' + name_file_mp3
        }
    )

    time.sleep(10)

    response = transcribe.get_transcription_job(
        TranscriptionJobName='speech-to-text-iot_' + name_file_mp3
    )

    status = response["TranscriptionJob"]["TranscriptionJobStatus"]
    print(status)

    while status != "COMPLETED":
        time.sleep(5)
        response = transcribe.get_transcription_job(
            TranscriptionJobName='speech-to-text-iot_' + name_file_mp3
        )
        status = response["TranscriptionJob"]["TranscriptionJobStatus"]
        print(status)


    url = response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
    if os.path.exists("transcript.json"):
        os.remove("transcript.json")
    wget.download(url, 'transcript.json')
    with open('transcript.json') as json_file:
        data = json.load(json_file)
        print(data["results"]["transcripts"][0]["transcript"])
        return data["results"]["transcripts"][0]["transcript"]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

def quit_properly():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    
def loop(text, debug=False):
    if debug:
        print(">>> DEBUG text : " + str(text))
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
    lang = json.loads(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True, indent=4))["Languages"][0]["LanguageCode"]
    if debug:
        print(">>> DEBUG language : " + str(lang))
    sentiment = json.loads(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode=lang), sort_keys=True, indent=4))["Sentiment"]
    if sentiment == "NEGATIVE":
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(20, GPIO.HIGH)
    elif sentiment == "POSITIVE":
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(21, GPIO.HIGH)
    elif sentiment == "NEUTRAL":
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(16, GPIO.HIGH)
    else:
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        
    time.sleep(10)

    if sentiment == "NEGATIVE":
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(20, GPIO.LOW)
    elif sentiment == "POSITIVE":
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(21, GPIO.LOW)
    elif sentiment == "NEUTRAL":
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(16, GPIO.LOW)
    else:
        if debug:
            print(">>> DEBUG Sentiment : " + str(sentiment))
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)

if __name__ == "__main__":
    name_file_mp3 = 'film.mp3'
    text = analyze_speech(name_file_mp3)
    setup() 
    loop(text)
    quit_properly()
    


