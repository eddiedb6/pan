import sys
import os
import collections

import PanConfig

class Console:
    def __init__(self, os):
        self.__os = os
        self.__scriptCmds = collections.deque()

    def GetCommand(self):
        cmdCheck = "check"
        cmdSync = "sync"
        cmdPrint = "print"
        cmdQuit = "quit"
        cmdExit = "exit"
        cmdLoad = "load"

        while True:
            print("----------------")
            print(">> Usange: " + cmdCheck + ", " + cmdSync + ", " + cmdPrint + ", " + cmdLoad + ", " + cmdQuit + "|" + cmdExit)

            input = None
            if len(self.__scriptCmds) > 0:
                input = self.__scriptCmds.popleft()
                print("<< " + input)
            else:
                input = sys.stdin.readline().strip()
            cmds = self.__preHandleCmd(input)

            cmdLen = len(cmds)
            if cmdLen <= 0:
                self.__printUsage()
                continue

            cmd = cmds[0]
            if (cmd == cmdCheck) and (cmdLen == 3):
                return lambda: self.__os.ExeCheck(cmds[1], cmds[2])
            if (cmd == cmdSync) and (cmdLen == 3):
                return lambda: self.__os.ExeSync(cmds[1], cmds[2])
            if (cmd == cmdPrint) and (cmdLen == 2):
                return lambda: self.__os.ExePrint(cmds[1])
            if (cmd == cmdLoad) and (cmdLen == 2):
                self.__loadCmdScript(cmds[1])
                continue
            if (cmd == cmdQuit) or (cmd == cmdExit):
                if cmdLen == 1:
                    return lambda: self.__os.ExeQuit()

            self.__printUsage()
            
        return None

    def __printUsage(self):
        print(">> Usage:")
        print("    check SRC_DIR PAN_DIR")
        print("    sync SRC_DIR PAN_DIR")
        print("    print OUTPUT_PATH")
        print("    load CMD_SCRIPT_PATH")
        print("    quit|exit")

    def __preHandleCmd(self, cmdStr):
        # To remove white space in path
        isInQuote = False
        handledStr = ""
        for c in cmdStr:
            if c == '\"':
                isInQuote = not isInQuote
                continue
            if c == " " and isInQuote:
                handledStr += "%20"
            else:
                handledStr += c
        cmds = handledStr.split(" ")
        result = []
        for cmd in cmds:
            result.append(cmd.strip().replace("%20", " "))
        return result

    def __loadCmdScript(self, scriptPath):
        if not os.path.isfile(scriptPath):
            print("** Invalid cmd script path: " + scriptPath)
            return
        try:
            with open(scriptPath, "r") as cmds:
                while True:
                    cmd = cmds.readline()
                    if not cmd:
                        break
                    self.__scriptCmds.append(cmd.strip())
        except:
            print("** Failed to handle cmd script: " + scriptPath)
