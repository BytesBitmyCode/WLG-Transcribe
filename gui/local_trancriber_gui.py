from tkinter import *
from tkinter import filedialog
import LocalAudioTranscriber

# Initialize the main window
window = Tk()
window.title("Local Audio Transcriber")
window.minsize(width=600, height=600)

# Program main label Title
my_label = Label(window, text="Mp3 Audio Transcriber", font=("Arial", 20, "bold"))
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


# Directories label and buttons
audio_directory_button = Button(window, text="Audio Directory", command=set_audio_directory)
audio_directory_button.pack(pady=5)
audio_directory_label = Label(window, text="Select Audio Directory")
audio_directory_label.pack(pady=5)



# Transcribe button
transcribe_button = Button(window, text="Transcribe", command=LocalAudioTranscriber)
transcribe_button.pack(side=BOTTOM, pady=20)

window.mainloop()
