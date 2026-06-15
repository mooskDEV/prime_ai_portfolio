import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# 1. Nasza mini-baza wiedzy (symulacja dokumentu HR)
knowledge_base = (
    "Polityka pracy zdalnej w firmie XYZ: Każdy pracownik ma prawo do dofinansowania "
    "biurka ergonomicznego do kwoty 800 PLN raz na dwa lata. Wnioski należy składać "
    "do działu HR do 10. dnia każdego miesiąca."
)

# 2. Pytanie użytkownika
user_query = "Ile wynosi budżet na pizzę podczas piątkowych integracji?"

# 3. Stworzenie promptu systemowego za pomocą f-stringa.
prompt = f"""
Użyj tylko i wyłącznie poniższego kontekstu, aby odpowiedzieć na pytanie użytkownika. 
Jeśli w kontekście nie ma odpowiedzi, napisz 'Nie znaleziono takich informacji w dokumentacji'.

Kontekst:
{knowledge_base}

Pytanie użytkownika:
{user_query}
"""

# 4. Wywołanie modelu Claude 3.5 Sonnet
response = client.messages.create(
    model="claude-haiku-4-5-lastest",
    max_tokens=1024,
    messages=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

# 5. Wyświetl wynik w terminalu za pomocą print()
print(response.content[0].text)