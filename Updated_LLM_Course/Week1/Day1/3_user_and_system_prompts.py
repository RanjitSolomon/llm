import os 
from dotenv import load_dotenv
from openai import OpenAI 
from scraper import fetch_website_contents

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai = OpenAI(api_key=api_key)

website = fetch_website_contents("https://edwarddonner.com")

system_prompt = """ 
You are an assistant that analyzes the contents of a website, 
and provides a short summary, ignoring text that might be navigation related. 
"""
# You are a snarky assistant ...
# Reqpond in markdown format. 

user_prompt_prefix = """
Here are the contents of a website. 
Provide a short summary of this webiste in markdown format.  
If it includes news or announcements, then summarize these too. 
    
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_prefix + website  }
]

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)


