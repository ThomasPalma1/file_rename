import os
import shutil


def organize_files(path):
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(os.path.join(path, extension)):
            try:
                shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
            except PermissionError:
                print(f"Cannot move '{file}' as it's in use by another process.")
        else:
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))


if __name__ == "__main__":
    path = input("Enter the directory you want to organize:\n")
    organize_files(path)
