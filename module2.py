"""
creating a folder at a specified location

# input includes the destination path along with the folder name
# if the folder already exists at the specified location, display that it already exists
# if it does not exist, create a folder there
"""

import shutil,os

print("Enter the path with using double quotes \"\"")
destination = input()
print("Enter folder name using double quotes \"\"")
folder_name = input()

final_path = os.path.join(os.path.sep,destination,folder_name)

if not os.path.exists(final_path):
    os.mkdir(final_path)
    print("Folder created")
else:
    print("Already exists")