import sys
import os
import time

# __file__ will be AFW.py in auto/afw
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/login"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/main"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/pos"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/data"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/util"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/win"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/main/uploader"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../scripts/main/splash"))

from LoginPage import *
from MainPage import *
from PanOS import *
from Windows import *
import PanConfig

import time

username = PanConfig.username
password = PanConfig.password

browser = afw.OpenWebBrowser("Browser")
windows = Windows(afw)

print(">> Wait browser to open")
sys.stdin.read(1)

if LoginPage(browser).Login(username, password):
    PanOS(browser, windows).Run()
else:
    print("Log in failed!")

browser.Quit()
