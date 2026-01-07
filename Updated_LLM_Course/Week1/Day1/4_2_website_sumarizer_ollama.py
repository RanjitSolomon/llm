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





# ## TELUS - Website Summary

# The TELUS website serves as a central hub for information about the company, its services, and its social impact initiatives.

# **Key areas covered include:**

# *   **Newsroom:** A source for press releases, blog posts, and information about partnerships. Currently, there are no articles listed.
# *   **Social Impact:** Highlights TELUS's commitment to building stronger communities through technology, innovation, and charitable giving. This includes initiatives focused on the "TELUS Effect" and community support.
# *   **Connectivity:** Focuses on expanding access to high-speed internet, particularly in rural and Indigenous communities, and addresses policy and regulation impacting internet availability. There's a petition related to increasing internet choice for Canadians.
# *   **Media Resources:** Provides logos and contact information for media inquiries across various departments (Consumer Solutions, Public Affairs, Social Purpose, Health, Agriculture & Consumer Goods, Business Solutions, and Indigenous Relations).
# *   **Reconciliation:** TELUS acknowledges the traditional territories on which it operates and expresses commitment to reconciliation efforts as outlined by the Truth and Reconciliation Commission.

# **Important Notes:**

# *   The website includes extensive contact information for media and sponsorship/donation requests.
# *   The website acknowledges the traditional territories it operates within and expresses a commitment to reconciliation.
