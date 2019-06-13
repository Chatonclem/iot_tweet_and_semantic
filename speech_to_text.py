import boto3
from gtts import gTTS
import os

s3 = boto3.resource('s3')
#response = s3.create_bucket(
#    ACL='public-read-write',
#    Bucket='buckiot-5ibd',
#CreateBucketConfiguration={
#        'LocationConstraint': 'eu-west-1'
#    }
#)
#s3.meta.client.upload_file('test_ant.mp3', 'buckiot-5ibd', 'test_ant.mp3')

transcribe = boto3.client('transcribe')

#response2 = transcribe.start_transcription_job(
#    TranscriptionJobName='speech-to-text-iot-2',
#    LanguageCode='fr-FR',
#    MediaFormat='mp3',
#    Media={
#        'MediaFileUri': 'https://s3-eu-west-1.amazonaws.com/buckiot-5ibd/test_ant.mp3'
#    }
#)

response = transcribe.get_transcription_job(
    TranscriptionJobName='speech-to-text-iot-2'
)

print(response)