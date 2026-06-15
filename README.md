# Enterprise RAG System - Inteligentny Asystent Dokumentacji HR

Praktyczna implementacja produkcyjnego systemu klasy **RAG (Retrieval-Augmented Generation)**, zaprojektowana w celu automatyzacji procesów wewnętrznych (HR/Operations) i redukcji czasu wyszukiwania informacji w dokumentacji firmowej.

## 💡 Wartość Biznesowa (ROI)
System automatyzuje odpowiedzi na powtarzalne pytania pracowników dotyczące procedur wewnętrznych, regulaminów oraz benefitów. Wdrożenie takiego rozwiązania w organizacji pozwala na:
* **Redukcję obciążenia działu HR o 80-90%** w obszarze powtarzalnych zapytań.
* **Elimnację halucynacji AI** – model generuje odpowiedzi wyłącznie w oparciu o zweryfikowany kontekst biznesowy.
* **Skrócenie czasu wyszukiwania informacji** przez pracowników z kilkunastu minut do kilku sekund.

## 🛠️ Stack Technologiczny
* **LLM Core:** Anthropic Claude 3.5 Haiku (via Anthropic API SDK)
* **Vector Database:** ChromaDB (Lokalna wektorowa baza danych)
* **Embedding Model:** text-embedding-3 (all-MiniLM-L6-v2)
* **Environment & Security:** Python-dotenv (ochrona kluczy API przed wyciekiem)
* **Language:** Python 3.11+

## 🏗️ Architektura i Przepływ Danych (Data Flow)
1. **Ingestion:** Dokumenty tekstowe/procedury są indeksowane i transformowane na embeddingi (wektory matematyczne reprezentujące semantykę tekstu).
2. **Storage:** Wektory wraz z metadanymi są zapisywane w lokalnej kolekcji ChromaDB.
3. **Retrieval:** Zapytanie użytkownika jest wektoryzowane, a baza ChromaDB realizuje wyszukiwanie najbliższych sąsiadów (Semantic Search), dostarczając najbardziej dopasowany fragment dokumentu.
4. **Generation:** Dopasowany kontekst wraz z restrykcyjną instrukcją systemową (Prompt Engineering) trafia do modelu Claude, który generuje precyzyjną odpowiedź w języku polskim.

## 🚀 Jak uruchomić projekt lokalnie
1. Sklonuj repozytorium.
2. Utwórz środowisko wirtualne: `python -m venv .venv` i je aktywuj.
3. Zainstaluj wymagane biblioteki: `pip install -r requirements.txt` (lub ręcznie `python-dotenv anthropic chromadb`).
4. Stwórz plik `.env` i uzupełnij swój `ANTHROPIC_API_KEY`.
5. Uruchom system: `python rag_final.py`.