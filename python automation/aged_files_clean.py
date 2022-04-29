import os
import datetime

path_to_check = input("Enter a valid path to find the files older than 3 days? ")

if not os.path.exists(path_to_check) or os.path.isfile(path_to_check):
    print("The path entered is invalid!!")
    os._exit(1)
today = datetime.datetime.now()
for each_file in os.listdir(path_to_check):
    file_path = os.path.join(path_to_check,each_file)
    age_of_file = (today - datetime.datetime.fromtimestamp(os.path.getctime(file_path))).days
    if os.path.isfile(file_path) and age_of_file > 3:
        # You can delete the file here
        print(f"{file_path} ---> {age_of_file}")

