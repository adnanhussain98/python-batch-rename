import os

# points to the directory in which I want to rename files.
os.chdir('/Users/adnanhussain/Desktop/Portugal')

# for loop, listdir() lists all files in directory. print (f) prints all files.
# for f in os.listdir():
#     print(f)

# # loops over files in directory and splits file name and file extension
# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     print(file_name)

# new_file_name = variable for new file name
# {} is where the number is stored

# starts from 0
i = 0

# loops through file names in directory
for f in os.listdir():
    # stores new file name in the object, formats by i
    file_new_name = "Porto {}.jpg".format(i)
    # rename function takes 2 parameters, files in directory and changes to file_new_name
    os.rename(f, file_new_name)
    # increments i by 1. e.g. 1, 2, 3, 4..
    i = i + 1
