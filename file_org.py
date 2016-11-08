"""
script that organises a folder
currently I have organised for pdf files and images
input is the path of folder that needs to be organised
"""

import shutil,os

# function that looks for path of folder
# if folder does not exist, create the folder
# and moves the file to the folder

def organize(file_path,folder_path):
	if not os.path.exists(folder_path):
		os.mkdir(folder_path)
	shutil.move(file_path,folder_path)

print("Enter the path with using double quotes \"\"")
path = input().strip()

for filename in os.listdir( path ):
	file_path = os.path.join(os.path.sep,path,filename)

#PDF FILES
	if filename.endswith(".pdf"):
		folder_path_PDF = os.path.join(os.path.sep,path,"PDF")
		organize(file_path,folder_path_PDF)
#IMAGE FILES
	elif filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG"):
		folder_path_images = os.path.join(os.path.sep,path,"IMAGES")
		organize(file_path,folder_path_images)
#TEXT FILES
	elif filename.endswith(".txt"):
		folder_path_text = os.path.join(os.path.sep,path,"TEXT FILES")
		organize(file_path,folder_path_text)
#PYTHON FILES
	elif filename.endswith(".py"):
		folder_path_python = os.path.join(os.path.sep,path,"PYTHON FILES")
		organize(file_path,folder_path_python)
#DOC FILES
	elif filename.endswith(".doc") or filename.endswith(".docx"):
		folder_path_documents = os.path.join(os.path.sep,path,"DOC FILES")
		organize(file_path,folder_path_documents)
		
		
		