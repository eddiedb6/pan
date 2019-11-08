# Accept folder name as parameter and validate all picture names in it based on folder name
# Usage:
#	python ValidateName.py FOLDER_NAME
#

import sys
import os
import time
import re

######################################################
def PrintUsage():
    print("python ValidateName.py FOLDER_NAME")
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
def ValidateName(photoList):
    photoNumbers = len(photoList)
    index = 0
    validCount = 0
    for photo in photoList:
        index += 1
        photoPath = os.path.join(fullPath, subDir, photo)
        if not IsPhoto(photoPath):
            print(">>>>>>>>>>> Not a photo: " + photoPath)
            continue
        regStr = "^" + dirName + "_" + subDir + "_(\d\d\d\d)$"
        targetStr = photo.split(".")[0]
        match = re.search(regStr, targetStr)
        if not match:
            print("----------> Not valid photo name: " + photo)
            continue
        photoIndex = int(match.group(1))
        if photoIndex != index and photoIndex + index != photoNumbers + 1:
            print("..........> Invalid index: " + str(photoIndex) + ", should be " + str(index) + " or " + str(photoNumbers + 1 - index))
            continue
        validCount += 1
    if validCount == photoNumbers:
        print("  All valid in " + str(photoNumbers) + " for " + subDir)
    else:
        print("  " + str(photoNumbers - validCount)  + " not valid in " + str(photoNumbers) + " for " + subDir)
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
        ValidateName(photoList)

print("--- End ---")     
