import os
import shutil
from loguru import logger


def organize_files(directory):
    files = os.listdir(directory)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(os.path.join(directory, extension)):
            try:
                shutil.move(os.path.join(directory, file), os.path.join(directory, extension, file))
            except PermissionError:
                logger.info(f"Cannot move '{file}' as it's in use by another process.")
        else:
            os.makedirs(os.path.join(directory, extension))
            shutil.move(os.path.join(directory, file), os.path.join(directory, extension, file))


if __name__ == "__main__":
    path = input("Enter the directory you want to organize:\n")
    organize_files(path)
