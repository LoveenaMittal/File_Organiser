"""
Script that organizes files in a folder
# for PDF file, PDF folder will be created
# for Python files, PYTHON folder will be created and so on.
# in case of Log files such as csv, excel and .log files, files will be organized based on YEAR --> MONTH --> WEEKDAY	
"""


from datetime import datetime
import datetime
import calendar
import os,shutil

"""

# Assumption in case of log files: Name of file starts in format YYYY-MM-DD

"""

"""
# moves a file to proper folder
"""
def move_file(file_path, folder_path):
	shutil.move(file_path,folder_path)
	
"""
# function that looks for path of folder
# if folder does not exist, create the folder
"""

def organize(folder_path):
	if not os.path.exists(folder_path):
		os.mkdir(folder_path)
	

print("Enter the path with using double quotes \"\"")
path = input().strip()

for filename in os.listdir( path ):
	file_path = os.path.join(os.path.sep,path,filename)

#PDF FILES
	if filename.lower().endswith((".pdf")):
		folder_path_PDF = os.path.join(os.path.sep,path,"PDF")
		organize(folder_path_PDF)
		move_file(file_path,folder_path_PDF)
#IMAGE FILES
	elif filename.lower().endswith((".jpg",".png",".JPG")):
		folder_path_images = os.path.join(os.path.sep,path,"IMAGES")
		organize(folder_path_images)
		move_file(file_path,folder_path_images)
#TEXT FILES
	elif filename.lower().endswith((".txt")):
		folder_path_text = os.path.join(os.path.sep,path,"TEXT FILES")
		organize(folder_path_text)
		move_file(file_path,folder_path_text)
#PYTHON FILES
	elif filename.lower().endswith((".py")):
		folder_path_python = os.path.join(os.path.sep,path,"PYTHON FILES")
		organize(folder_path_python)
		move_file(file_path,folder_path_python)
#DOC FILES
	elif filename.lower().endswith((".doc",".docx")):
		folder_path_documents = os.path.join(os.path.sep,path,"DOC FILES")
		organize(folder_path_documents)
		move_file(file_path,folder_path_documents)
#LOGS
	elif filename.lower().endswith((".csv",".xls",".xlsx",".log")):
		main_folder = os.path.join(os.path.sep,path,"LOGS")
		organize(main_folder)
		year,month,day = [int(x) for x in filename[:10].split('-')]
		year_folder = os.path.join(os.path.sep,main_folder,str(year))
		organize(year_folder)
		month_folder = os.path.join(os.path.sep,year_folder,calendar.month_name[month])
		organize(month_folder)
		check = datetime.date(year,month,day)
		weekday = calendar.day_name[check.weekday()]
		weekname_folder = os.path.join(os.path.sep,month_folder,weekday)
		organize(weekname_folder)
		move_file(file_path,weekname_folder)
