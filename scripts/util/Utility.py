import os

def JoinPath(basePath, path):
    # This is to resolve the windows and linux path different format issue
    return os.path.join(basePath, path).replace("\\", "/")

