import os  
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

response = gemini.chat.completions.create(model="gemini-2.5-flash", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print(response.choices[0].message.content)



# Here's one for you:

# **Honey never spoils!**

# Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. 
# This is due to its low water content, acidic pH, and the presence of hydrogen peroxide.
