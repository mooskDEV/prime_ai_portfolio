import os
from dotenv import load_dotenv
import anthropic

# 1. Załaduj zmienne z pliku .env
load_dotenv()

# 2. Pobierz klucz z systemu za pomocą os.environ.get
api_key = os.environ.get("ANTHROPIC_API_KEY")

# 3. Inicjalizacja klienta Anthropic
client = anthropic.Anthropic(api_key=api_key)

# 4. Wywołanie modelu Claude 3.5 Sonnet
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

# 5. Wyświetlenie odpowiedzi w terminalu
print(response.content[0].text)