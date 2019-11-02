import os
import time
import platform

import AFWConst
import PanConfig
from Utility import *
from AFWUIUtil import *

class Windows:
    def __init__(self, root):
        self.__root = root

    def UploadFile(self, item):
        if not os.path.isfile(item.FullPath):
            print("** It's not file to upload: " + item.FullPath)
            return False
        
        finder = lambda : self.__root.FindWinForm("FormBrowser")
        form  = SafeFind(finder)
        if form is None:
            print("** Failed to find open form")
            return False

        path = item.BasePath
        if platform.system() == "Windows" or platform.system() == "cli":
            path = path.replace("/", "\\")

        # Alt d to input base path
        form.PressKey(AFWConst.AFWKeyAlt)
        form.PressKey(AFWConst.AFWKeyD)
        form.ReleaseKey(AFWConst.AFWKeyD)
        form.ReleaseKey(AFWConst.AFWKeyAlt)
        SimulateTextInput(form, path)
        form.PressKey(AFWConst.AFWKeyEnter)
        form.ReleaseKey(AFWConst.AFWKeyEnter)

        time.sleep(PanConfig.ShortBreakSeconds)

        # Alt n to locate file
        form.PressKey(AFWConst.AFWKeyAlt)
        form.PressKey(AFWConst.AFWKeyN)
        form.ReleaseKey(AFWConst.AFWKeyN)
        form.ReleaseKey(AFWConst.AFWKeyAlt)
        SimulateTextInput(form, item.Name)

        time.sleep(PanConfig.ShortBreakSeconds)

        # Alt O to confirm
        form.PressKey(AFWConst.AFWKeyAlt)
        form.PressKey(AFWConst.AFWKeyO)
        form.ReleaseKey(AFWConst.AFWKeyO)
        form.ReleaseKey(AFWConst.AFWKeyAlt)

        return True        
