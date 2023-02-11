import tkinter as tk
from tkinter import font
import sys
import os

def show_content():
    with open("files.txt", "r") as file:
        content = file.read()
    content_label.config(text=content)

def back_to_main():
    root.destroy()
    os.system('python gui.py')
    sys.exit()

root = tk.Tk()
root.geometry("700x350")
root.title("Text File Viewer")

frame = tk.Frame(root, bg="#F0997D")
frame.pack(padx=10, pady=10)

file_label = tk.Label(frame, text="Contents of files.txt:", font=("Helvetica", 16), bg="#F0997D", fg="white")
file_label.grid(row=0, column=0, padx=10, pady=10)

content_label = tk.Label(frame, text="", font=("Helvetica", 14), bg="#F0997D", fg="white")
content_label.grid(row=1, column=0, padx=10, pady=10)

show_content_button = tk.Button(frame, text="Show Content", command=show_content, font=("Helvetica", 14), bg="white", fg="#F0997D", activebackground="#D3756B", activeforeground="white")
show_content_button.grid(row=2, column=0, padx=10, pady=10)

back_button = tk.Button(frame, text="Back", command=back_to_main, font=("Helvetica", 14), bg="white", fg="#F0997D", activebackground="#F0997D", activeforeground="white")
back_button.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
