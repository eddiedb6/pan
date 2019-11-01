import re
import datetime
import time

from Utility import *
import PanConfig

class Uploader:
    def __init__(self, page):
        self.__uploader = page.FindSubUI("Uploader")
        self.__headerText = page.FindSubUI("UploaderHeader")
        self.__minHeaderText = page.FindSubUI("UploaderMinHeader")

    def GetUploadingFileNumber(self):
        if not IsUIVisible(self.__uploader):
            return 0
        textUI = None
        if IsUIVisible(self.__headerText):
            textUI = self.__headerText
        elif IsUIVisible(self.__minHeaderText):
            textUI = self.__minHeaderText
        else:
            return 0
        text = textUI.GetText()
        match = re.search("\((\d+)/(\d+)\)", text)
        if not match:
            return 0
        totalNum = match.group(2)
        doneNum = match.group(1)
        return totalNum - doneNum
        
    def GetUploadAbilityCount(self):
        inQueueNum = self.GetUploadAbilityCount()
        return PanConfig.UploadingAbility - inQueueNum

    def WaitUploadingQueueAvailable(self):
        startTime = datetime.datetime.now()
        while True:
            if self.GetUploadAbilityCount() > 0:
                return
            nowTime = datetime.datetime.now()
            if (nowTime - startTime).seconds > PanConfig.UploadingMaxWaitingSeconds:
                raise("It has been too long to wait for uploading queue")
            time.sleep(PanConfig.UploadingCheckInterval)
        


