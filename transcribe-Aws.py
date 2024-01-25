import os
import whisper
import boto3
from pydub import AudioSegment
import numpy as np
import io

# Set environment variables within the script
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAY6FBQKYEWXI2A6O4'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'  # US East (N. Virginia)

# Initialize a boto3 S3 client
s3 = boto3.client('s3')

# Set your S3 Bucket
bucket_name = 'wardlawphonerecordings'  # Replace with your actual bucket name

def transcribe_audio(output_directory, processed_files_log):
    # Load the model (consider doing this outside the loop if performance is a concern)
    model = whisper.load_model("medium")
    
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Read the list of processed files (if the file exists)
    if os.path.exists(processed_files_log):
        with open(processed_files_log, 'r') as file:
            processed_files = set(file.read().splitlines())
    else:
        processed_files = set()
    
    # List folders in the S3 bucket (assuming folder names are dates)
    folders = s3.list_objects_v2(Bucket=bucket_name, Prefix='', Delimiter='/').get('CommonPrefixes', [])
    for folder in folders:
        audio_directory = folder['Prefix']
        print(f"Processing folder: {audio_directory}")
        
        # Loop through each file in the S3 bucket folder
        for obj in s3.list_objects_v2(Bucket=bucket_name, Prefix=audio_directory)['Contents']:
            key = obj['Key']
            filename = key.split('/')[-1]
            
            if filename.endswith(".mp3") and key not in processed_files:  # Check if the file is an MP3 and not processed
                print(f"Transcribing {filename} from S3 bucket...")
                
                # Get the audio file object from S3
                audio_obj = s3.get_object(Bucket=bucket_name, Key=key)
                # Get the file content
                file_content = audio_obj['Body'].read()
                # Convert file content to a byte stream
                audio_stream = io.BytesIO(file_content)
                
                # Use PyDub to read the audio file
                audio_segment = AudioSegment.from_file(audio_stream, format="mp3")
                
                # Mix stereo to mono if necessary
                if audio_segment.channels > 1:
                    audio_segment = audio_segment.set_channels(1)
                
                samples = np.array(audio_segment.get_array_of_samples()).astype(np.float32)
                
                # Normalize the samples to the range expected by the model (if needed)
                samples = samples / (2**15)  # Assuming 16-bit audio
                
                # Transcribe the audio file
                result = model.transcribe(samples)
                
                # Extract the base name of the audio file (without extension)
                name_without_extension = os.path.splitext(filename)[0]
                
                # Construct the output file path with the same base name as the audio file
                output_file_path = os.path.join(output_directory, f"{name_without_extension}.txt")
                
                # Write the transcribed text to a file
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.write(result["text"])
                
                print(f"Transcription saved to {output_file_path}")
                
                # Add the key to the set of processed files
                processed_files.add(key)
                
                # Update the log file
                with open(processed_files_log, 'a') as log_file:
                    log_file.write(key + '\n')
            else:
                print(f"Skipping file (non-mp3 or already processed): {filename}")

# Output directory and processed files log
output_directory = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files\transcibed txt"
processed_files_log = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\processed_files.txt"

# Transcribe all audio files in the S3 bucket folders
transcribe_audio(output_directory, processed_files_log)