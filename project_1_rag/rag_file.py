import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

with open("regulamin.txt", "r", encoding="utf-8") as file:
    knowledge_base = file.read()

user_query = "Jaki jest kod PIN do karty paliwowej?"

prompt = f"""
Użyj tylko i wyłącznie poniższego kontekstu, aby odpowiedzieć na pytanie użytkownika. 
Jeśli w kontekście nie ma odpowiedzi, napisz 'Nie znaleziono takich informacji w dokumentacji'.

Kontekst:
{knowledge_base}

Pytanie użytkownika:
{user_query}
"""

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(response.content[0].text)