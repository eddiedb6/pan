import os
import re

import PanConfig

from Item import *

class File:
    def __init__(self):
        pass

    def ValidateDir(self, dir):
        if not os.path.isdir(dir):
            print("** Not valid directory: " + dir)
            return False
        return True

    def ListDir(self, dir):
        results = []
        
        items = os.listdir(dir)
        for item in items:
            if self.__isFileIgnored(item):
                continue
            
            result = Item()
            result.Name = item
            result.BasePath = dir
            result.FullPath = os.path.join(dir, item)
            result.IsDir = os.path.isdir(result.FullPath)
            results.append(result)
            
        return results

    def __isFileIgnored(self, name):
        for rule in PanConfig.FileIgnoreRules:
            if re.match(rule, name):
                return True
        return False
