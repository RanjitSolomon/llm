# Create OpenAI client
import os  
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
openai = OpenAI()

response = openai.chat.completions.create(model="gpt-5-nano", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print(response.choices[0].message.content)


# Fun fact: Honey never spoils—archaeologists have found edible honey in ancient Egyptian tombs that’s thousands of years old.

