import tkinter as tk
from tkinter import filedialog, messagebox
from file_organizer import organize_files

root = tk.Tk()
root.title('File Organizer Bot')
root.geometry('500x150')

folder_path_var = tk.StringVar()

tk.Label(root,text="Select Folder to Organize:").pack(pady=5)
tk.Entry(root, textvariable=folder_path_var, width=50).pack(padx=10)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

tk.Button(root, text='Browse', command=browse_folder).pack(pady=5)

def start_organizing():
    folder_path = folder_path_var.get()
    if not folder_path:
        messagebox.showwarning("Warning","Please select a folder")
        return
    organize_files(folder_path)
    messagebox.showinfo("Success", "Folder Organized successfully!")

tk.Button(root, text="Organize Files", command=start_organizing).pack(pady=10)

root.mainloop()