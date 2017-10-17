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
if Login(browser, username, password):
    pass
else:
    print("Log in failed!")    

#browser.Quit()
