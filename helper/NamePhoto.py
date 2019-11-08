# Accept folder name as parameter and rename all pictures in it based on folder name
# Usage:
#	python NamePhoto.py FOLDER_NAME
# 1. This will rename all photos in folder
# 2. Then use baidu pan to archive the whole folder
# 3. All above should be run on downloading PC

import sys
import os
import time
import re

######################################################
def PrintUsage():
    print("python NamePhoto.py FOLDER_NAME")
######################################################

######################################################
def GetWorkingDir(argList):
    if len(argList) < 2:
        print("[Error] Missing photo folder name")
        PrintUsage()
        return ""
    
    workingDir = os.path.join(os.getcwd(), argList[1])
    if not os.path.exists(workingDir):
        print("[Error] photo folder does not exist")
        PrintUsage()
        return ""

    return workingDir
######################################################

#########################################################
photoExtention = [".jpg", ".png", ".mp4", ".mov", ".avi", ".jpeg"]
def IsPhoto(photoPath):
    for ext in photoExtention:
        if os.path.splitext(photoPath)[1].lower() == ext:
            return True
    return False
#########################################################

#########################################################
def IsPhotoDir(dirName):
    if not re.match("^\d+_\d+$", dirName):
        return False
    dirPath = os.path.join(fullPath, dirName)
    if not os.path.isdir(dirPath):
        return False
    return True
#########################################################

#########################################################
def GetNewName(originalName, index):
    newName = os.path.join(fullPath, subDir, dirName + "_" + subDir + "_{0:04}".format(index) + os.path.splitext(originalName)[1].lower())
    return newName
#########################################################

#########################################################
def RenamePhotoes(photoList):
    photoMap = {}
    photoPriority = []
    for photo in photoList:
        photoPath = os.path.join(fullPath, subDir, photo)
        # use mtime but not ctime, mtime is the first time to create
        photoDate = os.path.getmtime(photoPath)
        if not IsPhoto(photoPath):
            print(">>>>>>>>>>> Not a photo: " + photoPath)
            continue
        photoPriority.append(photoDate)
        if photoDate not in photoMap:
            photoMap[photoDate] = []
        photoMap[photoDate].append(photo)
    photoPrioritySet = set(photoPriority)
    photoPrioritySort = list(photoPrioritySet)
    photoPrioritySort.sort()

    count = 0
    for key in photoPrioritySort:
        #print(str(key) + " " + time.ctime(key))
        for value in photoMap[key]:
            count += 1 
            originalPath = os.path.join(fullPath, subDir, value)
            newPath = GetNewName(value, count)
            print("Rename [" + originalPath + "] to [" + newPath + "]")
            os.rename(originalPath, newPath)
#########################################################

print("--- Start ---")

# Print arguments
argString = ""
for arg in sys.argv:
    argString += arg + " "
print(argString)

fullPath = GetWorkingDir(sys.argv)
if fullPath != "":
    dirName = os.path.basename(fullPath)
    subDir = ""
    dirPathList = []
    dirList = os.listdir(fullPath)
    for dir in dirList:
        if IsPhotoDir(dir):
            dirPathList.append(os.path.join(fullPath, dir))
        else:
            print(">>>>>>>>>> Not valid sub dir name: " + dir)
            sys.exit()

    for dirPath in dirPathList:
        photoList = os.listdir(dirPath)
        subDir = os.path.basename(dirPath)
        RenamePhotoes(photoList)

print("--- End ---")     
