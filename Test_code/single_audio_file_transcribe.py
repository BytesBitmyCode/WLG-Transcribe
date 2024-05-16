import os
import whisper

def transcribe_audio_file(audio_file_path, output_directory):
    # Load the model (consider doing this outside the loop if performance is a concern)
    model = whisper.load_model("medium")
            
    # Transcribe the audio file
    result = model.transcribe(audio_file_path)
    
    # Extract the base name of the audio file (without extension)
    name_without_extension = os.path.splitext(os.path.basename(audio_file_path))[0]
    
    # Construct the output file path with the same base name as the audio file
    output_file_path = os.path.join(output_directory, f"{name_without_extension}_transcript.txt")
    
    # Write the transcribed text to a file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(result["text"])
    
    print(f"Transcription saved to {output_file_path}")

# File path and output directory
audio_file_path = r"C:\Users\Michael Barreau\Downloads\mp3\test.mp3"
output_directory = r"C:\Users\Michael Barreau\Downloads\mp3"

# Transcribe the audio file
transcribe_audio_file(audio_file_path, output_directory)
