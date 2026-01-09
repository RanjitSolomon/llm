import os  
from dotenv import load_dotenv
import openai
import requests

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY") 
if not api_key:
    print("OPENAI_API_KEY not found in environment variables")
elif not api_key.startswith("sk-proj-"):
    print("OPENAI_API_KEY is not a valid API key")
else:
    print("OPENAI_API_KEY is valid")    
 
# import requests 
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Tell me a fun fact"}
    ]
}

# Endpoint 
response = requests.post(
    "https://api.openai.com/v1/chat/completions", 
    headers=headers, 
    json=payload
    )

print(response.json())

# {'id': 'chatcmpl-CvOjcQ5J9TT3gnX1j2q2FQbvEmmft', 
#  'object': 'chat.completion', 'created': 1767795812, 
#  'model': 'gpt-4o-mini-2024-07-18', 
#  'choices': [{'index': 0,
#       'message': {'role': 'assistant',
#       'content': "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible! Honey's low moisture content and acidity make it an inhospitable environment for bacteria and microorganisms, allowing it to last indefinitely.",
#       'refusal': None,
#       'annotations': []},
#       'logprobs': None,
#       'finish_reason': 'stop'}], 
#  'usage': {'prompt_tokens': 12,
#       'completion_tokens': 60,
#       'total_tokens': 72,
#       'prompt_tokens_details': {'cached_tokens': 0,
#           'audio_tokens': 0},
#       'completion_tokens_details': {'reasoning_tokens': 0,
#           'audio_tokens': 0,
#           'accepted_prediction_tokens': 0,
#           'rejected_prediction_tokens': 0}},
#    'service_tier': 'default',
#    'system_fingerprint': 'fp_29330a9688'}


print(response.json()["choices"][0]["message"]["content"])

# Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible! Honey's low moisture content and acidic nature make it an inhospitable environment for bacteria and microorganisms, allowing it to last indefinitely when stored properly.



