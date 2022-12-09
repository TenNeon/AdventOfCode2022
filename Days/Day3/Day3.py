# https://adventofcode.com/2022/day/3

# run(1,1,True)

#load util
import sys
sys.path.append('../../')
from aocutil import debugPrint as debug
from aocutil import toCountDict

singleInput = True
singleDebugInput = True
lines = "test"

import math

def charToPriority(char):
    num = ord(char)
    isUpper = num < 97
    debug(str(num) + " IS UPPER" if isUpper else "is lower")
    num = ((num-64)+26) if isUpper else num-96
    return num

def findCommonChar(line):
    compartmentSize = math.floor(len(line) / 2)
    debug(compartmentSize)

    left = line[0:compartmentSize]
    right = line[compartmentSize:]
    
    count_a = toCountDict(left)
    count_b = toCountDict(right)
    
    keys_a = count_a.keys()
    keys_b = count_b.keys()
    
    ab = toCountDict(list(keys_a) + list(keys_b))
    keys_ab = ab.keys()
    
    match = ''
    for key in keys_ab:
        if ab[key] == 2:
            match = key
            break
    
    
    debug("common char: " + match)
    
    matchNum = charToPriority(match)
    
    debug("value: " + str(matchNum))
    return matchNum
    
def findCommonChar3(i,j,k):
    count_a = toCountDict(i.strip("\n"))
    count_b = toCountDict(j.strip("\n"))
    count_c = toCountDict(k.strip("\n"))

    keys = list(count_a.keys())
    keys += list(count_b.keys())
    keys += list(count_c.keys())

    count_abc = toCountDict(keys)
    keys_abc = count_abc.keys()
    
    match = ''
    for key in keys_abc:
        if count_abc[key] == 3:
            match = key
            break
    
    
    debug(match)
    return charToPriority(match)
    
#7903
def A():
    print("A")
    sum = 0
    for line in (lines):
        sum+=findCommonChar(line)
        
    print("sum: " + str(sum))
    
#2548 
def B():
    print("B")
    
    i = 0
    sum = 0
    while i < len(lines):
        sum+=findCommonChar3(lines[i],lines[i+1],lines[i+2])
        i += 3
        
    print("sum: " + str(sum))