import os
import whisper

def transcribe_audio(audio_directory, output_directory):
    # Load the model (consider doing this outside the loop if performance is a concern)
    model = whisper.load_model("medium")
    
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Loop through each file in the audio_directory
    for filename in os.listdir(audio_directory):
        if filename.endswith(".mp3"):  # Check if the file is an MP3
            audio_file_path = os.path.join(audio_directory, filename)
            print(f"Transcribing {audio_file_path}...")
            
            # Transcribe the audio file
            result = model.transcribe(audio_file_path)
            
            # Extract the base name of the audio file (without extension)
            name_without_extension = os.path.splitext(filename)[0]
            
            # Construct the output file path with the same base name as the audio file
            output_file_path = os.path.join(output_directory, f"{name_without_extension}_transcript.txt")
            
            # Write the transcribed text to a file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(result["text"])
            
            print(f"Transcription saved to {output_file_path}")

# Directories
audio_directory = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files"
output_directory = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\transcibed txt"

# Transcribe all audio files in the directory
transcribe_audio(audio_directory, output_directory)
