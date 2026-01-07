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
