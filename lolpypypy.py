import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {str(e)}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text.get(1.0, tk.END))
                messagebox.showinfo("Saved", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {str(e)}")

def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def update_word_count():
    content = text.get(1.0, tk.END)
    words = content.split()
    word_count = len(words)
    status_var.set(f"Word Count: {word_count}")

root = tk.Tk()
root.title("Enhanced Text Editor")

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

# Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menubar)

# Status bar for word count
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Update word count initially
update_word_count()

root.mainloop()
