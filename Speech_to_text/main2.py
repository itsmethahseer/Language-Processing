import os
import speech_recognition as sr

# Corrected file path
AUDIO_FILE = "music.wav"
abs_path = os.path.abspath(AUDIO_FILE)

# transcribe audio file
AUDIO_FILE = "Speech_to_text/audio/music.wav"

if not os.path.exists(AUDIO_FILE):
    print(f"Error: File not found at {AUDIO_FILE}")
else:
    with sr.AudioFile(abs_path) as source:
        audio = r.record(source)  # read the entire audio file

        print("Transcription: " + r.recognize_google(audio))
