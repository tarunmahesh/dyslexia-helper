import openai
import nltk
import math
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
openai.api_key = secret

def extract_topics(text, num_of_sentences):
    summary = "Write a summary that is " + str(num_of_sentences) + " sentences long on the following text that includes no pronouns: " + text
    messages = [{"role": "user", "content": summary}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )

    return sent_tokenize(response.choices[0].message["content"])

def create_prompt(topic):
    new_topic = "Turn the following sentence into a prompt for dall-e so that it illustrates the image as a traditional cartoon. Make sure that the prompt includes that the picture should have no letters/textual elements/speech bubbles of any kind. Lastly, make sure that the prompt doesn't include pronouns of any kind.: " + topic
    messages = [{"role": "user", "content": new_topic}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]

def create_image(prompt):
    return openai.Image.create(prompt=prompt, n=1, size="1024x1024")["data"][0]["url"]

def get_pictures(text):
    img_list = []
    for topic in extract_topics(text, math.ceil(len(sent_tokenize(text))/5)):
        img_list.append(create_image(create_prompt(topic)))
    return img_list
