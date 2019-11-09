import re
import datetime
import time

from Utility import *
import PanConfig

class Splash:
    def __init__(self, page):
        self.__splash = page.FindSubUI("Splash")
        self.__splashClose = self.__splash.FindSubUI("SplashClose")

    def Dump(self):
        self.__splash.Dump()

    def Close(self):
        if IsUIVisible(self.__splash):
            self.__splashClose.Click()
