import sys
import os
import time

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/login"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/main"))

from LoginPage import *
from MainPage import *
import PanConfig

import time

username = PanConfig.username
password = PanConfig.password

browser = afw.OpenWebBrowser("Browser")

loginPage = LoginPage(browser)

if loginPage.Login(username, password):
    pass
else:
    print("Log in failed!")

mainPage = MainPage(browser)

uploadButton = mainPage.GetUploadFileButton()
allFileButton = mainPage.GetAllFileButton()

mainPage.OpenAlbum()
time.sleep(3)
allFileButton.Click()
time.sleep(3)
mainPage.OpenAlbum()
time.sleep(3)
uploadButton.Click()

#form = afw.FindWinForm("FormBrowser");
#if form != None:
#    print("Find!")
#else:
#    print("Not Find!")

print("Wait user to quit")
sys.stdin.read(1)

browser.Quit()
