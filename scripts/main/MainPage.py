import os
import time

import AFWConst
import PanConfig
from Item import *
from Utility import *

class MainPage:
    def __init__(self, browser, windows):
        if browser is None:
            raise Exception("None browser for MainPage")
        self.__browser = browser

        if windows is None:
            raise Exception("None windows for MainPage")
        self.__windows = windows

        self.__page = self.__browser.FindSubUI("PageMain")
        self.__uploadButton = self.__page.FindSubUI("ButtonUploadFile")
        self.__createButton = self.__page.FindSubUI("ButtonCreateFolder")
        self.__area = self.__page.FindSubUI("WorkingArea")
        self.__addressStatus = self.__page.FindSubUI("AddressStatus")
        self.__address = self.__addressStatus.FindSubUI("AddressValue")
        self.__fileRoot = self.__page.FindSubUI("EntryAllFile")

    ### Properties ###

    def GotoDir(self, path):
        print(".. Go to: " + path)
        currentPath = self.__getCurrentPath()
        if path == currentPath:
            return True

        if path == "/":
            return self.__gotoRoot()

        basePath = "/"
        relativeDir = path
        if path.find(currentPath) == 0:
            # This means it could go further base on current page
            relativeDir = path[len(currentPath):]
            basePath = currentPath

        folderList = relativeDir.split("/")
        for folder in folderList:
            if folder.strip() == "":
                continue
            if self.__openFolder(basePath, folder.strip()):
                basePath = JoinPath(basePath, folder.strip())
            else:
                print("** Failed to open '" + folder + "' of " + path)
                return False

        return True

    def ListDir(self, path):
        print(".. List: " + path)

        result = []

        if not self.GotoDir(path):
            print("** Failed to list dir because of open: " + path)
            return result;

        baseName = "ListItem"
        config = {
            AFWConst.Name: baseName,
            AFWConst.Type: AFWConst.UICommon,
            AFWConst.AttrTag: "dd",
            AFWConst.Attributes: {
                "_installed": "1"
            },
            AFWConst.SubUI: [
            {
                AFWConst.Name: baseName + "Name",
                AFWConst.Type: AFWConst.UIClickable,
                AFWConst.AttrClass: PanConfig.ClassListItemClickable
            },
            {
                AFWConst.Name: baseName + "Icon",
                AFWConst.Type: AFWConst.UICommon,
                AFWConst.AttrClass: PanConfig.ClassListItemIcon
            }]
        }

        finder = lambda: self.__area.TryToFindDynamicSubUI(config)
        lists = SafeListFind(finder)

        for i in range(0, len(lists)):
            listItem = lists[i]
            nameUI = listItem.FindSubUI(listItem.GetDynamicUIName(baseName + "Name", i))
            name = nameUI.GetAttribute("title")
            iconUI = listItem.FindSubUI(listItem.GetDynamicUIName(baseName + "Icon", i))
            isDir = True if iconUI.GetAttribute("class") == (PanConfig.ClassListItemIcon + " dir-small") else False

            item = Item()
            item.Name = name
            item.BasePath = path
            item.FullPath = JoinPath(item.BasePath, name)
            item.IsDir = isDir
            result.append(item)

        return result

    def Copy(self, item, path):
        print(".. Copy: " + JoinPath(path, item.Name))

        if not self.GotoDir(path):
            raise Exception("Failed to goto dir for copy: " + path)
        currentPath = self.__getCurrentPath()
        if currentPath != path:
            raise Exception("Current path is not copy path: " + path)

        newPath = JoinPath(path, item.Name)
        if item.IsDir:
            print(".. Try to create folder: " + newPath)
            if self.__createFoler(item):
                if self.GotoDir(newPath):
                    print(".. Successfully create folder: " + newPath)
                    return True
            print(".. Failed to create folder: " + newPath)
            return False

        print(".. Try to upload file: " + newPath)
        if self.__uploadFile(item):
            print(".. Successfully upload file: " + newPath)
            return True
        print(".. Failed to upload file: " + newPath)
        return False

    def Delete(self, item):
        print(".. Delete: " + item.FullPath)

        if not PanConfig.IsDeleteRedundant:
            return True
        return False

    def __openFolder(self, basePath, folder):
        while True:
            currentPath = self.__getCurrentPath()
            if currentPath != basePath:
                self.GotoDir(basePath)
            else:
                break

        folderConfig = {
            AFWConst.Name: self.__getDynamicFolderName(folder),
            AFWConst.Type: AFWConst.UIClickable,
            AFWConst.AttrTag: "a",
            AFWConst.Attributes: {
                "title": folder
            }
        }
        folderItems = self.__area.TryToFindDynamicSubUI(folderConfig)
        if len(folderItems) != 1:
            return False
        return self.__executeClick(folderItems[0])

    def __getDynamicFolderName(self, folder):
        return "DynamicFolder" + folder

    def __getCurrentPath(self):
        if self.__addressStatus.GetAttribute("style") != "display: block;":
            # Then it's root, the ul element will be hiden
            return "/"

        addressConfig = {
            AFWConst.Name: "AddressItem",
            AFWConst.Type: AFWConst.UICommon,
            AFWConst.AttrTag: "span",
            AFWConst.Attributes: {
            }
        }
        addressItems = self.__address.TryToFindDynamicSubUI(addressConfig)
        if len(addressItems) <= 0:
            raise Exception("It's impossible that got nothing from address bar")

        # It's format of "XXX/path/subpath/..."
        path = addressItems[len(addressItems) -1].GetAttribute("title")

        return path[path.find("/"):]

    def __gotoRoot(self):
        return self.__executeClick(self.__fileRoot)

    def __executeClick(self, clickable):
        if clickable.Click():
            time.sleep(PanConfig.ShortBreakSeconds)
            return True
        return False

    def __uploadFile(self, item):
        self.__waitInUploadQueue()
        if not self.__executeClick(self.__uploadButton):
            return False
        if not self.__windows.UploadFile(item):
            return False
        time.sleep(PanConfig.LongBreakSeconds)
        return True

    def __createFoler(self, item):
        if not self.__executeClick(self.__createButton):
            return False
        if not self.__inputNewFolderName(item.Name):
            return False
        time.sleep(PanConfig.LongBreakSeconds)
        return True

    def __waitInUploadQueue(self):
        # TODO
        pass

    def __inputNewFolderName(self, name):
        inputWrapper = self.__page.FindSubUI("NewFolderWrapper")
        if inputWrapper.GetAttribute("style").find("display: none") >= 0:
            return False
        inputBox = inputWrapper.FindSubUI("NewFolderInput")
        inputConfirm = inputWrapper.FindSubUI("NewFolderInputConfirm")
        if inputBox.Input(name):
            return self.__executeClick(inputConfirm)
        return False