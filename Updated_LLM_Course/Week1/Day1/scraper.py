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

