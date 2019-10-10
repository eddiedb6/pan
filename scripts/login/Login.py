import sys

def Login(browser, username, password):
    if browser is None:
        return False
    if not browser.OpenURL("URLLogin"):
        return False

    loginPage = browser.FindSubUI("PageLogin")
    
    accountLoginLink = loginPage.FindSubUI("PasswordLogin")
    accountLoginLink.Click()

    userNameEditBox = loginPage.FindSubUI("EditUserName")
    passwordEditBox = loginPage.FindSubUI("EditPassword")
    loginButton = loginPage.FindSubUI("ButtonLogin")

    userNameEditBox.InputText(username)
    passwordEditBox.InputText(password)

    if not loginButton.Click():
        return False

    print("Wait user to login")
    sys.stdin.read(1)

    return True
