import os
import shutil

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

src_dirs = ['F:\\Videos-test\\test1', 'F:\\Videos-test\\test2']
dst_dir = 'F:\\Videos-test\\output'
search_and_copy(src_dirs, dst_dir)
