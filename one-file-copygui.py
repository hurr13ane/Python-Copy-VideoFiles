import os
import shutil
import tkinter as tk
from tkinter import filedialog
import sys


def open_files_gui():
    root.destroy()
    os.system('python files-gui.py')
    sys.exit()

def search_and_copy(src_dirs, dst_dir):
    copied = False
    file_names = []
    with open("files.txt", "a+") as f:
        f.seek(0)
        file_names = f.readlines()
        file_names = [x.strip() for x in file_names]
        for src_dir in src_dirs:
            for subdir, dirs, files in os.walk(src_dir):
                for file in files:
                    file_path = subdir + os.sep + file
                    if file.endswith(".mp4"):
                        dst_file_path = os.path.join(dst_dir, file)
                        if file not in file_names:
                            shutil.copy(file_path, dst_dir)
                            f.write(file + "\n")
                            copied = True
    if not copied:
        all_files_copied = True
        for src_dir in src_dirs:
            for subdir, dirs, files in os.walk(src_dir):
                for file in files:
                    if file.endswith(".mp4"):
                        dst_file_path = os.path.join(dst_dir, file)
                        if not os.path.exists(dst_file_path):
                            all_files_copied = False
        if all_files_copied:
            print("You already copied those videos.")

def browse_src_dirs():
    src_dirs = filedialog.askdirectory(title="Select source directories")
    src_dirs_entry.insert(0, src_dirs)

    
def browse_dst_dir():
    dst_dir = filedialog.askdirectory(title="Select destination directory")
    dst_dir_entry.insert(0, dst_dir)

def copy_files():
    src_dirs = src_dirs_entry.get().split(";")
    dst_dir = dst_dir_entry.get()
    search_and_copy(src_dirs, dst_dir)


root = tk.Tk()
root.title("Copy Videos")
root.geometry("700x350")
root.config(bg='white')

def switch_theme():
    global theme
    theme = "dark" if theme == "white" else "white"
    change_theme()

def change_theme():
    if theme == "white":
        root.configure(bg="#FFFFFF")
        src_dirs_label.configure(bg="#FFFFFF", fg="#000000")
        dst_dir_label.configure(bg="#FFFFFF", fg="#000000")
        src_dirs_entry.configure(bg="#FFFFFF", fg="#000000")
        dst_dir_entry.configure(bg="#FFFFFF", fg="#000000")
        src_dirs_button.configure(bg="#FFC3A1", fg="#000000", activebackground="#D3756B")
        dst_dir_button.configure(bg="#FFC3A1", fg="#000000", activebackground="#D3756B")
        copy_button.configure(bg="#FFCCD2", fg="#000000", activebackground="#990000")
        see_file_button.configure(bg="#F7A4A4", fg="#000000", activebackground="#A62349")
        theme_button.configure(bg="#FFCCD2", fg="#000000", activebackground="#990000")
    else:
        root.configure(bg="#262626")
        src_dirs_label.configure(bg="#262626", fg="#FFFFFF")
        dst_dir_label.configure(bg="#262626", fg="#FFFFFF")
        src_dirs_entry.configure(bg="#262626", fg="#FFFFFF")
        dst_dir_entry.configure(bg="#262626", fg="#FFFFFF")
        src_dirs_button.configure(bg="#D3756B", fg="#FFFFFF", activebackground="#FFC3A1")
        dst_dir_button.configure(bg="#D3756B", fg="#FFFFFF", activebackground="#FFC3A1")
        copy_button.configure(bg="#990000", fg="#FFFFFF", activebackground="#FFCCD2")
        see_file_button.configure(bg="#A62349", fg="#FFFFFF", activebackground="#F7A4A4")
        theme_button.configure(bg="#990000", fg="#FFFFFF", activebackground="#FFCCD2")

theme = "white"

src_dirs_label = tk.Label(root, text="Source Directories:", font=("Helvetica", 12))
src_dirs_label.pack(pady=(10, 0))

src_dirs_entry = tk.Entry(root, width=60, font=("Helvetica", 12))
src_dirs_entry.pack(pady=(0, 2))

src_dirs_button = tk.Button(root, text="Browse", height=1, width=50, command=browse_src_dirs, font=("Helvetica", 12), bg="#00bfff", activebackground="#0080ff")
src_dirs_button.pack(pady=(2, 10))

dst_dir_label = tk.Label(root, text="Destination Directory:", font=("Helvetica", 12))
dst_dir_label.pack(pady=(10, 0))

dst_dir_entry = tk.Entry(root, width=60, font=("Helvetica", 12))
dst_dir_entry.pack(pady=(0, 2))

dst_dir_button = tk.Button(root, text="Browse", height=1, width=50, command=browse_dst_dir, font=("Helvetica", 12), bg="#00bfff", activebackground="#0080ff")
dst_dir_button.pack(pady=(2, 10))

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

copy_button = tk.Button(buttons_frame, text="Copy Files", command=copy_files, font=("Helvetica", 12), bg="#32CD32", activebackground="#228B22", relief="groove", borderwidth=2)
copy_button.pack(side="left", padx=10)

def open_file():os.startfile("files.txt")

see_file_button = tk.Button(buttons_frame, text="See files.txt", command=open_files_gui, font=("Helvetica", 12), bg="#87CEFA", activebackground="#87CEFA", relief="groove", borderwidth=2)
see_file_button.pack(side="left", padx=10)

theme_button = tk.Button(buttons_frame, text="Switch Theme", command=switch_theme, font=("Helvetica", 12), bg="#FFCCD2", activebackground="#990000")
theme_button.pack(side="left", padx=10)

change_theme()
root.mainloop()



