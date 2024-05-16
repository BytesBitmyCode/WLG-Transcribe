import os
import shutil
import whisper

# Initialize the variables
audio_directory = None
output_directory = None
completed_audio_directory = None

def load_whisper_model(model_size="medium"):
    """Load the Whisper model."""
    return whisper.load_model(model_size)

def ensure_directories(*directories):
    """Ensure the specified directories exist."""
    for directory in directories:
        if directory:
            os.makedirs(directory, exist_ok=True)

def transcribe_audio_file(model, audio_file_path, output_file_path):
    """Transcribe a single audio file and save the transcription to a text file."""
    result = model.transcribe(audio_file_path)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(result["text"])

def move_completed_file(src_path, dest_path):
    """Move a completed audio file to the specified directory."""
    shutil.move(src_path, dest_path)

def transcribe_audio_directory(audio_directory, output_directory, completed_audio_directory, model_size="medium"):
    """Transcribe all audio files in a directory and save the transcriptions."""
    if not audio_directory or not output_directory or not completed_audio_directory:
        raise ValueError("All directories must be specified.")
    
    model = load_whisper_model(model_size)
    ensure_directories(output_directory, completed_audio_directory)
    
    for filename in os.listdir(audio_directory):
        if filename.endswith(".mp3"):
            audio_file_path = os.path.join(audio_directory, filename)
            print(f"Transcribing {audio_file_path} ...")
            
            name_without_extension = os.path.splitext(filename)[0]
            output_file_path = os.path.join(output_directory, f"{name_without_extension}_transcript.txt")
            
            transcribe_audio_file(model, audio_file_path, output_file_path)
            print(f"Transcription saved to {output_file_path}")
            
            completed_audio_file_path = os.path.join(completed_audio_directory, filename)
            move_completed_file(audio_file_path, completed_audio_file_path)
            print(f"Moved audio file to {completed_audio_file_path}")

