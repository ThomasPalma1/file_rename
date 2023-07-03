import os  # importing the 'os' module for operating system-related functionalities
import re  # importing the 're' module for regular expression matching
from time import sleep  # importing the 'sleep' function from the 'time' module

# define the directory containing the files to be renamed
folder = ''

# get a list of all files in the directory
files = os.listdir(folder)

# define a regular expression pattern to extract the numerical part of the filename
pattern = re.compile(r'^.*?(\d+)')

# sort the list of files based on their numerical part, if any
files.sort(key=lambda x: int(pattern.search(x).group(1)) if pattern.search(x) else float('inf'))

# count the number of files in the directory before adding a new file
num_files_before = sum(1 for file in files if os.path.isfile(os.path.join(folder, file)))

# create an empty file in the specified directory for testing
filename = 'test.txt'
filepath = os.path.join(folder, filename)

with open(filepath, 'w') as f:  # open the file in write mode (create if it doesn't exist) and assign it to 'f'
    pass  # placeholder statement (does nothing)


# define a function to rename all files in the directory numerically
def rename_all_files_numerically(files):
    name_count = {}  # create an empty dictionary to keep track of new file names
    for i, file in enumerate(files, start=1):  # iterate over the files with an index starting from 1
        old_file = os.path.join(folder, file)  # create the old file path by joining the folder path and file name

        # skip directories
        if os.path.isdir(old_file):  # if the current file is a directory, skip it and continue to the next file
            continue

        # get the base name and extension of the file
        base_name, extension = os.path.splitext(file)  # split the file name into base name and extension

        # generate the new name for the file
        new_name = f'{i}{extension}'  # generate a new name using the index and the original file's extension

        # if the new name already exists, generate a new name with a higher number
        while new_name in name_count:  # check if the new name already exists in the dictionary
            i += 1  # increment the index to generate a new number
            new_name = f'{i}{extension}'  # generate a new name using the updated index

        # mark the new name as used
        name_count[new_name] = True  # add the new name as a key in the dictionary

        # construct the new file path
        new_file = os.path.join(folder, new_name)  # create the new file path by joining the folder path and new name

        # attempt to rename the file
        try:
            os.rename(old_file, new_file)  # rename the old file to the new file name
            print(new_name)  # print the new file name
        except FileExistsError:
            continue  # if a file with the new name already exists, skip and continue to the next file

    # count the number of files in the directory after renaming
    files = [file for file in os.listdir(folder) if
             os.path.isfile(os.path.join(folder, file))]  # get all files in the directory (excluding directories)
    num_files_after = len(files)  # count the number of files after renaming

    # print the number of files before and after renaming, then wait 5 seconds and delete the test file
    print(f"total number of files before: {num_files_before}")  # print the total number of files before renaming
    print(f"total number of files after: {num_files_after}")  # print the total number of files after renaming
    sleep(5)  # wait for 5 seconds
    os.remove(filepath)  # delete the test file


# call the function to rename all files in the directory numerically
rename_all_files_numerically(files)  # call the 'rename_all_files_numerically' function with the 'files' list as input
