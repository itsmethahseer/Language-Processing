import speech_recognition as sr
from os import path
from pydub import AudioSegment
import ffmpeg
import av as acconv

# convert mp3 file to wav  if needed
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "/home/c847/Desktop/Language Processing/Speech_to_text/audio/music.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
    print("Transcription: " + r.recognize_google(audio))
