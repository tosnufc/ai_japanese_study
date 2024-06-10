import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
from pykakasi import kakasi
from time import sleep
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def speak_text(command):
    tts = gTTS(text=command, lang='ja')
    tts.save('voice.mp3')
    os.system('start voice.mp3')


translator = Translator()
kakasi = kakasi()
kakasi.setMode("J", "H")  # Japanese to Kana
conv = kakasi.getConverter()


def chat():
    # r = sr.Recognizer()
    r = sr.Recognizer(language='en')
    with sr.Microphone() as source:
        print('Speak Anything :')
        audio = r.listen(source)

        try:
            text = r.recognize(audio)
            print('You said: {}'.format(text))
            translated_text = translator.translate(text, dest='ja').text
            translated_text_kana = conv.do(translated_text)
            translated_text_english = translator.translate(text, dest='en').text
            print('Japanese: {}'.format(translated_text))
            print('Kana: {}'.format(translated_text_kana))
            print('English: {}'.format(translated_text_english))
            speak_text(translated_text)
            # sleep(4)
            # speak_text(translated_text)
            # sleep(4)
            # speak_text(translated_text)

        except LookupError:
            print('Sorry could not recognize your voice')


keep_going = True

while keep_going:
    chat()
    sleep(4)
