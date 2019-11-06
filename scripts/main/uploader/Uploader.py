import re
import datetime
import time

from Utility import *
import PanConfig

class Uploader:
    def __init__(self, page):
        self.__uploader = page.FindSubUI("Uploader")

        self.__header = page.FindSubUI("UploaderHeader")
        self.__headerText = self.__header.FindSubUI("UploaderHeaderText")
        self.__headerClose = self.__header.FindSubUI("UploaderHeaderClose")

        self.__minHeader = page.FindSubUI("UploaderMinHeader")
        self.__minHeaderText = self.__minHeader.FindSubUI("UploaderMinHeaderText")
        self.__minHeaderClose = self.__minHeader.FindSubUI("UploaderMinHeaderClose")

    def Dump(self):
        self.__uploader.Dump()

    def Close(self):
        if not IsUIVisible(self.__uploader):
            return
        closeUI = None
        if IsUIVisible(self.__header):
            closeUI = self.__headerClose
        elif IsUIVisible(self.__minHeader):
            closeUI = self.__minHeaderClose
        else:
            return
        closeUI.Click()

    def GetUploadingFileNumber(self):
        if not IsUIVisible(self.__uploader):
            return 0
        textUI = None
        if IsUIVisible(self.__header):
            textUI = self.__headerText
        elif IsUIVisible(self.__minHeader):
            textUI = self.__minHeaderText
        else:
            return 0
        text = textUI.GetText()
        match = re.search("\((\d+)/(\d+)\)", text)
        if not match:
            return 0
        totalNum = int(match.group(2))
        doneNum = int(match.group(1))
        if totalNum > PanConfig.UploadingAbility:
            self.Close()
        return totalNum - doneNum
        
    def GetUploadAbilityCount(self):
        inQueueNum = self.GetUploadingFileNumber()
        result = PanConfig.UploadingAbility - inQueueNum
        if result < 0:
            result = 0
        return result

    def WaitUploadingQueueAvailable(self):
        startTime = datetime.datetime.now()
        while True:
            if self.GetUploadAbilityCount() > 0:
                return True
            nowTime = datetime.datetime.now()
            if (nowTime - startTime).seconds > PanConfig.UploadingMaxWaitingSeconds:
                break
            time.sleep(PanConfig.UploadingCheckInterval)
        return False

    def WaitUploadingQueueFinished(self):
        startTime = datetime.datetime.now()
        while True:
            if IsUIVisible(self.__uploader):
                if IsUIVisible(self.__minHeader):
                    return True
            else:
                return True
            nowTime = datetime.datetime.now()
            if (nowTime - startTime).seconds > PanConfig.UploadingMaxWaitingSeconds:
                print("** Too long to wait for upload queue finished!")
                startTime = datetime.datetime.now()
            time.sleep(PanConfig.UploadingCheckInterval)
        return False
