import io
import os

from google.cloud import speech_v1 as speech

#setting Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='C:\Dev\LG2 Solutions\Speech-To-Text-Google\gcloud_do_not_share\dictation-sample-82bc323451d9.json'


def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")
        

#config = dict(language_code="en-US")
#audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    enable_automatic_punctuation=True,
    audio_channel_count=2,
    language_code="en-US"
)
audio = dict(uri="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0010_8k.wav")

speech_to_text(config,audio)


