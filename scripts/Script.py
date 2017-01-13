import sys
import os

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))

from ScriptLogin import *
import PanConfig

username = PanConfig.username
password = PanConfig.password

browser = afw.OpenWebBrowser("Browser")
if not Login(browser, username, password):
    sys.exit("Login failed!")

welcomeButton = browser.TryToFindSubUI("ButtonWelcome")
if welcomeButton is not None:
    print "Find welcome screen"
    welcomeButton.Click()
else:
    print "No welcome found!"
    
