import os
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
            continue
    return None

