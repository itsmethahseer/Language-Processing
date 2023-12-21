# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "Your assemblyai api key here"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("/home/c847/Desktop/Language Processing/Speech_to_text/audio/music.wav")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)