import os 
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

message = "Hello, GPT! This is my first ever message to you. Hi! "

messages = [{"role": "user", "content": message}]

openai = OpenAI(api_key=api_key)

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)


# uv run 1_simple_openai.py 
# Hello! Welcome! I'm glad to hear from you. How can I assist you today?  

