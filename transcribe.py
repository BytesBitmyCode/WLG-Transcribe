import os
import whisper

# Load the model
model = whisper.load_model("medium")

# Path to your audio file
audio_file_path = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\test.mp3"

# Transcribe the audio file
result = model.transcribe(audio_file_path)

# Extract the base name of the audio file (without extension)
base_name = os.path.basename(audio_file_path)
# Remove the file extension (.mp3) to get the name
name_without_extension = os.path.splitext(base_name)[0]

# Construct the output file path with the same base name as the audio file
output_directory = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\transcibed txt"
output_file_path = os.path.join(output_directory, f"{name_without_extension}_transcript.txt")

# Write the transcribed text to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(result["text"])

print(f"Transcription saved to {output_file_path}")
