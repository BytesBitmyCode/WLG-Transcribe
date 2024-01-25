import spacy
nlp = spacy.load('en_core_web_md')  # Load the medium English model

# Function to check if the questions or phrases are mentioned in the call
def check_questions_phrases(text, questions_phrases, keywords_phrases, threshold=0.85):  # Increased threshold
    doc = nlp(text)
    results = {}
    for question, keyword in zip(questions_phrases, keywords_phrases):
        keyword_doc = nlp(keyword)
        similarities = [keyword_doc.similarity(sent) for sent in doc.sents]
        max_similarity = max(similarities)

        # Debug: print detailed similarity info
        print(f"Checking: {question}")
        print(f"Max similarity: {max_similarity}")
        if max_similarity > threshold:
            results[question] = "Yes"
        else:
            results[question] = "No"
        print("-" * 60)

    return results

# Function to read text file and check specific questions/phrases
def analyze_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Define your questions and corresponding keywords or phrases
    questions_phrases = [
        "Did the caller ask to speak to an attorney?", 
        "Did the caller ask to speak to a manager?",
        # ... add all your questions here ...
        "Did the caller mention they would discharge their case?",
        "Did the caller mention they would close their case?",
        "Did the caller mention they will be changing firms?"
    ]

    keywords_phrases = [
        "speak to an attorney",
        "speak to a manager",
        # ... add the corresponding keywords/phrases for your questions ...
        "discharge their case",
        "close their case",
        "change firms"
    ]

    # Check if specific questions or phrases are mentioned
    checklist_results = check_questions_phrases(text, questions_phrases, keywords_phrases)
    
    # Display the checklist results
    for question, answer in checklist_results.items():
        print(f"{question}: {answer}")

# Path to your text file
file_path = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\transcibed txt\2022-05-03_062219__FROM_17869238043__TO_9547518552__00505693990111ecc93894fda8983495.txt"

# Analyze the text file
analyze_text_file(file_path)
