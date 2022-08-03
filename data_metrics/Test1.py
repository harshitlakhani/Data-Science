#count total files
import os
def count_files():


	file_count = sum(len(files) for _, _, files in os.walk(r'C:\Sharad\Dalhousie\Study\Semester 3\Courses\DATA SCIENCE\Project\Dataset'))
	
	print("total file count : ",file_count)


count_files()