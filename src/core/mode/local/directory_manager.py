import os

class DirectoryManager:
    def __init__(self):
        # Initialize all attributes
        self.audio_path = None
        self.audio_directory = None
        self.output_directory = None
        self.completed_directory = None
        self.single_audio_file = None

        # Prompt for audio path and setup directories
        self.audio_path = self.prompt_path("Enter the path to your audio file or directory: ")
        self.determine_and_setup_directories()

    def prompt_path(self, message):
        """Prompt the user to input a path and format it for use."""
        while True:
            path = input(message)
            if os.path.exists(path):  # Check if the path is valid
                return rf"{path}"  # Raw formatted string to handle path correctly
            else:
                print(f"Error: The path {path} is not valid. Please ensure the path exists and try again.")

    def determine_and_setup_directories(self):
        """Set up directories for transcriptions and completed audio files based on the audio path."""
        if os.path.isdir(self.audio_path):
            self.audio_directory = self.audio_path
            self.output_directory = os.path.join(self.audio_directory, "transcriptions")
            self.completed_directory = os.path.join(self.audio_directory, "completed")
        elif os.path.isfile(self.audio_path):
            self.single_audio_file = self.audio_path
            self.audio_directory = os.path.dirname(self.audio_path)
            self.output_directory = os.path.join(self.audio_directory, "transcriptions")
            self.completed_directory = os.path.join(self.audio_directory, "completed")

        # Create directories if they don't exist
        if self.audio_directory:  # Ensure the directory exists
            os.makedirs(self.output_directory, exist_ok=True)
            os.makedirs(self.completed_directory, exist_ok=True)
            print(f"Directories for output and completed audio have been set up at {self.audio_directory}")

    def get_directories(self):
        """Return the paths for audio, output, and completed directories."""
        return self.audio_directory, self.output_directory, self.completed_directory, self.single_audio_file
