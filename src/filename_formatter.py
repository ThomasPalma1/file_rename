import re  # importing the regular expression module
import os  # importing the operating system module
from unidecode import unidecode  # importing the unidecode function from the unidecode module

# function to sanitize a filename
def sanitize_filename(filename):
    filename = filename.lower()  # convert the filename to lowercase

    filename = re.sub(r'_+', '_', filename)  # replace consecutive underscores with a single underscore

    filename = filename.replace(' - ', '_')  # replace space followed by hyphen with an underscore

    filename = filename.replace(' ', '_')  # replace spaces with underscores

    filename = filename.replace('-', '_')  # replace hyphens with underscores

    filename = unidecode(filename)  # remove diacritical marks (accents) from Unicode characters

    filename = re.sub(r'\W+', '', filename)  # remove all non-alphanumeric characters

    return filename  # return the sanitized filename


directory = ""  # directory path containing the files

for filename in os.listdir(directory):  # loop over the filenames in the directory

    file_path = os.path.join(directory, filename)  # full path to the current file

    if os.path.isfile(file_path):  # check if the path is a file (not a directory)

        base_name, extension = os.path.splitext(filename)  # split the filename into base name and extension

        new_filename = sanitize_filename(base_name)  # get the sanitized base name

        new_filename = new_filename + extension  # add the extension to the sanitized base name

        new_file_path = os.path.join(directory, new_filename)  # full path to the new filename

        os.rename(file_path, new_file_path)  # rename the file by moving it to the new path

        # print the old and new filenames for each renamed file
        print(f"File '{filename}' renamed to '{new_filename}'")

print("File renaming completed!")  # print a message indicating the completion of file renaming
