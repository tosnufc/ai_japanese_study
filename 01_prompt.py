import openai
import os

client = openai.OpenAI()

# gpt_model = "gpt-3.5-turbo"
gpt_model = "gpt-4o"


def get_completion(prompt, model=gpt_model, temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


# prompt = f"""
# You are a language teacher AI assistant.
# Your task is to generate a conversation of a restaurant customer and a waitress.
# The customer is vegan. He wants to order food but would like to ask what are the vegan choices on the menu.
# He wants to ask about the ingredients on the item on the menu that he's interested in whether they contain any non-vegan ones or not.
# If it contains non-vegan ingredients, he wants to ask whether it is possible to substitute these ingredients with some vegan ingredients or not.
#
# The waiter is helpful and very polite.
#
#
#
# format the output as follows:
#
# Waiter: Good morning. Welcome to our restaurant.
# Customer: <put customer sentence here>
# Waiter: <put waiter sentence here>
#
# """
# response = get_completion(prompt)
# print(response)
#
# conversation = response
#
# prompt = f"""
# Rewrite the following conversation into everyday use and informal Japanese language.
# Make sure you make the conversation sounds natural in Japanese language, not just translating it directly.
#
# {conversation}
#
# """
# response = get_completion(prompt, temperature=0.7)
# print(response)


# scenario = f"""
# The customer is vegan. He wants to order food but would like to ask what are the vegan choices on the menu.
# He wants to ask about the ingredients on the item on the menu that he's interested in whether they contain any non-vegan ones or not.
# If it contains non-vegan ingredients, he wants to ask whether it is possible to substitute these ingredients with some vegan ingredients or not.
#
# The waiter is helpful and very polite.
# """
#
# prompt = f"""
# You are a language teacher AI assistant.
# Your task is as follows:
# - generate a conversation of a restaurant customer and a waitress in English from the scenario below.
#       <<<{scenario}>>>
# - convert the conversation you have generated into Japanese langauge using tone for everyday use.
#
# When converting into Japanese language, make sure you make it sounds natural in Japanese language, not just translating it directly.
#
# format the output as follows:
#
# Waiter: Good morning. Welcome to our restaurant.
# Customer: <put your generated customer sentence here>
# Waiter: <put generated waiter sentence here>
# Customer:
# Waiter:
# *****
# <put your conversation translation here>
# """


scenario = f"""
Two close friends are talking about their travel plan within Japan. They will have 1-week off for their vacation. They like nature and quite places.
"""

prompt = f"""
You are a language teacher AI assistant.
Your task is as follows:
- generate a conversation in English from the scenario below.
      <<<{scenario}>>>
- convert the conversation you have generated into Japanese langauge using tone for everyday use.

When converting into Japanese language, make sure you make it sounds natural in Japanese language, not just translating it directly.

format the output as follows:

Person A: <put your generated sentence here> 
Person B: <put your generated sentence here>
Person A: <put your generated sentence here>
Person B:
Person A:
*****
<put your conversation translation here>
"""


response = get_completion(prompt, temperature=0.7)
print(response)

# save the response to a text file named ‘conversation.txt’
with open('conversation_scripts.txt', 'w', encoding='utf-8') as f:
    f.write(response)
