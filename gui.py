import tkinter as tk
import os
from tkinter import filedialog
import tkinter.simpledialog
import tkinter.messagebox as messagebox
import shutil
import pickle

def browse_src_dirs():
    global src_dirs
    src_dirs = filedialog.askdirectory(parent=root, initialdir= "/", title='Please select a directory')
    src_dirs_entry.delete(0, tk.END)
    src_dirs_entry.insert(0, src_dirs)
    import sys
    from cx_Freeze import setup, Executable

def browse_dst_dir():
    global dst_dir
    dst_dir = filedialog.askdirectory(parent=root, initialdir= "/", title='Please select a directory')
    dst_dir_entry.delete(0, tk.END)
    dst_dir_entry.insert(0, dst_dir)

END = tk.END

def select_additional_files():
    num_files = tk.simpledialog.askinteger("Number of Files", "How many files do you want to select?", minvalue=1)
    if num_files:
        additional_files = []
        for i in range(num_files):
            directory = filedialog.askdirectory(title="Select Additional Directory {}".format(i + 1))
            if directory:
                additional_files.append(directory)
        additional_files_entry.delete(0, tk.END)
        additional_files_entry.insert(0, ", ".join(additional_files))

def expand_src_dirs():
    new_window = tk.Toplevel(root)
    new_window.title("Expanded Source Directories")
    new_window.geometry("500x500")
    src_dirs_text = tk.Text(new_window, font=("Helvetica", 12))
    src_dirs_text.pack(fill='both', expand=True)
    src_dirs_text.insert('1.0', src_dirs_entry.get())

def expand_additional_files():
    new_window = tk.Toplevel(root)
    new_window.title("Expanded Additional Files")
    new_window.geometry("500x500")
    additional_files_text = tk.Text(new_window, font=("Helvetica", 12))
    additional_files_text.pack(fill='both', expand=True)
    additional_files_text.insert('1.0', "\n".join(additional_files))
    
def expand_dst_dir():
    new_window = tk.Toplevel(root)
    new_window.title("Expanded Destination Directory")
    new_window.geometry("500x500")
    dst_dir_text = tk.Text(new_window, font=("Helvetica", 12))
    dst_dir_text.pack(fill='both', expand=True)
    dst_dir_text.insert('1.0', dst_dir_entry.get())

def copy_files():
    src_dir = src_dirs_entry.get()
    dst_dir = dst_dir_entry.get()
    additional_files_string = additional_files_entry.get()
    additional_files = []
    if os.path.isdir(additional_files_string):
        for dirpath, dirnames, filenames in os.walk(additional_files_string):
            for file in filenames:
                additional_files.append(os.path.join(dirpath, file))
    all_files = []
    if not src_dir or not dst_dir:
        src_dirs_label.config(fg="red")
        dst_dir_label.config(fg="red")
        status_label.config(text="Please select both source and destination directories!")
        return
    if not os.path.exists(src_dir):
        status_label.config(text="Source directory does not exist!")
        return
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    all_files = []
    files = [f for f in os.listdir(src_dir) if f.endswith('.mp4')]
    if not files:
        status_label.config(text="No .mp4 files found in source directory!")
        return
    all_files.extend([os.path.join(src_dir, f) for f in files])
    all_files.extend(additional_files)
    copied_files = 0
    for src in all_files:
        if not os.path.exists(src):
            continue
        if not src.endswith('.mp4'):
            continue
        dst = os.path.join(dst_dir, os.path.basename(src))
        if os.path.exists(dst):
            copied_files += 1
            continue
        try:
            shutil.copy(src, dst)
            copied_files += 1
        except Exception as e:
            print(f"Could not copy {src}: {e}")
    if copied_files == len(all_files):
        status_label.config(text="Copied all files.")
    else:
        status_label.config(text=f"Could not copy {len(all_files) - copied_files} files.")

root = tk.Tk()
root.title("Copy Videos")
root.geometry("700x350")
root.config(bg='white')

src_dirs_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
src_dirs_frame.pack(pady=(10, 0))

src_dirs_warning = tk.Label(src_dirs_frame, text="*", font=("Helvetica", 12), fg="red")
src_dirs_warning.pack(side='left', padx=(0, 10))

src_dirs_label = tk.Label(src_dirs_frame, text="Source Directories:", font=("Helvetica", 12))
src_dirs_label.pack(side='left', padx=(0, 10))

src_dirs_entry = tk.Entry(src_dirs_frame, font=("Helvetica", 12), bd=2, relief=tk.SUNKEN)
src_dirs_entry.pack(side='left', fill='x', expand=True)

src_dirs_button = tk.Button(src_dirs_frame, text="Browse", font=("Helvetica", 12), command=browse_src_dirs, bg="#fec89a", activebackground="#ffd7ba")
src_dirs_button.pack(side='left', padx=(10, 0))

src_dirs_expand_button = tk.Button(src_dirs_frame, text="Expand", font=("Helvetica", 12), command=expand_src_dirs, bg="#fec5bb", activebackground="#fcd5ce")
src_dirs_expand_button.pack(side='left', padx=(10, 0))

additional_files_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
additional_files_frame.pack(pady=(10, 0))

additional_files_label = tk.Label(additional_files_frame, text="Additional Files:", font=("Helvetica", 12))
additional_files_label.pack(side='left', padx=(0, 10))

additional_files_entry = tk.Entry(additional_files_frame, font=("Helvetica", 12), bd=2, relief=tk.SUNKEN)
additional_files_entry.pack(side='left', fill='x', expand=True)

additional_files_browse_button = tk.Button(additional_files_frame, text="Select", font=("Helvetica", 12), command=select_additional_files, bg="#fec89a", activebackground="#ffd7ba")
additional_files_browse_button.pack(side='left', padx=(10, 0))

additional_files_expand_button = tk.Button(additional_files_frame, text="Expand", font=("Helvetica", 12), command=expand_additional_files, bg="#fec5bb", activebackground="#fcd5ce")
additional_files_expand_button.pack(side='left', padx=(10, 0))

dst_dir_frame = tk.Frame(root, bg='white')
dst_dir_frame.pack(pady=(20, 0))

dst_dir_warning = tk.Label(dst_dir_frame, text="*", font=("Helvetica", 12), fg="red", bg='white')
dst_dir_warning.pack(side='left', padx=(0, 10))

dst_dir_label = tk.Label(dst_dir_frame, text="Destination Directory:", font=("Helvetica", 12), bg='white')
dst_dir_label.pack(side='left', padx=(0, 10))

dst_dir_entry = tk.Entry(dst_dir_frame, font=("Helvetica", 12))
dst_dir_entry.pack(side='left', fill='x', expand=True)

dst_dir_browse_button = tk.Button(dst_dir_frame, text="Browse", font=("Helvetica", 12), command=browse_dst_dir, bg="#fec89a", activebackground="#ffd7ba")
dst_dir_browse_button.pack(side='left', padx=(10, 0))

dst_dir_expand_button = tk.Button(dst_dir_frame, text="Expand", font=("Helvetica", 12), command=expand_dst_dir, bg="#fec5bb", activebackground="#fcd5ce")
dst_dir_expand_button.pack(side='left', padx=(10, 0))

copy_files_button = tk.Button(root, text="Copy Files", font=("Helvetica", 12), command=copy_files, bg="#ffafcc", activebackground="#ffc8dd")
copy_files_button.pack(pady=(30, 0))

status_label = tk.Label(root, text="", font=("Helvetica", 12), bg='white')
status_label.pack(pady=(20, 0))

root.mainloop()
