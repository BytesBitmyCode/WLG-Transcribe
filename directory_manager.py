# directory_manager.py
import os
from tkinter import filedialog, Tk

def select_directory():
    """
    Open a dialog to select a directory.
    """
    print("Initializing Tkinter root...")
    root = Tk()
    root.withdraw()  # Hide the Tkinter root window
    print("Opening directory selection dialog...")
    selected_directory = filedialog.askdirectory()
    print("Dialog opened, selected directory:", selected_directory)
    root.update()  # Update the root window
    root.destroy()  # Destroy the Tkinter root window
    print("Tkinter root destroyed")
    return selected_directory

if __name__ == "__main__":
    # Test the directory selection independently
    print("Please select a directory")
    selected_directory = select_directory()
    print(f"Selected directory: {selected_directory}")
