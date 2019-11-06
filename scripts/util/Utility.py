import os
import time
import PanConfig

def JoinPath(basePath, path):
    # This is to resolve the windows and linux path different format issue
    return os.path.join(basePath, path).replace("\\", "/")

def SafeFind(finder):
    for i in range(0, PanConfig.FindRetryTimes):
        try:
            result = finder()
            if result is not None:
                return result
        except:
            pass
        time.sleep(PanConfig.ShortBreakSeconds)
    return None

def SafeListFind(finder):
    result = []
    for i in range(0, PanConfig.FindRetryTimes):
        try:
            result = finder()
            if len(result) > 0:
                return result
        except:
            pass
        time.sleep(PanConfig.ShortBreakSeconds)
    return result

def IsUIVisible(ui):
    style = ui.GetAttribute("style")
    if style.find("display: block") >= 0:
        return True
    elif style.find("display: none") >= 0:
        return False
    return True

