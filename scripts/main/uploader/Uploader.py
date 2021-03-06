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

        # First wait current upload finished
        if not self.__waitLoop(lambda: True if IsUIVisible(self.__minHeader) else False):
            raise Exception("Close uploader failed")

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
        return self.__waitLoop(lambda: True if self.GetUploadAbilityCount() > 0 else False)

    def WaitUploadingQueueFinished(self):
        return self.__waitLoop(lambda: False if IsUIVisible(self.__uploader) and not IsUIVisible(self.__minHeader) else True)

    def __waitLoop(self, checker):
        startTime = datetime.datetime.now()
        while True:
            if checker():
                return True
            nowTime = datetime.datetime.now()
            if (nowTime - startTime).seconds > PanConfig.UploadingMaxWaitingSeconds:
                print("** Uploader Waiting TIMEOUT!")
                break
            time.sleep(PanConfig.UploadingCheckInterval)
        return False
