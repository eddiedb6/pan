import sys
import time

class LoginPage:
    def __init__(self, browser):
        if browser is None:
            raise Exception("None browser for LoginPage")
        self.__browser = browser

    ### Properties ###
    def Login(self, username, password):
        if not self.__browser.OpenURL("URLLogin"):
            return False
        time.sleep(2)
        
        loginPage = self.__browser.FindSubUI("PageLogin")
    
        accountLoginLink = loginPage.FindSubUI("PasswordLogin")
        accountLoginLink.Click()

        userNameEditBox = loginPage.FindSubUI("EditUserName")
        passwordEditBox = loginPage.FindSubUI("EditPassword")
        loginButton = loginPage.FindSubUI("ButtonLogin")

        userNameEditBox.Input(username)
        passwordEditBox.Input(password)

        if not loginButton.Click():
            return False

        print("Wait user to login")
        sys.stdin.read(1)

        return True
