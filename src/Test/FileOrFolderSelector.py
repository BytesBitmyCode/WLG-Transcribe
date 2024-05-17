import tkinter as tk
from tkinter import filedialog, ttk


class FileOrFolderSelector:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        """Setup user interface elements within the main window."""
        self.root.title("Select File or Folder")
        
        # Dropdown menu to select type
        self.type_choice = tk.StringVar()
        self.type_selector = ttk.Combobox(self.root, textvariable=self.type_choice)
        self.type_selector['values'] = ('File', 'Directory')
        self.type_selector['state'] = 'readonly'  # Prevent typing a value
        self.type_selector.pack(fill=tk.X, expand=True)
        self.type_selector.set('Choose Type')

        # Button to confirm selection and open the appropriate dialog
        button_open = tk.Button(self.root, text="Open", command=self.open_dialog)
        button_open.pack(fill=tk.X, expand=True)

    def open_dialog(self):
        """Open a file or directory dialog based on the type selected in the dropdown."""
        choice = self.type_choice.get()
        if choice == 'File':
            file_path = filedialog.askopenfilename(
                title='Select a file',
                filetypes=(("Audio Files", "*.mp3 *.wav"), ("All files", "*.*"))
            )
            if file_path:
                print(f"File selected: {file_path}")
            else:
                print("No file selected.")
        elif choice == 'Directory':
            dir_path = filedialog.askdirectory(title='Select a directory')
            if dir_path:
                print(f"Directory selected: {dir_path}")
            else:
                print("No directory selected.")
        self.root.destroy()  # Close the window after selection
        
# Create the main application window
root = tk.Tk()
app = FileOrFolderSelector(root)
root.mainloop()
