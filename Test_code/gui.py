from tkinter import *
from tkinter import filedialog
import local_audio_transcribe

# Initialize the main window
window = Tk()
window.title("Audio Directory Transcriber")
window.minsize(width=600, height=600)

# Program main label Title
my_label = Label(window, text="Mp3 Audio Directory Transcriber", font=("Arial", 20, "bold"))
my_label.pack(pady=10)

# Select Directory
def select_directory(directory_label, directory_var):
    """Open a directory selection dialog and update the specified variable and label."""
    directory = filedialog.askdirectory()
    if directory:
        # Ensure the path is saved in the correct format
        raw_directory = r"{}".format(directory)
        directory_label.config(text=raw_directory)
        setattr(local_audio_transcribe, directory_var, raw_directory)

# Sets selected Directory
def set_audio_directory():
    """Define button click functions to select directories and update variables."""
    select_directory(audio_directory_label, 'audio_directory')

def set_output_directory():
    """Define button click functions to select directories and update variables."""
    select_directory(output_directory_label, 'output_directory')

def set_completed_audio_directory():
    """Define button click functions to select directories and update variables."""
    select_directory(completed_directory_label, 'completed_audio_directory')

# Directories label and buttons
audio_directory_button = Button(window, text="Audio Directory", command=set_audio_directory)
audio_directory_button.pack(pady=5)
audio_directory_label = Label(window, text="Select Audio Directory")
audio_directory_label.pack(pady=5)

audio_output_directory_button = Button(window, text="Output Directory", command=set_output_directory)
audio_output_directory_button.pack(pady=5)
output_directory_label = Label(window, text="Select Output Directory")
output_directory_label.pack(pady=5)

completed_button = Button(window, text="Completed Audio Directory", command=set_completed_audio_directory)
completed_button.pack(pady=5)
completed_directory_label = Label(window, text="Select Completed Audio Directory")
completed_directory_label.pack(pady=5)

# Transcribe button
def transcribe():
    """Check if all directories are set and then transcribe the audio files."""
    if local_audio_transcribe.audio_directory and local_audio_transcribe.output_directory and local_audio_transcribe.completed_audio_directory:
        try:
            local_audio_transcribe.transcribe_audio_directory(
                local_audio_transcribe.audio_directory,
                local_audio_transcribe.output_directory,
                local_audio_transcribe.completed_audio_directory
            )
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Please select all directories before transcribing.")

transcribe_button = Button(window, text="Transcribe", command=transcribe)
transcribe_button.pack(side=BOTTOM, pady=20)

window.mainloop()
