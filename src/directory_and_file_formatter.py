import re
import os
from loguru import logger
from unidecode import unidecode


# function to sanitize a filename or directory name
def sanitize_name(name):
    # convert the name to lowercase
    name = name.lower()

    # replace consecutive underscores with a single underscore
    name = re.sub(r'_+', '_', name)

    # replace space followed by hyphen with an underscore
    name = name.replace(' - ', '_')

    # replace spaces with underscores
    name = name.replace(' ', '_')

    # replace hyphens with underscores
    name = name.replace('-', '_')

    # remove diacritical marks (accents) from Unicode characters
    name = unidecode(name)

    # remove all non-alphanumeric characters
    name = re.sub(r'\W+', '', name)

    return name


def rename_files_and_directories_in_directory(directory):
    # loop through the list of filenames and directories in the given directory
    for item in os.listdir(directory):
        # construct the full path of the item by joining the directory path and the item name
        item_path = os.path.join(directory, item)

        # check if the item in the directory is a file
        if os.path.isfile(item_path):
            # split the filename into the base name and extension parts
            base_name, extension = os.path.splitext(item)

            # sanitize the base name of the file using the 'sanitize_name' function
            new_name = sanitize_name(base_name) + extension

            # create the new path for the renamed file
            new_item_path = os.path.join(directory, new_name)

            # rename the file by moving it to the new path with the sanitized name
            os.rename(item_path, new_item_path)

            # print the old and new names for each renamed file
            logger.info(f"File '{item}' renamed to '{new_name}'")

        # check if the item in the directory is a subdirectory
        elif os.path.isdir(item_path):
            # sanitize the name of the directory using the 'sanitize_name' function
            new_name = sanitize_name(item)

            # create the new path for the renamed directory
            new_item_path = os.path.join(directory, new_name)

            # rename the directory by moving it to the new path with the sanitized name
            os.rename(item_path, new_item_path)

            # logger.info() the old and new names for each renamed directory
            logger.info(f"Directory '{item}' renamed to '{new_name}'")

            # now, call the function recursively to handle subdirectories
            rename_files_and_directories_in_directory(new_item_path)


if __name__ == "__main__":
    while True:
        directory_input = input("Enter the directory or the directory with the files you want to format:")
        rename_files_and_directories_in_directory(directory_input)
        logger.info("File and directory renaming completed!")
