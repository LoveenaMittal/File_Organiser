"""
script that organises a folder
currently I have organised for pdf files and images
input is the path of folder that needs to be organised
"""

import shutil,os

print("Enter the path with using double quotes \"\"")
path = input()

for filename in os.listdir( path ):
	file_path = os.path.join(os.path.sep,path,filename)
	if filename.endswith(".pdf"):
		folder_path_PDF = os.path.join(os.path.sep,path,"PDF")
		if not os.path.exists(folder_path_PDF):
			os.mkdir(folder_path_PDF)
		shutil.move(file_path,folder_path_PDF)
	elif filename.endswith(".jpg") or filename.endswith(".png"):
		folder_path_images = os.path.join(os.path.sep,path,"IMAGES")
		if not os.path.exists(folder_path_images):
			os.mkdir(folder_path_images)
		shutil.move(file_path,folder_path_images)
		
		
		