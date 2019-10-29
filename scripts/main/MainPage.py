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
                AFWConst.AttrClass: "lebNA3e"
            },
            {
                AFWConst.Name: baseName + "Icon",
                AFWConst.Type: AFWConst.UICommon,
                AFWConst.AttrClass: "cduyKEp"
            }]
        }

        lists = self.__area.TryToFindDynamicSubUI(config)

        for i in range(0, len(lists)):
            listItem = lists[i]
            nameUI = listItem.FindSubUI(listItem.GetDynamicUIName(baseName + "Name", i))
            name = nameUI.GetAttribute("title")
            iconUI = listItem.FindSubUI(listItem.GetDynamicUIName(baseName + "Icon", i))
            isDir = True if iconUI.GetAttribute("class") == "cduyKEp dir-small" else False

            item = Item()
            item.Name = name
            item.BasePath = path
            item.FullPath = JoinPath(item.BasePath, name)
            item.IsDir = isDir
            result.append(item)

        return result

    def Copy(self, item, path):
        if not self.GotoDir(path):
            raise Exception("Failed to goto dir for copy: " + path)
        currentPath = self.__getCurrentPath()
        if currentPath != path:
            raise Exception("Current path is not copy path: " + path)
        if item.IsDir:
            return self.__uploadFile(item)
        return self.__createFoler(item)

    def Delete(self, item):
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
        return self.__clickOnFolder(folderItems[0])

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
        return self.__clickOnFolder(self.__fileRoot)

    def __clickOnFolder(self, folder):
        if folder.Click():
            time.sleep(1)
            return True
        return False

    def __uploadFile(self, item):
        self.__waitInUploadQueue()
        if not self.__uploadButton.Click():
            return False
        return self.__windows.UploadFile(item)

    def __createFoler(self, item):
        if not self.__createButton.Click():
            return False
        return self.__inputNewFolderName(item.Name)

    def __waitInUploadQueue(self):
        # TODO
        pass

    def __inputNewFolderName(self, name):
        inputConfig = {
            AFWConst.Name: "NewFolderWrapper",
            AFWConst.Type: AFWConst.UICommon,
            AFWConst.AttrClass: "ExFGye",
            AFWConst.SubUI: [
            {
                AFWConst.Name: "NewFolderInput",
                AFWConst.Type: AFWConst.UIInputable,
                AFWConst.AttrClass: "GadHyA"
            },
            {
                AFWConst.Name: "NewFolderInputConfirm",
                AFWConst.Type: AFWConst.UIClickable,
                AFWConst.AttrClass: "eyymZQ"
            }]
        }

        inputs = self.__page.TryToFindDynamicSubUI(inputConfig)
        if len(inputs) <= 0:
            raise Exception("Could not input new folder name")
        inputWrapper = inputs[0]
        if inputWrapper.GetAttribute("style").find("display: none") < 0:
            return False

        inputBox = inputWrapper.FindSubUI(inputWrapper.GetDynamicUIName("NewFolderInput", 0))
        inputConfirm = inputWrapper.FindSubUI(inputWrapper.GetDynamicUIName("NewFolderInputConfirm", 0))

        if inputBox.Input(name):
            return inputConfirm.Click()

        return False
