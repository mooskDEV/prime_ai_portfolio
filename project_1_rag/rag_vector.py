import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="firmowa_wiedza")

documents = [
    "Polityka pracy zdalnej: Każdy pracownik ma prawo do dofinansowania biurka do kwoty 800 PLN.",
    "Zasady korzystania z aut służbowych: Koszty paliwa są pokrywane z karty (PIN: 1234).",
    "Benefity: Firma oferuje darmowe lekcje języka angielskiego w każdy czwartek o 15:00."
]

ids = ["doc_biurko", "doc_auto", "doc_angielski"]

collection.add(
    documents=documents,
    ids=ids
)

print("🚀 Baza wektorowa została pomyślnie utworzona i zasilona danymi!")

query = "Chcę się uczyć języków obcych, co oferuje firma?"

results = collection.query(
    query_texts=[query],
    n_results=1
)

print("\n🔍 Pytanie użytkownika:", query)
print("📄 Najbardziej pasujący dokument z bazy:", results['documents'][0][0])