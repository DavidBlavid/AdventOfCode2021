import numpy as np


valueDict = {

    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137),
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4

}
counter1 = 0
counter2List = []

for ln in open('Day 10/input.txt').readlines():

    stack = []
    corrupted = False
    counter2 = 0
    
    for c in ln[:-1]:

        if c in ('(', '[', '{', '<'):   # push to stack
            stack.append(c)

        else:
            if valueDict[c][0] == stack[-1]:
                del stack[-1]           # remove from stack
            else:
                counter1 += valueDict[c][1]
                #print(' -> ', c, valueDict[c])
                corrupted = True
                break
        
    if stack != [] and not corrupted: # incomplete line
        for s in stack[::-1]:
            counter2 = counter2 * 5 + valueDict[s]
        counter2List.append(counter2)


print(counter1)
print(np.median(counter2List))