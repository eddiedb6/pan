# Accept folder name as parameter and rename all pictures dir in it by NamePhoto.py
# Or validate pic names in it
# Usage:
#	python LoopDir.py ABS_PATH_OF_SCRIPT.py FOLDER_NAME

import sys
import os
import re

######################################################
def PrintUsage():
    print("python LoopDir.py ABS_PATH_OF_SCRIPT.py ./FOLDER_NAME")
######################################################

######################################################
def GetWorkingDir(argList):
    if len(argList) < 3:
        print("[Error] Missing photo folder name")
        PrintUsage()
        return ""
    
    workingDir = os.path.join(os.getcwd(), argList[2])
    if not os.path.exists(workingDir):
        print("[Error] photo folder does not exist")
        PrintUsage()
        return ""

    return workingDir
######################################################

######################################################
def GetScriptPath(argList):
    if len(argList) < 3:
        print("[Error] Missing script path")
        PrintUsage()
        return ""
    
    path = argList[1]
    if not os.path.exists(path):
        print("[Error] photo script does not exist")
        PrintUsage()
        return ""

    return path
######################################################

######################################################
def IsPhotoDir(dirName):
    if not re.match("[0-9a-zA-Z_]*", dirName):
        return False
    dirPath = os.path.join(fullPath, dirName)
    if not os.path.isdir(dirPath):
        return False
    return True
######################################################

print("--- Start ---")

# Print arguments
argString = ""
for arg in sys.argv:
    argString += arg + " "
print(argString)

fullPath = GetWorkingDir(sys.argv)
scriptPath = GetScriptPath(sys.argv)

if fullPath != "":
    dirPathList = []
    dirList = os.listdir(fullPath)
    for dir in dirList:
        if IsPhotoDir(dir):
            dirPathList.append(os.path.join(fullPath, dir))
        else:
            print(">>>>>>>>>> Not valid photo dir name: " + dir)
            sys.exit()

    for dirPath in dirPathList:
        os.chdir(fullPath)
        os.system("python " + scriptPath + " " + os.path.basename(dirPath))

print("--- End ---")     
