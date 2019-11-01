import sys

class Console:
    def __init__(self, os):
        self.__os = os

    def GetCommand(self):
        cmdCheck = "check"
        cmdSync = "sync"
        cmdPrint = "print"
        cmdQuit = "quit"
        cmdExit = "exit"

        while True:
            print("----------------")
            print(">> Usange: " + cmdCheck + ", " + cmdSync + ", " + cmdPrint + ", " + cmdQuit + "|" + cmdExit)

            input = sys.stdin.readline().strip()
            cmds = input.split(" ")

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
        print("    quit|exit")
