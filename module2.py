"""
creating a folder at a specified location

# input includes the destination path along with the folder name
# if the folder already exists at the specified location, display that it already exists
# if it does not exist, create a folder there
"""

import shutil

print("Enter the path with using double quotes \"\"")
destination = input()
#folder_name = input()

if not os.path.exists(destination):
    os.mkdir(destination)
    print("Folder created")
else:
    print("Already exists")
