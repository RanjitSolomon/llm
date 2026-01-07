
## Week 1     
### Day 1
###  1. Running your first LLM locally with Ollama and Open Source Models 
          
https://github.com/ed-donner/llm_engineering       
       
Install Ollama - ollama.com  
       
ollama server - runs the ollama server tcp 127.0.0.1:11434 
       
ollama pull <model_name> - downloads the model to the local cache       
       
ollama run <model_name> - runs the model locally       
ollama run gemma3:270m       
         
>>> Hi there        
Hi! How can I help you today?               
         
>>> my name is Ranjit        
That's wonderful to hear! 😊       
        
ollama run phi3     
         
>>> tell me a fun fact       
Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are
over 3,000 years old and still perfectly edible. Honey's low moisture content and acidic nature make it an
inhospitable environment for bacteria and microorganisms, allowing it to remain stable indefinitely under the
right conditions. 🍯✨        
         
If you'd like another fun fact or more information on a specific topic, feel free to ask!      
          
### 2. Spanish Tutor Demo with Open-Source Models 
         
ollama run gpt-oss      
        
>>> Hi, I'm trying to learn Spanish. I'm a total beginner. Please have a conversation with me as my Spanish tutor.
Thinking...     
We need to respond as a Spanish tutor. The user says: "Hi, I'm trying to learn Spanish. I'm a total beginner.
Please have a conversation with me as my Spanish tutor."     
     
We need to create a conversation with them, presumably in Spanish, and maybe with some English explanation. It's a
conversation, starting with greetings. We can ask the user about their goals, and maybe provide a simple
conversation in Spanish. Should we ask them what they'd like to practice? We can also provide corrections.       
         
We need to maintain the conversation style: we are a Spanish tutor. So we can begin with "¡Hola! ¿Cómo estás?"
Then ask what they'd like to focus on. Use simple Spanish, include translations. Encourage them. The user is a
beginner. Keep it simple, use short sentences, maybe ask them to respond in Spanish, but also provide corrections.        
          
We can also ask them to introduce themselves in Spanish. Then proceed.        
        
We should adopt a friendly tone. Provide explanations in English if needed. We can also incorporate common
beginner topics: numbers, colors, days, greetings. Provide practice.        
        
We can respond as a conversation. Let's respond with a Spanish conversation. But we need to be mindful of the
conversation format. It's a tutor, so the assistant should respond with Spanish, ask a question, maybe provide a
translation. And the user can respond. Since we cannot get the user's reply, we just need to generate the
assistant's first message. That can be the initial conversation starter. We can ask: "¿Cómo te llamas?" etc. Then
we can continue. So let's produce a first message in Spanish, with some English explanations. Provide a bit of
guidance. That should be enough.         
        
But also note that the user may want a conversation as tutor, so we can respond in Spanish and ask them to respond
in Spanish. Let's do that.       
        
We'll produce a Spanish conversation starter, ask for their name, maybe ask about their Spanish experience, and
provide an explanation.      
         
We'll keep it simple. We'll maybe give some common vocabulary. We'll also correct any potential mistakes. Since we
don't know what they'll say, we just give them a prompt. We'll end with a question for them to answer in Spanish.      
        
Let's produce the answer.      
...done thinking.       
       
¡Hola! 👋     
Soy tu tutor de español. Vamos a conversar de manera sencilla y práctica.       
Siéntete libre de responder en español; yo te corregiré y te daré explicaciones en inglés cuando lo necesites.      
        
---      
       
**Tutor:**         
1. **¡Hola!** ¿Cómo te llamas?       
   *Translation:* Hello! What’s your name?        
         
2. ¿Desde cuándo quieres aprender español?      
   *Translation:* How long have you wanted to learn Spanish?      
       
3. ¿Para qué te gustaría usar el español? (ej. viajes, trabajo, amigos, etc.)       
   *Translation:* What would you like to use Spanish for? (e.g., traveling, work, friends, etc.)       
        
---       
        
**Tip:**       
- **Verbos regulares en presente**:      
  - **Yo hablo** (I speak)       
  - **Tú hablas** (You speak)       
  - **Él/ella habla** (He/she speaks)       
  - **Nosotros hablamos** (We speak)      
  - **Vosotros habláis** (You all speak)      
  - **Ellos hablan** (They speak)       
       
**Ejemplo rápido**       
- *Yo hablo español.* (I speak Spanish.)         
- *Tú hablas inglés.* (You speak English.)         
        
