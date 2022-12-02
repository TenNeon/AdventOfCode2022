# https://adventofcode.com/2022/day/1

lines = "test"
singleInput = True
singleDebugInput = True

def lines_to_elves():
    elves = []
    elf = []
    
    for i in range(0, len(lines)):
        line = lines[i]
        
        if line != '\n':
            elf.append(int(line))
            
        if line == '\n' or i == len(lines)-1: 
            elves.append(elf)
            elf = []
    return elves
            
# 72070
def A():
    print("A")
    elves = lines_to_elves();

    largest = 0
    for i in elves:
        elf = i
        sum = 0
        for j in elf:
            sum+=j
        largest = largest if largest >= sum else sum
        
    print(largest)

#211805
def B():
    print("B")
    elves = lines_to_elves();

    sums = []
    
    for i in elves:
        elf = i
        sum = 0
        for j in elf:
            sum+=j
        sums.append(sum)
    
    sums.sort(reverse=True)
    
    print(sums[0] + sums[1] + sums[2])