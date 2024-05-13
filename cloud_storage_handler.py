from abc import ABC, abstractmethod

class CloudStorageHandler(ABC):
    """
    Abstract base class for cloud storage handlers.

    This class defines the interface for cloud storage handlers, ensuring that
    all subclasses provide implementations for listing folders, listing files,
    and retrieving audio files.
    """
    
    def __init__(self):
        self.client = None

    @abstractmethod
    def list_folders(self):
        """
        List folders in the cloud storage.

        This method must be implemented by any subclass.
        """
        pass

    @abstractmethod
    def list_files(self, folder):
        """
        List files in a specific folder in the cloud storage.

        This method must be implemented by any subclass.
        """
        pass

    @abstractmethod
    def get_audio_file(self, key):
        """
        Get an audio file from the cloud storage.

        This method must be implemented by any subclass.
        """
        pass
