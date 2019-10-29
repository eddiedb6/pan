import os

import AFWConst
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

        # Alt d to input base path
        form.PressKey(AFWConst.AFWKeyAlt)
        form.PressKey(AFWConst.AFWKeyD)
        form.ReleaseKey(AFWConst.AFWKeyD)
        form.ReleaseKey(AFWConst.AFWKeyAlt)
        SimulateTextInput(form, item.BasePath)
        form.PressKey(AFWConst.AFWKeyEnter)
        form.ReleaseKey(AFWConst.AFWKeyEnter)
        
        # Alt n to locate file
        form.PressKey(AFWConst.AFWKeyAlt)
        form.PressKey(AFWConst.AFWKeyN)
        form.ReleaseKey(AFWConst.AFWKeyN)
        form.ReleaseKey(AFWConst.AFWKeyAlt)
        SimulateTextInput(form, item.Name)
        
        # Alt O to confirm
        form.PressKey(AFWConst.AFWKeyAlt)
        form.PressKey(AFWConst.AFWKeyO)
        form.ReleaseKey(AFWConst.AFWKeyO)
        form.ReleaseKey(AFWConst.AFWKeyAlt)

        return True        
