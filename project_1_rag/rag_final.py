import os
from dotenv import load_dotenv
import anthropic
import chromadb

load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="firmowa_wiedza_final")

documents = [
    "Polityka pracy zdalnej: Każdy pracownik ma prawo do dofinansowania biurka do kwoty 800 PLN.",
    "Zasady korzystania z aut służbowych: Koszty paliwa są pokrywane z karty (PIN: 1234).",
    "Benefity: Firma oferuje darmowe lekcje języka angielskiego w każdy czwartek o 15:00."
]
ids = ["doc_biurko", "doc_auto", "doc_angielski"]
collection.add(documents=documents, ids=ids)

user_query = "Potrzebuję kupić biurko do pracy zdalnej. Czy firma mi w tym pomoże?"

results = collection.query(query_texts=[user_query], n_results=1)
context = results['documents'][0][0]

prompt = f"""
Zawsze odpowiadaj wyłącznie w języku polskim.
Użyj tylko i wyłącznie poniższego kontekstu, aby odpowiedzieć na pytanie użytkownika. 
Jeśli w kontekście nie ma odpowiedzi, napisz 'Nie znaleziono takich informacji w dokumentacji'.

Kontekst:
{context}

Pytanie użytkownika:
{user_query}
"""

try:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
)
    print("\n🤖 Odpowiedź Asystenta AI:")
    print(response.content[0].text)

except Exception as e:
    print(f"\n❌ Wystąpił błąd podczas połączenia z AI: {e}")
    print("Proszę spróbować ponownie później.")