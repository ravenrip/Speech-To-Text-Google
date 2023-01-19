# Import the Speech-to-Text client library
from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://stt_temp_lg2/MLKDream.wav"


def transcribe_speech():
    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=22050,
        language_code="en-US",
        model="video",
        audio_channel_count=1,
        enable_automatic_punctuation=True,
        profanity_filter=True,
        use_enhanced=True,
        enable_word_time_offsets=True,
        max_alternatives=3,
        diarization_config=speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True,
            min_speaker_count=1,
            max_speaker_count=1,
        ),
    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=180)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")


transcribe_speech()

# def transcribe_speech():
#     audio = speech.RecognitionAudio(uri=gcs_uri)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.MP3,
#     sample_rate_hertz=44100,
#     language_code="en-US",
#     model="video",
#     audio_channel_count=2,
#     enable_automatic_punctuation=True,
#     use_enhanced=True,
#     enable_word_time_offsets=True,
#     max_alternatives=3,
#     diarization_config=speech.SpeakerDiarizationConfig(
#         enable_speaker_diarization=True,
#         min_speaker_count=2,
#         max_speaker_count=2,
#     ),
# )
