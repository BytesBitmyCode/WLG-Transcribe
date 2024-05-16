import os

class LocalStorageHandler:
    """
    Handler for local directory operations.
    """

    def __init__(self, audio_directory):
        self.audio_directory = audio_directory

    def list_files(self):
        """
        List MP3 files in the local audio directory.
        """
        return [f for f in os.listdir(self.audio_directory) if f.endswith(".mp3")]

    def get_audio_file(self, filename):
        """
        Get the path to an audio file in the local audio directory.
        """
        return os.path.join(self.audio_directory, filename)
