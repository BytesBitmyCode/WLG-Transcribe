import os
import shutil
import whisper
from directory_manager import DirectoryManager  # Assuming DirectoryManager is in a file named directory_manager.py

class LocalAudioTranscriber:
    def __init__(self, model_name="medium"):
        self.model = whisper.load_model(model_name)
        print("Model loaded successfully.")

    def transcribe_file(self, audio_file_path, output_directory, completed_audio_directory):
        try:
            # Transcribe the audio file
            result = self.model.transcribe(audio_file_path)
            
            # Extract the base name of the audio file (without extension)
            name_without_extension = os.path.splitext(os.path.basename(audio_file_path))[0]
            
            # Construct the output file path with the same base name as the audio file
            output_file_path = os.path.join(output_directory, f"{name_without_extension}_transcript.txt")
            
            # Write the transcribed text to a file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(result["text"])
            
            print(f"Transcription saved to {output_file_path}")

            # Move the transcribed audio file to the completed_audio_directory
            completed_audio_file_path = os.path.join(completed_audio_directory, os.path.basename(audio_file_path))
            shutil.move(audio_file_path, completed_audio_file_path)
            print(f"Moved audio file to {completed_audio_file_path}")

            return output_file_path
        except Exception as e:
            print(f"An error occurred while processing the file {audio_file_path}: {e}")

    def transcribe_directory(self, audio_directory, output_directory, completed_audio_directory):
        try:
            os.makedirs(output_directory, exist_ok=True)  # Ensure output directory exists
            os.makedirs(completed_audio_directory, exist_ok=True)  # Ensure completed audio directory exists
            
            # Loop through each file in the audio_directory
            for filename in os.listdir(audio_directory):
                if filename.lower().endswith(".mp3"):  # Check if the file is an MP3
                    audio_file_path = os.path.join(audio_directory, filename)
                    print(f"Transcribing {audio_file_path} ...")
                    
                    # Transcribe the audio file using the transcribe_file method
                    self.transcribe_file(audio_file_path, output_directory, completed_audio_directory)
        except Exception as e:
            print(f"An error occurred in the directory processing: {e}")

# Create an instance of the directory manager to get the directories and the single file path
dir_manager = DirectoryManager()
audio_directory, output_directory, completed_audio_directory, single_audio_file = dir_manager.get_directories()

# Create an instance of the transcriber
transcriber = LocalAudioTranscriber()

# Decide which function to call based on whether a single file path was provided
if single_audio_file:
    transcriber.transcribe_file(single_audio_file, output_directory, completed_audio_directory)
else:
    transcriber.transcribe_directory(audio_directory, output_directory, completed_audio_directory)
