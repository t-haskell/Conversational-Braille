from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from utils.config import API_KEY, API_URL  # Import config variables

def initialize_transcription_service():
    """Initializes the IBM Watson transcription service."""
    authenticator = IAMAuthenticator(API_KEY)
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(API_URL)
    return speech_to_text

def transcribe_audio(file_path):
    """Transcribes audio from the given file using IBM Watson."""
    speech_to_text = initialize_transcription_service()
    with open(file_path, "rb") as audio_file:
        response = speech_to_text.recognize(audio=audio_file, content_type="audio/wav")
        return response.result["results"][0]["alternatives"][0]["transcript"]