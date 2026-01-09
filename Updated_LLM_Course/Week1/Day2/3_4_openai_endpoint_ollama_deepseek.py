from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1" 
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")


response = ollama.chat.completions.create(model="deepseek-r1", messages=[{"role": "user", "content": "Tell me a fun fact"}])

print(response.choices[0].message.content)



# Sure! Here's a fun fact for you:

# **Venus flytraps don't automatically close on insects.** At first glance, you might think that touching the inner sides of the "teeth" triggers the trapping process. But wait, that's not entirely true. The plant actually requires two distinct touches within a short time period to respond. This mechanism is somewhat like a double-check system to prevent catching anything too small or causing waste of energy.

# Once the two touches occur, the trap snaps shut in less than a second!

#---

# How about another one? Let me know what you're curious about!
