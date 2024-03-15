# backend/services/transcription_service.py

import os
from google.cloud import speech_v1p1beta1 as speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/smallbrain/Downloads/comedian_joke_app/credentials.json'

def transcribe_audio(audio_file_path, language_code='en-US'):
    client = speech.SpeechClient()

    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript