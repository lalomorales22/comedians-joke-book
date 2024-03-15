# backend/services/language_model_service.py

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
import os

openai_api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=openai_api_key)

def generate_joke_name(transcribed_text):
    prompt = f"Generate a short and catchy name for the joke based on the following transcribed text:\n\n{transcribed_text}\n\nJoke Name:"
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates joke names based on transcribed text."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    joke_name = response.choices[0].message.content.strip()
    return joke_name

def generate_joke_description(transcribed_text, joke_name):
    prompt = f"Generate a detailed description for the following joke:\n\nJoke Name: {joke_name}\n\nTranscribed Text:\n{transcribed_text}\n\nJoke Description:"
    messages = [
        {"role": "system", "content": "You are a helpful assistant that generates detailed joke descriptions based on transcribed text and joke names."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7
    )
    joke_description = response.choices[0].message.content.strip()
    return joke_description

def extract_joke_info(transcribed_text):
    joke_name = generate_joke_name(transcribed_text)
    joke_description = generate_joke_description(transcribed_text, joke_name)
    return joke_name, joke_description