---        
         
Cuando respondas, intenta usar una de las formas del verbo *hablar* en presente. ¡Estoy aquí para ayudarte con
cualquier duda que tengas! 🚀           
             
### 3. Setting up your LLM Development Environment with Cursor and UV      
        
### Creating a full powered Data Science Environment.      
#### 1. Step 1 - Clone the repo, install cursor, open the project        
        
#### 2. Step 2 - Install the wonderful uv. Setup your environment.     
          
#### 3. Step 3 - Create an OpenAi key 
        
#### 4. Step 4 - Create the .env file    
      
       
### 4.  Setting up your PC Development Environment with Git and Cursor 
       
git clone https://github.com/ed-donner/llm_engineering.git     
         
### 6. Installing UV and setting up your cursor development environment       
        
install uv      
       
### 7. Setting up your OpenAI API Key and environment variables 
           
https://platform.openai.com/        
           
https://platform.openai.com/settings/organization/api-keys      
         
https://platform.openai.com/settings/organization/billing/overview         
        
### 8. Installing Cursor Extensions and setting up your jupyter notebook        
        
View > Extensions > Jupyter          
        
> uv init llm_engineering               
> cd llm_engineering               
> uv venv       
> .\.venv\Scripts\activate       
               
### 9. Running Your first OpenaI API Call and System vs user prompts 
```
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
```
uv run test.py      
        
Hello! It's great to hear from you! How can I assist you today?


### 10. Fetching website contents  
```
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
```

scraper.py
``` 
from bs4 import BeautifulSoup 
import requests 

# Standard headers to fetch a website 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
} 

def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url. 
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else "No title found" 
    for irrelevant in soup.body(["script", "style", "img", "input"]):
        irrelevant.decompose() 
    text = soup.body.get_text("\n", strip=True)
    return title + "\n\n" + text  
```

### 11. System and User prompts  
```
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
```

> uv run 3_user_and_system_prompts.py  

#### Summary of Edward Donner's Website

""" 
Edward Donner's website serves as a personal and professional portfolio highlighting his interests in coding, experimentation with large language models (LLMs), and electronic music production. He is the co-founder and CTO of Nebula.io, a company that utilizes AI to aid in talent discovery, and he previously founded the AI startup untapt, which was acquired in 2021. His work at Nebula includes the development of proprietary LLMs and a patented matching model.

## News and Announcements
- **November 11, 2025**: The Unique Energy of an AI Live Event
- **September 15, 2025**: AI Engineering MLOps Track – Deploy AI to Production
- **May 28, 2025**: The AI Curriculum
- **May 18, 2025**: AI Leadership Track – Gen AI and Agentic AI for Business Leaders

The site encourages visitors to connect with him through various platforms including LinkedIn, Twitter, and Facebook. 
""" 
      
      
Models: Open-Source, Closed-Source, Multi-Modal, Architecture, Selecting        
      
Tools : HuggingFace, LangChain, Gradio, Weights & Biases, Modal        
       
Techniques: APIs, Multi-shot prompting, RAG, Fine-tuning, Agentization       
          
Intermediate level Python
"""
yield from set(book.get("author") for book in books if book.get("author"))  
"""   
         
### 12. Website Summarizer - OpenAI 
```
import os 
from dotenv import load_dotenv
from openai import OpenAI 
from scraper import fetch_website_contents

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai = OpenAI(api_key=api_key)

system_prompt = """ 
You are an assistant that analyzes the contents of a website, 
and provides a short summary, ignoring text that might be navigation related. 
"""

user_prompt_prefix = """
Here are the contents of a website. 
Provide a short summary of this webiste in markdown format.  
If it includes news or announcements, then summarize these too.

"""

def messages_for(website): 
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

def summarize_website(website): 
    website = fetch_website_contents(website)
    messages = messages_for(website)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

if __name__ == "__main__": 
    website = "https://www.telus.com/en/about/newsroom"
    summary = summarize_website(website)
    print(summary)
```
"""
TELUS Newsroom Summary     
        
The TELUS Newsroom serves as the primary source for the latest news and updates related to TELUS, including press releases, blog stories, and partnership information. It emphasizes the company's commitment to community strengthening through technology, innovation, and social impact initiatives.
       
Key Features:        
         
 - **News Releases**: Access to the most recent updates about TELUS’s developments, innovations, and other key announcements.         
 - **Public Policy**: Insights into how government policies impact internet access and network quality in Canada.       
 - **Innovation and Investment**: Information on TELUS’s network investments aimed at enhancing economic, social, and environmental benefits.     
 - **Rural and Indigenous Connectivity**: Efforts to provide high-speed internet access to rural areas and Indigenous communities.       
           
Social Impact:       
TELUS is focused on driving social change through various initiatives, reinforcing its dedication to building healthier communities.       
         
For media resources, contact information, and opportunities for engagement, visit the newsroom section of the TELUS website.        
"""
        
