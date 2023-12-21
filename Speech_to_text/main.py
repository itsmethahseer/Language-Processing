import speech_recognition as sr
from os import path
from pydub import AudioSegment
import ffmpeg
from language_tool_python import LanguageTool
import prose
import afterglowpy

# convert mp3 file to wav  if needed
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "/home/c847/Desktop/Language Processing/Speech_to_text/audio/music.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    print("Processing the file .....")
    audio = r.record(source)  # read the entire audio file
    text = "Transcription: " + r.recognize_google(audio)
    # Basic grammar correction with LanguageTool
    tool = LanguageTool("en")
    corrected_text = tool.correct(text)
    # prose_tool = prose.models.bart.bart_corrector(temperature=0.7)
    # suggestions = prose_tool.correct(corrected_text)
    # final_text = afterglowpy.edit(suggestions.text, edits=[afterglowpy.edits.Replace("colorful", "vibrant")])
    print(corrected_text)
