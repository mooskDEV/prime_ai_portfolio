import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {
            "role": "user", 
            "content": "Cześć! Jesteś moim asystentem AI w projekcie dla Prime Engineering. Napisz w jednym zdaniu, czym się zajmujesz."
        }
    ]
)

print(response.content[0].text)