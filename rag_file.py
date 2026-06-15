import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# ==========================================
# NOWOŚĆ: Wczytywanie bazy wiedzy z pliku .txt
# ==========================================
# Funkcja open() otwiera plik, "r" oznacza "read" (czytanie), 
# a encoding="utf-8" pozwala poprawnie czytać polskie znaki (ą, ę, ć).

with open("regulamin.txt", "r", encoding="utf-8") as file:
    # Twoje zadanie: odczytaj zawartość pliku i zapisz ją do zmiennej knowledge_base
    # Podpowiedź: użyj metody file.read()
    knowledge_base = file.read()

# Pytanie użytkownika
user_query = "Jaki jest kod PIN do karty paliwowej?"

# Szablon promptu (taki sam jak poprzednio)
prompt = f"""
Użyj tylko i wyłącznie poniższego kontekstu, aby odpowiedzieć na pytanie użytkownika. 
Jeśli w kontekście nie ma odpowiedzi, napisz 'Nie znaleziono takich informacji w dokumentacji'.

Kontekst:
{knowledge_base}

Pytanie użytkownika:
{user_query}
"""

# Twoje zadanie: 
# 1. Doklej tutaj kod wywołania Claude (ten z client.messages.create), który już znasz.
# 2. Doklej print(), który wyświetli odpowiedź.
# 4. Wywołanie modelu Claude 3.5 Sonnet
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

# 5. Wyświetl wynik w terminalu za pomocą print()
print(response.content[0].text)