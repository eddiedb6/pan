def Login(browser, username, password):
    if browser is None:
        return False
    if not browser.OpenURL("URLLogin"):
        return False

    loginPage = browser.FindSubUI("PageLogin")
    
    accountLoginLink = loginPage.FindSubUI("LinkAccountLogin")
    accountLoginLink.Click()

    userNameEditBox = loginPage.FindSubUI("EditUserName")
    passwordEditBox = loginPage.FindSubUI("EditPassword")
    loginButton = loginPage.FindSubUI("ButtonLogin")

    userNameEditBox.InputText(username)
    passwordEditBox.InputText(password)

    return loginButton.Click()

