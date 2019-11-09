import re
import datetime
import time

from Utility import *
import PanConfig

class Splash:
    def __init__(self, page):
        self.__splash = None
        self.__splashClose = None

        self.__splash = page.TryToFindSubUI("Splash")
        if self.__splash != None:
            self.__splashClose = self.__splash.FindSubUI("SplashClose")

    def Dump(self):
        if self.__splash != None:
            self.__splash.Dump()

    def Close(self):
        if self.__splash != None and IsUIVisible(self.__splash):
            self.__splashClose.Click()
