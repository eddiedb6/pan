import sys
import os
import logging

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "./auto"))

from afw.AFW import AFW

auto = AFW()
auto.LogLevel = logging.DEBUG
auto.BreakTime = 100 # ms

if auto.Load(os.path.join(os.path.split(os.path.realpath(__file__))[0], "scripts/Config.py")):
    auto.Execute()

auto.Destroy()

