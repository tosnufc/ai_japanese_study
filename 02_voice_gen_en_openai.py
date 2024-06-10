from pathlib import Path
from openai import OpenAI
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

client = OpenAI()

with open('conversation_scripts.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


def divide_list(lst, delimiter):
    try:
        # Find the index of the delimiter
        idx = lst.index(delimiter)
        # Slice the list into two parts based on the index of the delimiter
        return lst[:idx], lst[idx+1:]
    except ValueError:
        # If the delimiter is not in the list, return the original list and an empty list
        return lst, []


lst = lines
delimiter = '*****\n'
en_conv, ja_conv = divide_list(lst, delimiter)

for n in range(len(en_conv)-1):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=en_conv[n],
    )
    speech_file_path = Path(__file__).parent / f"openai_en_voice_{n}.mp3"
    print(f"Writing openai_en_voice_{n}.mp3...")
    response.stream_to_file(speech_file_path)
