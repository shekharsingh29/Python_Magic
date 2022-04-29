import os
import platform

# Check if the given path is a file or directory and list all files inside it.
file_path = input("Enter a file to be validated ? ")

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        print(f'{file_path} is a file')
    else:
        print(f'{file_path} is a directory and files under it are:')
        for i,each_file in enumerate(os.listdir(file_path)):
            print(f'{i+1} --> {file_path}\\{each_file}')
else:
    print("!!!! The path entered is invallid")
    os._exit(1)