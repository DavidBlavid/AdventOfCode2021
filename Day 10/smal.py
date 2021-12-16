import numpy as np

vDict = {
    ')': ('(', 3),    ']': ('[', 57),
    '}': ('{', 1197), '>': ('<', 25137),
    '(': 1, '[': 2, '{': 3, '<': 4
}
c1, c2List = 0, []

for ln in open('Day 10/input.txt').readlines():
    stack = []
    corrupted = c2 = False
    
    for ch in ln[:-1]:
        if ch in ('(', '[', '{', '<'):
            stack += [ch]       # push to stack

        elif vDict[ch][0] == stack[-1]:
            del stack[-1]       # pop from stack
            
        else:
            c1 += vDict[ch][1]  # found corrupted line
            corrupted = True
            break
        
    if not corrupted:
        for s in stack[::-1]: c2 = c2 * 5 + vDict[s]
        c2List.append(c2)       # complete lines

print(c1)
print(np.median(c2List))