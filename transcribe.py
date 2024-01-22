import whisper

# Load the model
model = whisper.load_model("medium")

# Path to your audio file
audio_file_path = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\test.mp3"

# Transcribe the audio file
result = model.transcribe(audio_file_path)

# Print the transcribed text
print(result["text"])
