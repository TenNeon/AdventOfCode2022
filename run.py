import importlib as imp
import importlib.machinery
import importlib.util

import shutil
import os

import aocutil as util

# imp.reload(foo)

day_module = ""

def run(day = 1, test = 3, debug = False):
    global day_module
    util.isDebug = debug

    print("Running day {} ({}) {}".format(day, test, "(debug)" if (debug) else "" ))
    name = "Days/Day{}/Day{}.py".format(day,day) 
    
    # Import day module
    loader = imp.machinery.SourceFileLoader( 'day_module', name )
    spec = imp.util.spec_from_loader( 'day_module', loader )
    day_module = imp.util.module_from_spec( spec )
    loader.exec_module( day_module )
    
    if (test == 3):
        runTest(day,1,debug)
        runTest(day,2,debug)
    else:
        runTest(day,test,debug)

def runTest(daynum,testnum,debug):
    global day_module
    ab = "A" if testnum==1 or day_module.singleInput else "B"
    ab_debug = "A" if testnum==1 or day_module.singleDebugInput else "B"
    isDebug = "_debug" if debug else ""

    inputFileName = "Days\Day{}\Input\{}{}.txt".format(daynum,ab_debug if isDebug else ab,isDebug)
    print(inputFileName)

    with open(inputFileName) as f:
        day_module.lines = f.readlines()
    
    day_module.A() if testnum==1 else day_module.B()
    
def addDay(daynum, overwrite = False):
    daystr = "Days\Day{}".format(daynum)
    exists = os.path.exists(daystr)

    if exists and not overwrite:
        print("Directory already exists. Use addDay(daynum,True) to overwrite")
    else:
        shutil.copytree("Days/Day_template", daystr, False, None, shutil.copy2, False, True)
        oldfilename = "Days\Day{}\Day0.py".format(daynum)
        newfilename = "Days\Day{}\Day{}.py".format(daynum,daynum)
        
        if os.path.exists(newfilename):
            os.remove(newfilename) 
        os.rename(oldfilename,newfilename)
        
        print(os.listdir("Days\Day{}".format(daynum)))
        os.startfile(newfilename)
        
        print("Added Day{}".format(daynum))
    
    
    
    