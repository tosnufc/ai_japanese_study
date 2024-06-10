import requests
import os

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

url = "https://api.elevenlabs.io/v1/text-to-speech/j210dv0vWm7fCknyQpbA"

with open(f'.env', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

api_key = lines[0].split(' ')[-1]

for n in range(len(ja_conv)):
    payload = {
        "text": f"{ja_conv[n]}",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        },
        "seed": 1,
        "model_id": "eleven_multilingual_v2"
    }
    headers = {
        "xi-api-key": f"{api_key}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    # Save the audio content into an mp3 file
    with open(f'elevenlab_ja_voice_{n}.mp3', 'wb') as f:
        f.write(response.content)
        print(f'Writing elevenlab_ja_voice_{n}.mp3...')
    # os.system('start elevenlab_ja_voice.mp3')

