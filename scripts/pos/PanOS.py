import sys
import collections

from MainPage import *
from Console import *
from File import *
from Item import *
from Utility import *

class PanOS:
    def __init__(self, browser, windows):
        self.__windows = windows
        self.__page = MainPage(browser, windows)
        
        self.__console = Console(self)
        self.__file = File()
        self.__outputs = []
        self.__matchQueue = collections.deque()
        
        self.__finished = False
        
    def Run(self):
        lastCmd = None
        while not self.__finished:
            cmd = None
            if lastCmd == None:
                cmd = self.__console.GetCommand()
            else:
                cmd = lastCmd
            if cmd == None:
                continue
            lastCmd = cmd
            try:
                cmd()
            except:
                print("** Reset on exception")
                self.__reset()
            else:
                lastCmd = None
        
    def ExeCheck(self, srcDir, pageDir):
        self.__clearStack()
        if not self.__file.ValidateDir(srcDir) or not self.__page.GotoDir(pageDir):
            return
        self.__doCheck(srcDir, pageDir)
        self.__printResult()

    def ExeSync(self, srcDir, pageDir):
        self.__clearStack()
        if not self.__file.ValidateDir(srcDir) or not self.__page.GotoDir(pageDir):
            return
        self.__doSync(srcDir, pageDir)
        self.__generateSyncReport(srcDir, pageDir)
        self.__printResult()

    def ExePrint(self, outputPath):
        try:
            with open(outputPath, "w") as log:
                for line in self.__outputs:
                    log.write(line + "\n")
        except:
            print("Failed to print: " + outputPath)
            return
        print("Successfully print to: " + outputPath)

    def ExeQuit(self):
        self.__finished = True

    def __doCompare(self, srcDir, pageDir):
        srcItems = self.__file.ListDir(srcDir)
        pageItems = self.__page.ListDir(pageDir)
        missedItems = []
        matchedItems = []
        redundancy = []
        for srcItem in srcItems:
            matchedPageItem = self.__matchItem(srcItem, pageItems)
            if matchedPageItem is None:
                missedItems.append(srcItem)
            else:
                matchedItems.append([srcItem, matchedPageItem])
                self.__matchQueue.append([srcItem, matchedPageItem])
        for item in pageItems:
            if not item.IsChecked:
                redundancy.append(item)
            else:
                # Clear flag
                item.IsChecked = False
        return missedItems, matchedItems, redundancy
                
    def __doSync(self, srcDir, pageDir):
        missedItems, matchedItems, redundancy = self.__doCompare(srcDir, pageDir)
        for missedItem in missedItems:
            self.__copyToPage(missedItem, pageDir)
        for redund in redundancy:
            self.__deleteFromPage(redund)
        for matchedItem in matchedItems:
            if matchedItem[0].IsDir:
                self.__doSync(matchedItem[0].FullPath, matchedItem[1].FullPath)
        
    def __doCheck(self, srcDir, pageDir):
        missedItems, matchedItems, redundancy = self.__doCompare(srcDir, pageDir)
        self.__generateCheckReport(srcDir, pageDir, missedItems, matchedItems, redundancy)
        nextCheck = None
        while len(self.__matchQueue) > 0:
            pair = self.__matchQueue.popleft()
            if pair[0].IsDir:
                nextCheck = pair
                break
        if nextCheck is not None:
            self.__doCheck(nextCheck[0].FullPath, nextCheck[1].FullPath)
                
    def __matchItem(self, target, pageItems):
        for item in pageItems:
            if target.Name == item.Name and target.IsDir == item.IsDir:
                item.IsChecked = True 
                return item
        return None

    def __clearStack(self):
        self.__outputs = []
        self.__matchQueue = collections.deque()

    def __generateCheckReport(self, src, page, missed, matched, redundancy):
        self.__outputs.append("....")
        self.__outputs.append("[" + src + " <---> " + page + "]")
        self.__outputs.append("Matched: " + str(len(matched)))
        self.__outputs.append("Missed in Page: " + str(len(missed)))
        self.__outputs.append("Redundancy in Page: " + str(len(redundancy)))
        
        indent = "    "
        if len(missed) > 0:
            self.__outputs.append("")
            self.__outputs.append("Missed Details:")
            self.__outputItems(indent, missed)
        if len(redundancy) > 0:
            self.__outputs.append("")
            self.__outputs.append("Redundancy Details:")
            self.__outputItems(indent, redundancy)
        self.__outputs.append("")        

    def __generateSyncReport(self, srcDir, pageDir):
        copied = []
        deleted = []
        for log in self.__outputs:
            if re.match("^\\[Copy\\]", log):
                copied.append(log)
            elif re.match("^\\[Delete\\]", log):
                deleted.append(log)
        self.__clearStack()
        self.__outputs.append("....")
        self.__outputs.append("[" + srcDir + " ----> " + pageDir + "]")
        self.__outputs.append("Copied: " + str(len(copied)))
        self.__outputs.append("Deleted: " + str(len(deleted)))
        
        indent = "    "
        if len(copied) > 0:
            self.__outputs.append("")
            self.__outputs.append("Copy Details:")
            for copyLog in copied:
                self.__outputs.append(copyLog.replace("[Copy]", indent))
        if len(deleted) > 0:
            self.__outputs.append("")
            self.__outputs.append("Delete Details:")
            for deleteLog in deleted:
                self.__outputs.append(deleteLog.replace("[Delete]", indent))
        self.__outputs.append("")        

    def __outputItems(self, indent, items):
        for item in items:
            flag = "[D]" if item.IsDir else "[F]"
            self.__outputs.append(indent + flag + item.FullPath)
        
    def __printResult(self):
        for line in self.__outputs:
            print(line)

    def __copyToPage(self, srcItem, pageDir):
        if not self.__page.Copy(srcItem, pageDir):
            return
        pagePath = JoinPath(pageDir, srcItem.Name)
        self.__outputs.append("[Copy] " + srcItem.FullPath + " -> " + pagePath)
        if srcItem.IsDir:
            self.__doSync(srcItem.FullPath, pagePath)

    def __deleteFromPage(self, pageItem):
        if self.__page.Delete(pageItem):
            self.__outputs.append("[Delete] " + pageItem.FullPath)

    def __reset(self):
        self.__windows.Reset()
        self.__page.Reset()
