
# import required module
import os
# assign directory
directory = 'C:\Sharad\Dalhousie\Study\Semester 3\Courses\DATA SCIENCE\Project\Dataset'


# iterate over files in
# that directory
def loop_File(file_dir):
    for filename in os.listdir(file_dir):
        # print(filename)
        f = os.path.join(file_dir, filename)
        print(f)
        
        # checking if it is a file
        if os.path.isfile(f):
            if(filename=='0.txt' or filename=='1.txt' or filename=='2.txt' or filename=='commitKeyMap.txt' or filename=='logOneLine.txt'):
                print(f)
            else:
                os.remove(f)
            
        else:
            loop_File(f)

loop_File(directory)