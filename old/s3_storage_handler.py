import os
import boto3
import io
from pydub import AudioSegment
from cloud_storage_handler import CloudStorageHandler

class S3StorageHandler(CloudStorageHandler):
    """
    Handler for AWS S3 storage operations.
    """
    
    def __init__(self, aws_access_key, aws_secret_key, aws_region, bucket_name):
        super().__init__()
        self.bucket_name = bucket_name
        os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key
        os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_key
        os.environ['AWS_DEFAULT_REGION'] = aws_region
        self.client = boto3.client('s3')

    def list_folders(self):
        """
        List folders in the S3 bucket.
        """
        folders = self.client.list_objects_v2(Bucket=self.bucket_name, Prefix='', Delimiter='/').get('CommonPrefixes', [])
        return [folder['Prefix'] for folder in folders]

    def list_files(self, folder):
        """
        List files in a specific folder in the S3 bucket.
        """
        return self.client.list_objects_v2(Bucket=self.bucket_name, Prefix=folder).get('Contents', [])

    def get_audio_file(self, key):
        """
        Get an audio file from the S3 bucket.
        """
        audio_obj = self.client.get_object(Bucket=self.bucket_name, Key=key)
        file_content = audio_obj['Body'].read()
        audio_stream = io.BytesIO(file_content)
        return AudioSegment.from_file(audio_stream, format="mp3")
