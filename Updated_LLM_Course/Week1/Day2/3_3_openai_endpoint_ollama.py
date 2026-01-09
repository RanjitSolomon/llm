from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1" 
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama") 

response = ollama.chat.completions.create(model="gemma3", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print(response.choices[0].message.content)


# Here's one:

# Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. 
# Honey's longevity can be attributed to its unique properties: it has antibacterial and antifungal properties, which prevent the growth of bacteria and other microorganisms that cause spoilage. Plus, bees actively seal any holes or cracks in their honeycombs with wax, creating an airtight container that prevents contamination. Isn't that sweet?
