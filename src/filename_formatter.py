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


def rename_files_in_directory(directory):
    # loop through the list of filenames in the given directory
    for filename in os.listdir(directory):
        # construct the full file path by joining the directory path and the filename
        file_path = os.path.join(directory, filename)

        # check if the item in the directory is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # split the filename into the base name and extension parts
            base_name, extension = os.path.splitext(filename)

            # sanitize the base name of the file using the 'sanitize_filename' function
            new_filename = sanitize_filename(base_name) + extension

            # create the new file path by joining the directory path and the sanitized filename
            new_file_path = os.path.join(directory, new_filename)

            # rename the file by moving it to the new file path with the sanitized filename
            os.rename(file_path, new_file_path)

            # print the old and new filenames for each renamed file
            print(f"File '{filename}' renamed to '{new_filename}'")


if __name__ == "__main__":
    directory_input = input("Enter the directory you want to format the file names:\n")
    rename_files_in_directory(directory_input)
    print("File renaming completed!")
