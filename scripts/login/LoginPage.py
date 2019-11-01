import sys
import time

import PanConfig
from Utility import *

class LoginPage:
    def __init__(self, browser):
        if browser is None:
            raise Exception("None browser for LoginPage")
        self.__browser = browser

    ### Properties ###
    def Login(self, username, password):
        if not self.__browser.OpenURL("URLLogin"):
            return False

        time.sleep(PanConfig.ShortBreakSeconds)
        
        loginPage =  SafeFind(lambda: self.__browser.FindSubUI("PageLogin"))
    
        accountLoginLink = SafeFind(lambda: loginPage.FindSubUI("PasswordLogin"))
        if accountLoginLink is None:
            return False
        accountLoginLink.Click()

        userNameEditBox = loginPage.FindSubUI("EditUserName")
        passwordEditBox = loginPage.FindSubUI("EditPassword")
        loginButton = loginPage.FindSubUI("ButtonLogin")

        userNameEditBox.Input(username)
        passwordEditBox.Input(password)

        if not loginButton.Click():
            return False

        print(">> Wait user to login")
        sys.stdin.read(1)

        return True
