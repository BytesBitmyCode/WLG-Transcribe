from audio_transcriber import AudioTranscriber
from local_storage_handler import LocalStorageHandler
from directory_manager import select_directory

def main():
    # Prompt the user for the mode and relevant information
    mode = input("Choose mode (local OR s3 For AWS S3): ").strip().lower()
    
    if mode == 'local':
        print("Select audio directory")
        audio_directory = select_directory()
        print(f"Audio directory selected: {audio_directory}")

        print("Select output directory")
        output_directory = select_directory()
        print(f"Output directory selected: {output_directory}")

        print("Select completed audio directory")
        completed_audio_directory = select_directory()
        print(f"Completed audio directory selected: {completed_audio_directory}")

        storage_handler = LocalStorageHandler(audio_directory=audio_directory)
        transcriber = AudioTranscriber(mode='local', audio_directory=audio_directory)
        transcriber.transcribe_files(output_directory)
        
    elif mode == 's3':
        aws_access_key = input("Enter AWS Access Key: ").strip()
        aws_secret_key = input("Enter AWS Secret Key: ").strip()
        aws_region = input("Enter AWS Region: ").strip()
        bucket_name = input("Enter S3 Bucket Name: ").strip()

        print("Select output directory")
        output_directory = select_directory()
        print(f"Output directory selected: {output_directory}")

        processed_files_log = input("Enter the processed files log path: ").strip()
        transcriber = AudioTranscriber(
            mode='s3',
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            aws_region=aws_region,
            bucket_name=bucket_name
        )
        transcriber.transcribe_files(output_directory, processed_files_log)

if __name__ == "__main__":
    main()
