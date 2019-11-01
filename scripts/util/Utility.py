import os
import time
import PanConfig

def JoinPath(basePath, path):
    # This is to resolve the windows and linux path different format issue
    return os.path.join(basePath, path).replace("\\", "/")

def SafeFind(finder):
    for i in range(0, PanConfig.FindRetryTimes):
        time.sleep(PanConfig.ShortBreakSeconds)
        try:
            result = finder()
            if result is not None:
                return result
        except:
            continue
    return None

def SafeListFind(finder):
    result = []
    for i in range(0, PanConfig.FindRetryTimes):
        time.sleep(PanConfig.ShortBreakSeconds)
        try:
            result = finder()
            if len(result) > 0:
                return result
        except:
            continue
    return result

