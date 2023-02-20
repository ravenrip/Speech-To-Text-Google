import os
from google.cloud import speech_v1 as speech
from gcp_stt_util import get_filename, save_url_to_gcp_bucket, speech_to_text

config = dict(language_code="en-US")
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     enable_automatic_punctuation=True,
#     audio_channel_count=2,
#     language_code="en-US",
# )

audio = dict(
    uri="gs://stt_temp_lg2/MLKDream.wav"
    # uri="https://ia800207.us.archive.org/29/items/MLKDream/MLKDream.wav"
)

audio_to_text = dict(uri=f"gs://stt_temp_lg2/{get_filename(audio['uri'])}")

if __name__ == "__main__":
    if not audio["uri"].startswith("gs:"):
        save_url_to_gcp_bucket(
            "stt_temp_lg2",
            audio["uri"],
        )
    speech_to_text(audio_to_text["uri"])


# config = dict(language_code="en-US")
# audio_to_text = dict(uri="gs://stt_temp_lg2/MLKDream.wav")
