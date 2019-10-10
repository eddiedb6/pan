import sys
import os

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/login"))

from Login import *
import PanConfig

import time

username = PanConfig.username
password = PanConfig.password

browser = afw.OpenWebBrowser("Browser")
time.sleep(2)

if Login(browser, username, password):
    pass
else:
    print("Log in failed!")    

form = afw.FindWinForm("FormBrowser");
if form != None:
    print("Find!")
else:
    print("Not Find!")

print("Wait user to quit")
sys.stdin.read(1)

browser.Quit()
