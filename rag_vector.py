import chromadb

# 1. Inicjalizacja bazy danych ChromaDB
# Tworzymy bazę, która tymczasowo działa w pamięci RAM komputera
chroma_client = chromadb.Client()

# 2. Tworzymy tzw. "Kolekcję" (to odpowiednik tabeli w bazie danych)
# Nazwijmy ją "firmowa_wiedza"
collection = chroma_client.create_collection(name="firmowa_wiedza")

# 3. Przygotowujemy dokumenty biznesowe
# Wyobraź sobie, że to są 3 różne paragrafy wyciągnięte z wielkiego PDF-a
documents = [
    "Polityka pracy zdalnej: Każdy pracownik ma prawo do dofinansowania biurka do kwoty 800 PLN.",
    "Zasady korzystania z aut służbowych: Koszty paliwa są pokrywane z karty (PIN: 1234).",
    "Benefity: Firma oferuje darmowe lekcje języka angielskiego w każdy czwartek o 15:00."
]

# Każdy dokument musi mieć swój unikalny identyfikator (ID), żeby baza wiedziała co jest czym
ids = ["doc_biurko", "doc_auto", "doc_angielski"]

# 4. Wrzucamy dane do bazy wektorowej
# ChromaDB pod maską automatycznie zamieni te teksty na liczby (embeddingi)
collection.add(
    documents=documents,
    ids=ids
)

print("🚀 Baza wektorowa została pomyślnie utworzona i zasilona danymi!")

# =========================================================================
# 5. TEST WYSZUKIWANIA (Retrieval)
# =========================================================================

# Zadajemy pytanie, które NIE ZAWIERA idealnych słów kluczowych (np. nie ma słowa 'angielskiego')
query = "Chcę się uczyć języków obcych, co oferuje firma?"

# Przeszukujemy bazę. Parametr n_results=1 oznacza: "daj mi 1 najlepszy dopasowany fragment"
results = collection.query(
    query_texts=[query],
    n_results=1
)

# Wyświetlamy to, co znalazła nasza inteligentna baza danych
print("\n🔍 Pytanie użytkownika:", query)
print("📄 Najbardziej pasujący dokument z bazy:", results['documents'][0][0])