import os 
from dotenv import load_dotenv
from openai import OpenAI 
from scraper import fetch_website_contents

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

message = "Hello, GPT! This is my first ever message to you. Hi! "

messages = [{"role": "user", "content": message}]

message = "Hello, GPT! This is my first ever message to you. Hi! "

messages = [{"role": "user", "content": message}]

openai = OpenAI(api_key=api_key)

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)

ed = fetch_website_contents("https://edwarddonner.com")
print(ed)



# uv run 2_fetch_contents.py 
"""
Hello! Welcome! It’s great to hear from you. How can I assist you today?
Home - Edward Donner

Home
Connect Four
Outsmart
An arena that pits LLMs against each other in a battle of diplomacy and deviousness
About
Posts
Well, hi there.
I’m Ed. I like writing code and experimenting with LLMs, and hopefully you’re here because you do too. I also enjoy DJing (but I’m badly out of practice), amateur electronic music production (
very
amateur) and losing myself in
Hacker News
, nodding my head sagely to things I only half understand.
I’m the co-founder and CTO of
Nebula.io
. We’re applying AI to a field where it can make a massive, positive impact: helping people discover their potential and pursue their reason for being. Recruiters use our product today to source, understand, engage and manage talent. I’m previously the founder and CEO of AI startup untapt,
acquired in 2021
.
We work with groundbreaking, proprietary LLMs verticalized for talent, we’ve
patented
our matching model, and our award-winning platform has happy customers and tons of press coverage.
Connect
with me for more!
November 11, 2025
The Unique Energy of an AI Live Event
September 15, 2025
AI Engineering MLOps Track – Deploy AI to Production
May 28, 2025
The AI Curriculum
May 18, 2025
AI Leadership Track – Gen AI and Agentic AI for Business Leaders
Navigation
Home
Connect Four
Outsmart
An arena that pits LLMs against each other in a battle of diplomacy and deviousness
About
Posts
Get in touch
ed [at] edwarddonner [dot] com
www.edwarddonner.com
Follow me
LinkedIn
Twitter
Facebook
Subscribe to newsletter
Type your email…
"""