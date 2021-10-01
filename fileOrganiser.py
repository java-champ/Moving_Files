import os 
import shutil

# This is the code to give the entry.
path = input("Enter the name of the directory to be sorted:  ")

# This is the code to list the directories that is in the folder which the user typed.
listOfFiles = os.listdir(path)

# This is will go through each and every file in the listOfFiles variable.
for file in listOfFiles:
    name, ext = os.path.splitext(file)

    # This is going to store the extention type.
    ext = ext[1:]

    # This wil go to the next iteration if it is in the directory.
    if ext =='' :
        continue

    # This will move the file to the directory where the name extention already exists.
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    # This will create a new directory if it does not exist.
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)