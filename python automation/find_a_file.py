import os
import platform
import string

# Serach of file should be platform independent
search_file = input("Enter the file name you need to search?")

# To find drive list in windows
win_drive_list = []
for letter in string.ascii_uppercase:
    drive_letter = letter + ":"
    if os.path.exists(drive_letter):
        win_drive_list.append(drive_letter)

if platform.system() == 'Windows':
    print(f"Searching in {platform.system()} platform....\n\n")
    for drive in win_drive_list:
        for p,d,f in os.walk(drive):
            if search_file in f :  
                print(f"File {search_file} is found at location: {p}")
                break    
elif platform.system() == 'Linux':
    for p, d, f in os.walk("/"):
        if search_file in f:
            print(f"File {search_file} is found at location {p}")
            break    
else:
    pass
    # This can be for Mac code
