"""
moving file from one location to another
"""

import shutil

print("Enter the path with using double quotes \"\"")
source = input()
destination = input()
shutil.move(source,destination)