from transformers import pipeline
import nltk

# Download the Punkt tokenizer for sentence splitting
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Function to split text into chunks
def chunk_text(text, max_length):
    """
    Splits the text into chunks, each with a maximum length of max_length.
    Tries to split on full stops to ensure complete sentences in each chunk.
    """
    sentences = sent_tokenize(text)
    current_chunk = ""
    chunks = []

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + " "
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

# Function to perform sentiment analysis
def analyze_sentiment(text_chunks):
    classifier = pipeline('sentiment-analysis')
    results = []
    for chunk in text_chunks:
        result = classifier(chunk)
        results.extend(result)
    return results

# Function to read text file, chunk text, and analyze sentiment
def analyze_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Chunk the text
    text_chunks = chunk_text(text, max_length=500)  # Adjust the max_length as needed
    
    # Perform sentiment analysis on each chunk
    sentiment_results = analyze_sentiment(text_chunks)
    
    # Display the results
    for result in sentiment_results:
        print(f"Sentiment: {result['label']}, Score: {result['score']:.2f}")
        print("-" * 60)

# Path to your text file
file_path = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\transcibed txt\2022-05-03_062219__FROM_17869238043__TO_9547518552__00505693990111ecc93894fda8983495.txt"

# Analyze the text file
analyze_text_file(file_path)
