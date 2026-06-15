import os
from dotenv import load_dotenv
import anthropic
import chromadb

# 1. Inicjalizacja Claude i bazy ChromaDB
load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="firmowa_wiedza_final")

# 2. Zasilamy bazę dokumentami
documents = [
    "Polityka pracy zdalnej: Każdy pracownik ma prawo do dofinansowania biurka do kwoty 800 PLN.",
    "Zasady korzystania z aut służbowych: Koszty paliwa są pokrywane z karty (PIN: 1234).",
    "Benefity: Firma oferuje darmowe lekcje języka angielskiego w każdy czwartek o 15:00."
]
ids = ["doc_biurko", "doc_auto", "doc_angielski"]
collection.add(documents=documents, ids=ids)

# 3. Dynamiczne pytanie użytkownika (Możesz je zmieniać!)
user_query = "Potrzebuję zatankować auto służbowe, jak mam za to zapłacić?"

# 4. RETRIEVAL: Szukamy 1 najlepszego dokumentu w bazie wektorowej
results = collection.query(query_texts=[user_query], n_results=1)
context = results['documents'][0][0]  # Wyciągamy czysty tekst dopasowanego dokumentu

# 5. Budujemy prompt z dynamicznym kontekstem
prompt = f"""
Zawsze odpowiadaj wyłącznie w języku polskim.
Użyj tylko i wyłącznie poniższego kontekstu, aby odpowiedzieć na pytanie użytkownika. 
Jeśli w kontekście nie ma odpowiedzi, napisz 'Nie znaleziono takich informacji w dokumentacji'.

Kontekst:
{context}

Pytanie użytkownika:
{user_query}
"""

# 6. GENERATION: Wysyłamy gotowy zestaw do Claude
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt}]
)

# 7. Wyświetlamy ostateczną odpowiedź bota
print("\n🤖 Odpowiedź Asystenta AI:")
print(response.content[0].text)