import os
import urllib.request

from google.cloud import speech_v1 as speech
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# This file needs to be created. Refer to the README.md file for more info
import os_environ_util


def speech_to_text(config, audio):
    # sourcery skip: inline-immediately-returned-variable
    """
    returns the Google Speech-To-Text result

    :param _type_ config: the configuration used for the google.cloud.speech.configuration
    :param _type_ audio: the fill GCP bucket uri for the audio file
    """
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)
    return response


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")


def save_url_to_gcp_bucket(bucket_name, url):
    """
    Given a name of a GCP bucket and a URL for an audio file, save the file into the given GPC Bucket

    _extended_summary_

    :param _type_ bucket_name: name of the GCP bucket
    :param _type_ url: URL of the audio file
    """
    data = fetch_url(url)

    # Create a new bucket in Google Cloud Storage
    credentials = Credentials.from_authorized_user_info()
    service = build("storage", "v1", credentials=credentials)
    try:
        bucket = (
            service.buckets()
            .insert(project=os.environ["GOOGLE_PROJECT_ID"], body={"name": bucket_name})
            .execute()
        )
        print(f"Bucket {bucket_name} created")
    except HttpError as error:
        print(f"An error occurred while creating the bucket: {error}")
        bucket = None

    # Save file in the new bucket
    if bucket is not None:
        try:
            bucket_name = bucket["name"]
            # Pull the file name from the URL
            head, tail = os.path.split(url)
            file_name = tail
            service.objects().insert(
                bucket=bucket_name, body={"name": file_name}, media_body=data
            ).execute()
            print(f"File {file_name} saved in bucket {bucket_name}")
        except HttpError as error:
            print(f"An error occurred while saving the file: {error}")


def fetch_url(url):
    # Create a request with the Accept header
    req = urllib.request.Request(url, headers={"Accept": "audio/x-wav"})
    response = urllib.request.urlopen(req)
    return response.read()
