import os
import platform
import time

# platform independent code to clear screen
print(f"The system is: {platform.system()}")
time.sleep(5)

if platform.system() == 'Windows':
    os.system("cls")
elif platform.system() == 'Linux':
    os.system("clear")
else:
    # We can add macbook code here
    pass

