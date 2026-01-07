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






# # TELUS Newsroom Summary

# The TELUS Newsroom serves as the primary source for the latest news and updates related to TELUS, including press releases, blog stories, and partnership information. It emphasizes the company's commitment to community strengthening through technology, innovation, and social impact initiatives.

# ## Key Features:

# - **News Releases**: Access to the most recent updates about TELUS’s developments, innovations, and other key announcements.
# - **Public Policy**: Insights into how government policies impact internet access and network quality in Canada.
# - **Innovation and Investment**: Information on TELUS’s network investments aimed at enhancing economic, social, and environmental benefits.
# - **Rural and Indigenous Connectivity**: Efforts to provide high-speed internet access to rural areas and Indigenous communities.

# ## Social Impact:
# TELUS is focused on driving social change through various initiatives, reinforcing its dedication to building healthier communities.

# For media resources, contact information, and opportunities for engagement, visit the newsroom section of the TELUS website.