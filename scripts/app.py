import tkinter as tk
from tkinter import filedialog
import processing_script  # Import your processing script

class DocumentProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Processor")

        # Create and pack GUI elements
        self.upload_button = tk.Button(root, text="Upload Document", command=self.upload_document)
        self.upload_button.pack(pady=10)

        self.process_button = tk.Button(root, text="Process Document", command=self.process_document)
        self.process_button.pack(pady=10)

    def upload_document(self):
        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")])
        # Store the file_path for later processing
        self.file_path = file_path
        tk.messagebox.showinfo("Success!", "Document has been uploaded!")
        
    def process_document(self):
        if hasattr(self, 'file_path'):
            # Call your processing script with the file_path
            a = processing_script.process_document(self.file_path)
            tk.messagebox.showinfo("Document processing result:", f"{a}")
        else:
            tk.messagebox.showwarning("Error", "Seems like you haven't uploaded a document, you fool! Please upload a document first, then we'll be fine.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentProcessorApp(root)
    root.mainloop()


        
