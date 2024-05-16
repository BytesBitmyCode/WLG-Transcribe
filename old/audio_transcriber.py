import os
import whisper
import shutil
from s3_storage_handler import S3StorageHandler
from local_storage_handler import LocalStorageHandler
import numpy as np

class AudioTranscriber:
    """Main class for audio transcription."""

    def __init__(self, mode='local', **kwargs):
        self.mode = mode
        self.model = whisper.load_model("medium")
        if mode == 'local':
            self.storage_handler = LocalStorageHandler(kwargs.get('audio_directory'))
        elif mode == 's3':
            self.storage_handler = S3StorageHandler(
                kwargs.get('aws_access_key'),
                kwargs.get('aws_secret_key'),
                kwargs.get('aws_region'),
                kwargs.get('bucket_name')
            )

    def transcribe_files(self, output_directory, processed_files_log=None):
        """Transcribe audio files and save the results."""
        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)
        processed_files = set()

        # Load processed files log if it exists
        if processed_files_log and os.path.exists(processed_files_log):
            with open(processed_files_log, 'r') as file:
                processed_files = set(file.read().splitlines())

        # List folders in the storage
        folders = self.storage_handler.list_folders()
        for folder in folders:
            # List files in each folder
            for obj in self.storage_handler.list_files(folder):
                key = obj['Key']
                filename = key.split('/')[-1]
                if filename.endswith(".mp3") and key not in processed_files:
                    print(f"Transcribing {filename} from {self.mode} storage...")

                    # Get audio file and transcribe it
                    audio_segment = self.storage_handler.get_audio_file(key)
                    if audio_segment.channels > 1:
                        audio_segment = audio_segment.set_channels(1)
                    samples = np.array(audio_segment.get_array_of_samples()).astype(np.float32) / (2**15)
                    result = self.model.transcribe(samples)
                    
                    # Save transcription result
                    name_without_extension = os.path.splitext(filename)[0]
                    output_file_path = os.path.join(output_directory, f"{name_without_extension}.txt")
                    with open(output_file_path, 'w', encoding='utf-8') as file:
                        file.write(result["text"])
                    print(f"Transcription saved to {output_file_path}")

                    # Update processed files log
                    processed_files.add(key)
                    if processed_files_log:
                        with open(processed_files_log, 'a') as log_file:
                            log_file.write(key + '\n')
                else:
                    print(f"Skipping file (non-mp3 or already processed): {filename}")
