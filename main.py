
import os

from gcp_stt_util import speech_to_text

config = dict(language_code="en-US")
audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     enable_automatic_punctuation=True,
#     audio_channel_count=2,
#     language_code="en-US"
# )
# audio = dict(uri="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0010_8k.wav")

speech_to_text(config, audio)
