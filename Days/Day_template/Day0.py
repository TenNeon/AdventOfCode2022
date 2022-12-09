# https://adventofcode.com/2022/day/1
# run(1,1,True)

#load util
import sys
sys.path.append('../../')
from aocutil import debugPrint as debug

singleInput = False
singleDebugInput = True
lines = "test"

def A():
    print("A")
    for i in range(0, len(lines)):
       print(lines[i])
    
def B():
    print("B")
