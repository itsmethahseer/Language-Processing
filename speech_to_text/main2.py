import speech_recognition as sr
from gtts import gTTS
import os


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")

        audio = r.listen(source)
        print("Recognizing Now...")

        try:
            return r.recognize_google(audio)
        except Exception as e:
            print("Error is occured . please try again..." + str(e))


def text_to_speech(text,language = 'en',save_path = 'output.mp3'):
    tts = gTTS(text=text,lang=language,slow=False)
    tts.save(save_path)
    
    os.system(f"xdg-open {save_path}")


text = main()
if __name__ =='__main__':
    text_to_speech(text)