import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
from pykakasi import kakasi
from time import sleep
import warnings
import keyboard

warnings.filterwarnings("ignore", category=DeprecationWarning)


translator = Translator()
kakasi = kakasi()
kakasi.setMode("J", "H")  # Japanese to Kana
conv = kakasi.getConverter()


def speak_text(sentences):
    print('****************************************************************')
    print('Japanese: {}'.format(sentences))
    tts = gTTS(text=sentences, lang='ja')
    tts.save('voice.mp3')
    os.system('start voice.mp3')
    # print('Please say: {}'.format(sentences))
    # translated_text = translator.translate(sentences, dest='ja').text
    translated_text_kana = conv.do(sentences)
    translated_text_english = translator.translate(sentences, dest='en').text
    # print('Japanese: {}'.format(translated_text))
    print('Kana: {}'.format(translated_text_kana))
    print('English: {}'.format(translated_text_english))


with open('conversation_scripts_backup.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

line = lines.index('*****')+1
cont = True


def go_back(e):
    global line
    line -= 1
    sentences = lines[line]
    speak_text(sentences=sentences)


def go_forward(e):
    global line
    line += 1
    sentences = lines[line]
    speak_text(sentences=sentences)


def repeat(e):
    global line
    sentences = lines[line]
    speak_text(sentences=sentences)


def end_program(e):
    global cont
    cont = False


keyboard.on_press_key('left', go_back)
keyboard.on_press_key('right', go_forward)
keyboard.on_press_key('esc', end_program)
keyboard.on_press_key('up', repeat)

while cont:
    pass
