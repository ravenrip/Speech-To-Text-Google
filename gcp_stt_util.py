import os
import urllib.request

# import noisereduce as nr
import requests
from google.cloud import storage
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# This file needs to be created. Refer to the README.md file for more info
import os_environ_util

# from scripy.io import wavfile


def speech_to_text_beta(gcs_uri):
    from google.cloud import speech_v1p1beta1 as speech
    from google.cloud.speech_v1p1beta1 import enums, types

    client = speech.SpeechClient()
    audio = types.RecognitionAudio(uri=gcs_uri)
    config = speech.types.RecognitionConfig(
        language_code="en-US",
        enable_speaker_diarization=True,
        diarization_speaker_count=2,
    )
    operation = client.long_running_recognize(config, audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=3000)
    result = response.results[-1]

    words_info = result.alternatives[0].words

    tag = 1
    speaker = ""

    for word_info in words_info:
        if word_info.speaker_tag == tag:
            speaker = speaker + " " + word_info.word

        else:
            print("speaker {}: {}".format(tag, speaker))
            tag = word_info.speaker_tag
            speaker = "" + word_info.word

    print("speaker {}: {}".format(tag, speaker))


def speech_to_text(gcs_uri, _sample_rate_hertz=16000):
    from google.cloud import speech_v1 as speech

    # sourcery skip: inline-immediately-returned-variable
    """
    returns the Google Speech-To-Text result

    :param _type_ config: the configuration used for the google.cloud.speech.configuration
    :param _type_ audio: the fill GCP bucket uri for the audio file
    """
    # client = speech.SpeechClient()
    # response = client.recognize(config=config, audio=audio)
    # print_sentences(response)
    # return response

    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=_sample_rate_hertz,
        language_code="en-US",
    )

    # config = speech.v1p1beta1.types.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    #     sample_rate_hertz=_sample_rate_hertz,
    #     language_code="en-US",
    #     enable_speaker_diarization=True,
    #     diarization_speaker_count=2,
    # )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=1800)

    transcripts = {}
    for result in response.results:
        if result.alternatives and result.alternatives[0].words:
            speaker_tag = result.alternatives[0].words[0].speaker_tag
            if speaker_tag not in transcripts:
                transcripts[speaker_tag] = ""
            transcripts[speaker_tag] += result.alternatives[0].transcript

    for speaker_tag, transcript in transcripts.items():
        print(f"Speaker {speaker_tag}: {transcript}")

    # for result in response.results:
    #     # The first alternative is the most likely one for this portion.
    #     print(f"Transcript: {result.alternatives[0].transcript}")
    #     print(f"Confidence: {result.alternatives[0].confidence}")


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")


def save_url_to_gcp_bucket(bucket_name, url):  # sourcery skip: extract-method
    """
    Given a name of a GCP bucket and a URL for an audio file, save the file into the given GPC Bucket

    _extended_summary_

    :param _type_ bucket_name: name of the GCP bucket
    :param _type_ url: URL of the audio file
    """
    # data = fetch_url(url)
    # Get GCP credentials
    # setting Google credentials
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"
    ] = "C:\Dev\LG2 Solutions\Speech-To-Text-Google\gcloud_do_not_share\dictation-sample-82bc323451d9.json"

    os.environ["GOOGLE_PROJECT_ID"] = "dictation-sample"
    credentials_file = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    try:
        storage_client = storage.Client()
        buckets = storage_client.list_buckets()
        if any(x.id == bucket_name for x in buckets):
            bucket = storage_client.get_bucket(bucket_name)
        else:
            bucket = storage_client.bucket(bucket_name)
            bucket.storage_class = "STANDARD"
            new_bucket = storage_client.create_bucket(bucket, location="us")
            print(
                f"Created bucket {new_bucket.name} in {new_bucket.location} with storage class {new_bucket.storage_class}"
            )
        blob = bucket.blob(url.split("/")[-1])
        # Pull the file name from the URL
        # file_name = clean_wavfile(get_filename(url))
        file_name = get_filename(url)
        # urllib.request.urlretrieve(url, f"./{file_name}")

        response = requests.get(url, stream=True)
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(100000):
                file.write(chunk)
        #     f_web.write(response.content)

        blob.upload_from_filename(file_name)
        print(f"File {file_name} saved in bucket {bucket_name}")
    except HttpError as error:
        print(f"An error occurred while saving the file: {error}")


def get_filename(url):
    head, file_name = os.path.split(url)
    return file_name


def fetch_url(url):
    # Create a request with the Accept header
    req = urllib.request.Request(url, headers={"Accept": "audio/wav"})
    response = urllib.request.urlretrieve(req)
    return response.read()


def clean_wavfile(wavfile):
    # load data
    rate, data = wavfile.read(wavfile)
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(f"filtered_{wavfile}", rate, reduced_noise)
    return f"filtered_{wavfile}"
