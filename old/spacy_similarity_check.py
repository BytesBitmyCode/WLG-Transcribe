import spacy
from langdetect import detect

# Load English and Spanish language models
en_nlp = spacy.load('en_core_web_md')
es_nlp = spacy.load('es_core_news_md')

# Function to check if the questions or phrases are mentioned in the call (English)
def check_questions_phrases_english(text, questions_phrases, keywords_phrases, threshold=0.8):
    doc = en_nlp(text)
    results = {}
    for question, keyword in zip(questions_phrases, keywords_phrases):
        keyword_doc = en_nlp(keyword)
        similarities = [keyword_doc.similarity(sent) for sent in doc.sents]
        max_similarity = max(similarities)

        # Debug: print detailed similarity info
        print(f"Checking (English): {question}")
        print(f"Max similarity: {max_similarity}")
        if max_similarity > threshold:
            results[question] = "Yes"
        else:
            results[question] = "No"
        print("-" * 60)

    return results

# Function to check if the questions or phrases are mentioned in the call (Spanish)
def check_questions_phrases_spanish(text, questions_phrases, keywords_phrases, threshold=0.8):
    doc = es_nlp(text)
    results = {}
    for question, keyword in zip(questions_phrases, keywords_phrases):
        keyword_doc = es_nlp(keyword)
        similarities = [keyword_doc.similarity(sent) for sent in doc.sents]
        max_similarity = max(similarities)

        # Debug: print detailed similarity info
        print(f"Checking (Spanish): {question}")
        print(f"Max similarity: {max_similarity}")
        if max_similarity > threshold:
            results[question] = "Yes"
        else:
            results[question] = "No"
        print("-" * 60)

    return results

# Function to determine the language of the text
def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return None

# Function to analyze text based on detected language
def analyze_text(text):
    detected_language = detect_language(text)
    results = {}

    if detected_language == 'en':
        questions_phrases = [
            "Did the caller ask to speak to an attorney?", 
            "Did the caller ask to speak to a manager?",
            "Did the caller mention they would discharge their case?",
            "Did the caller mention they would close their case?",
            "Did the caller mention they will be changing firms?"
        ]

        keywords_phrases = [
            "speak to an attorney",
            "speak to a manager",
            "discharge case",
            "close case",
            "change firm"
        ]

        results = check_questions_phrases_english(text, questions_phrases, keywords_phrases)
    elif detected_language == 'es':
        questions_phrases = [
            "¿El llamante solicitó hablar con un abogado?",
            "¿El llamante solicitó hablar con un gerente?",
            # Add all your questions here
            "¿El llamante mencionó que daría de baja su caso?",
            "¿El llamante mencionó que cerraría su caso?",
            "¿El llamante mencionó que cambiaría de empresa?"
        ]

        keywords_phrases = [
            "hablar con un abogado",
            "hablar con un gerente",
            # Add the corresponding keywords/phrases for your questions in Spanish
            "dar de baja su caso",
            "cerrar su caso",
            "cambiar de empresa"
        ]

        results = check_questions_phrases_spanish(text, questions_phrases, keywords_phrases)
    else:
        print("Language not supported")

    return results

# Path to your text file
file_path = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\transcibed txt\2022-05-03_062219__FROM_17869238043__TO_9547518552__00505693990111ecc93894fda8983495.txt"

# Read the text from the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Analyze the text based on detected language
results = analyze_text(text)

# Print the results
print("Results:")
for question, answer in results.items():
    print(f"{question}: {answer}")
