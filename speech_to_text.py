import boto3
import json
import os
import wget
import time

s3 = boto3.resource('s3')

#response = s3.create_bucket(
#    ACL='public-read-write',
#    Bucket='buckiot-5ibd',
#CreateBucketConfiguration={
#        'LocationConstraint': 'eu-west-1'
#    }
#)

name_file_mp3 = 'film.mp3'
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

#print(response["TranscriptionJob"]["results"]["transcripts"])