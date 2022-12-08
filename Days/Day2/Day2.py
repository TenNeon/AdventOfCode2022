# https://adventofcode.com/2022/day/2

#load util
import sys
sys.path.append('../../')
from aocutil import debugPrint as debug

singleInput = True
singleDebugInput = True
lines = "test"

#run(2,1,True)


move = {"A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2 }
score = [[4,8,3],[1,5,9],[7,2,6]]
bscore = [[3,4,8],[1,5,9],[2,6,7]]

# returns score from a single round
def scoreRound(line,sc):
    first = line[0]
    second = line[2]

    debug(first + "<>" + second)
    
    return sc[move[first]][move[second]]
#13009
def A():
    print("A")
    
    totalScore = 0
    for i in range(0, len(lines)):
        thisRound = scoreRound(lines[i],score)
        debug(thisRound)
        totalScore += thisRound
        
    print(totalScore)
    
#10398 
def B():
    print("B")
    totalScore = 0
    for i in range(0, len(lines)):
        thisRound = scoreRound(lines[i],bscore)
        debug(thisRound)
        totalScore += thisRound
        
    print(totalScore)