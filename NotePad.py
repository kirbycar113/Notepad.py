# Simple Text Editor (No External Libraries)

import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {str(e)}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text.get(1.0, tk.END))
                messagebox.showinfo("Saved", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {str(e)}")

root = tk.Tk()
root.title("Simple Text Editor")

# Create a text widget
text = tk.Text(root, wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)

# Create menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

root.mainloop()
