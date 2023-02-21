## Table of Contents

1. [Python Copy Videofiles](#python-copy-videofiles)
2. [Story 1 - Copying from a single directory ](#story-1---copying-from-a-single-directory)
3. [Story 2 - Copying from multiple directories ](#story-2---copying-from-multiple-directories)
4. [Story 3 - Copying with existing file check ](#story-3---copying-with-existing-file-check)
2. [Functionality](#functionality)
   - browse_src_dirs()
   - browse_dst_dir()
   - select_additional_files()
   - expand_src_dirs()
   - expand_additional_files()
   - expand_dst_dir()
   - copy_files()
3. [User Interface](#user-interface)
4. [How Does it works?](#how-does-it-works)
5. [Requirements](#requirements)
6. [Usage](#usage)
7. [ search_and_copy() Function](#search-and-copy)
   - Input Parameters
   - Output
   - Implementation
8. [main() Function](#main-function)
   - Implementation
9. [Dependencies](#dependencies)
10. [copy_files_gui() function](#copy-files-gui)
11. [Support](#support)
12. [License](#license)

# Python Copy Videofiles

This is a Python program that allows the user to copy video files from a source directory and any additional directories to a destination directory using a GUI created with the tkinter library.

# Story 1 - Copying from a single directory
This will search for all .mp4 files in the Test1 directory and copy them to the Output directory.

```sh
src_dirs = ['C:/Videos/Test1']
dst_dir = 'C:/Videos/Output'
search_and_copy(src_dirs, dst_dir)
```

# Story 2 - Copying from multiple directories:
This will search for all .mp4 files in the Test1 and Test2 directories and copy them to the Output directory.

```sh
src_dirs = ['C:/Videos/Test1', 'C:/Videos/Test2']
dst_dir = 'C:/Videos/Output'
search_and_copy(src_dirs, dst_dir)
```

# Story 3 - Copying with existing file check:
This will search for all .mp4 files in the Test1 and Test2 directories and copy them to the Output directory only if they do not already exist in the Output directory.

```sh
src_dirs = ['C:/Videos/Test1', 'C:/Videos/Test2']
dst_dir = 'C:/Videos/Output'
search_and_copy(src_dirs, dst_dir, check_existing=True)
```

# Functionality:
The program has several functions to enable the user to browse and select the source and destination directories and any additional directories to include in the copy process.
-`browse_src_dirs()`: This function opens a file dialog and prompts the user to select a source directory. The path to the selected directory is saved in the global variable src_dirs
- `browse_dst_dir()`: This function opens a file dialog and prompts the user to select a destination directory. The path to the selected directory is saved in the global variable dst_dir
- `select_additional_files()`: This function prompts the user to enter the number of additional directories they want to include in the copy process and then prompts them to select those directories using a file dialog. The selected directories are stored in the additional_files list
- `expand_src_dirs()`, `expand_additional_files()`, and `expand_dst_dir()`: These functions open new windows that display the contents of the corresponding directories
- `copy_files()`: This function copies all .mp4 files from the source directory and any additional directories to the destination directory. If a file with the same name already exists in the destination directory, the program skips the copy. The function updates the status label to indicate how many files were copied and if there were any errors

# User Interface:
The user interface is created with the tkinter library and includes labels, entry fields, and buttons to interact with the functions described above. The program prompts the user to select a source directory, a destination directory, and any additional directories to include in the copy process. It also displays the status of the copy process.

# How Does it works?
- The program prompts the user to select a source directory and a destination directory, as well as any additional directories that they want to include in the copy process.
- The `browse_src_dirs()` and `browse_dst_dir()` functions prompt the user to select a directory using a file dialog and save the path to the selected directory in the src_dirs and dst_dir global variables, respectively.
- The `select_additional_files()` function prompts the user to enter the number of additional directories they want to include in the copy process and then prompts them to select those directories using a file dialog. The selected directories are stored in the additional_files list.
- The `expand_src_dirs()`, `expand_additional_files()`, and `expand_dst_dir()` functions open new windows that display the contents of the corresponding directories.
- The `copy_files()` function copies all .mp4 files from the source directory and any additional directories to the destination directory. If a file with the same name already exists in the destination directory, the program skips the copy. The function updates the status label to indicate how many files were copied and if there were any errors.
- The main part of the code creates a tkinter GUI with labels, entry fields, and buttons to interact with the functions described above.

# Requirements

Python 3.6 or later
Required packages listed in requirements.txt
To install the required packages, run the following command in your terminal:

```sh
pip install -r requirements.txt
```

# Usage
To run the script, use the following command in your terminal:
```sh
python gui.py
```

Once the GUI is open, use the "Select Source Directory", "Select Additional Directories", and "Select Destination Directory" buttons to choose the directories to include in the copy process. Use the "Expand" buttons to view the contents of the selected directories. Finally, click the "Copy Files" button to copy all .mp4 files from the selected directories to the destination directory.

# search_and_copy() Function

The `search_and_copy()` function is used to search for all `.mp4` files in the specified source directories and copy them to the specified destination directory. The function checks whether each file has already been copied, and only copies it if it hasn't been.

## Input Parameters

The search_and_copy() function takes two input parameters:
* `src_dirs`: A list of source directories to search for .mp4 files.
* `dst_dir`: The destination directory to copy the files to.

## Output

The `search_and_copy()` function doesn't return any output. Instead, it prints a message to the console indicating whether any files were copied.

## Implementation

The `search_and_copy()` function is implemented as follows:
1. Initialize the `copied` variable to `False` to indicate that no files have been copied yet.
2. Read the contents of the `files.txt` file to get a list of all files that have already been copied. This file is used to keep track of which files have already been copied to the destination directory.
3. For each source directory specified in `src_dirs`, search for all `.mp4` files in the directory and its subdirectories using the `os.walk()` function.
4. For each `.mp4` file found, check whether it has already been copied to the destination directory by checking whether its name appears in the `file_names` list.
5. If the file hasn't been copied yet, copy it to the destination directory using the `shutil.copy()` function and update the `files.txt` file with the name of the copied file.
6. If at least one file was `copied`, set the copied variable to `True`.
7. If no files were copied, check whether all `.mp4` files in the source directories have already been copied to the destination directory. If so, print a message to the console indicating that all files have already been copied.

# main() Function

The `main()` function is used to prompt the user to specify the source directories and destination directory, and then call the `search_and_copy()` function to copy the `.mp4` files.

## Implementation

The `main()` function is implemented as follows:
1. Prompt the user to enter the paths of the source directories to search for `.mp4` files, separated by commas.
2. Split the user input into a list of directories using the `split()` function.
3. Prompt the user to enter the path of the destination directory to copy the files to.
4. Call the `search_and_copy()` function with the source directories and destination directory as input parameters

# Dependencies

The code uses the following Python modules:
* `os`: Used to search for files in directories and subdirectories.
* `shutil`: Used to copy files.
* `tkinter`: Used to create the GUI.


# copy_files_gui() function
* The copy_files_gui() function is called when the Copy files button is clicked.
* It retrieves the values of the source directory, destination directory, and additional directories entry fields using the get() method.
* It calls the search_and_copy() function with the source directories and destination directory as arguments.
* It updates the status label to indicate how many files were copied and if there were any errors.


# Configuration

The script requires user to select directories in the guy.exe:

- Source Directories
- Additional Directories (Optional)
- Destination Directory

# Contributors ✨

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://hurr13ane.com"><img src="https://avatars.githubusercontent.com/u/76591840?v=4" width="100px;" alt="Jeroen Engels"/><br /><sub><b>Diana-Maria Iercosan</b></sub></a><br />
      </td>
    </tr>
  </tbody>
</table>

# Support
For any questions or support, please contact me via https://hurr13ane.com/contact/

# License
This project is licensed under the MIT License.
