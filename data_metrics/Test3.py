#count total files
import os
def count_files():


	file_count = sum(len(files) for _, _, files in os.walk(r'C:\Sharad\Dalhousie\Study\Semester 3\Courses\DATA SCIENCE\Project\ICST2022\Dataset\Denchmark_searchspace'))
	
	print("total search space file count : ",file_count)


count_files()