### 13. Website Summarizer - Ollama        
       
```
from ollama import ChatResponse
from ollama import chat
from scraper import fetch_website_contents

system_prompt = """ 
You are an assistant that analyzes the contents of a website, 
and provides a short summary, ignoring text that might be navigation related. 
"""

user_prompt_prefix = """
Here are the contents of a website. 
Provide a short summary of this webiste in markdown format.  
If it includes news or announcements, then summarize these too.

"""

def messages_for(website): 
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

def summarize_website(website): 
    website = fetch_website_contents(website)
    messages = messages_for(website)
    response: ChatResponse = chat(model="gemma3:12b", messages=messages)
    return response.message.content

if __name__ == "__main__": 
    website = 'https://finance.yahoo.com/quote/T.TO/'
    #website = "https://www.telus.com/en/about/newsroom"
    summary = summarize_website(website)
    print(summary)
```
""" 
TELUS - Website Summary       
        
The TELUS website serves as a central hub for information about the company, its services, and its social impact initiatives.        
        
**Key areas covered include:**          
       
**Newsroom:** A source for press releases, blog posts, and information about partnerships. Currently, there are no articles listed.        
**Social Impact:** Highlights TELUS's commitment to building stronger communities through technology, innovation, and charitable giving. This includes initiatives focused on the "TELUS Effect" and community support.           
**Connectivity:** Focuses on expanding access to high-speed internet, particularly in rural and Indigenous communities, and addresses policy and regulation impacting internet availability. There's a petition related to increasing internet choice for Canadians.    
**Media Resources:** Provides logos and contact information for media inquiries across various departments (Consumer Solutions, Public Affairs, Social Purpose, Health, Agriculture & Consumer Goods, Business Solutions, and Indigenous Relations).       
**Reconciliation:** TELUS acknowledges the traditional territories on which it operates and expresses commitment to reconciliation efforts as outlined by the Truth and Reconciliation Commission.            
          
**Important Notes:**        
         
The website includes extensive contact information for media and sponsorship/donation requests.          
The website acknowledges the traditional territories it operates within and expresses a commitment to reconciliation.          
          
""" 
         
### 14. Website Summarizer - Ollama playwright 
```
from ollama import ChatResponse
from ollama import chat
from playwright.sync_api import sync_playwright 
from bs4 import BeautifulSoup 
from IPython.display import Markdown, display  

system_prompt = """ 
You are an assistant that analyzes the contents of a website, 
and provides a short summary, ignoring text that might be navigation related. 
"""

user_prompt = """
Here are the contents of a website. 
Provide a short summary of this webiste in markdown format.  
If it includes news or announcements, then summarize these too.

""" 

def messages_for(website): 
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + website}
    ]

def scrape_website(website): 
    with sync_playwright() as p: 
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(website)
        content = page.content()
        browser.close()
    return content

def summarize_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    summarize_text = soup.get_text(separator=' ', strip=True)
    messages = messages_for(summarize_text)
    response: ChatResponse = chat(model="gemma3:12b", messages=messages)
    return response.message.content

def save_markdown(markdown_content, filename): 
    with open(filename, 'w') as f: 
        f.write(markdown_content)

def main(): 
    #website = "https://www.telus.com/en/about/newsroom"
    website = "https://finance.yahoo.com/quote/T.TO/"
    html_content = scrape_website(website)
    markdown_content = summarize_content(html_content)
    #save_markdown(markdown_content, "telus_newsroom.md")
    save_markdown(markdown_content, "telus_yahoo.md")
    #display(Markdown(markdown_content))

if __name__ == "__main__": 
    main()
```
       
                 
         
         



"bs4>=0.0.2",       
"ipython>=9.8.0",       
"ollama>=0.6.1",       
"openai>=2.14.0",       
"playwright>=1.57.0",       
"python-dotenv>=1.2.1",        
"requests>=2.32.5",      





   
   
         
             
































