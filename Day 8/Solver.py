import numpy as np

#             0  1  2  3  4  5  6  7  8  9
segmentNum = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
segments = [
    [1, 1, 1, 1, 1, 1, 0], # 0
    [0, 1, 1, 0, 0, 0, 0], # 1
    [1, 1, 0, 1, 1, 0, 1], # 2
    [1, 1, 1, 1, 0, 0, 1], # 3
    [0, 1, 1, 0, 0, 1, 1], # 4
    [1, 0, 1, 1, 0, 1, 1], # 5
    [1, 0, 1, 1, 1, 1, 1], # 6
    [1, 1, 1, 0, 0, 1, 0], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [1, 1, 1, 1, 0, 1, 1]  # 9
    ]

wireDigits = [0] * 10   # save digit rep as wire letters
posToLetter = [0] * 7   # saves letters at position

counter1 = counter2 = 0

def stringDiff(a, b):
    return ''.join([x for x in a if x not in b])        # a without b

def charIn(a, b):
    return set(a).issubset(set(b))                             # a in b?

for l in open('Day 8/input.txt').readlines():
    
    p1, p2 = l[:-1].split(' | ')
    wires = p1.split(' ')
    digits = p2.split(' ')

    for w in wires:
        if len(w) == 2:     # found 1
            wireDigits[1] = w
        elif len(w) == 4:   # found 4
            wireDigits[4] = w
        elif len(w) == 3:   # found 7
            wireDigits[7] = w
        elif len(w) == 7:   # found 8
            wireDigits[8] = w

    posToLetter[0] = stringDiff(wireDigits[7], wireDigits[1])

    posToLetterE = stringDiff(wireDigits[8], wireDigits[1])

    for w in wires:
        if len(w) == 6: # 0, 6, 9
            if charIn(posToLetterE, w): # found 6
                wireDigits[6] = w
                posToLetter[1] = stringDiff(w, posToLetterE)
                posToLetter[2] = stringDiff(wireDigits[1], posToLetter[1])

            if charIn(wireDigits[4], w): # found 9
                wireDigits[9] = w

    for w in wires:
        if len(w) == 6: # 0, 6, 9
            if w not in wireDigits:
                wireDigits[0] = w       # found 0

    for w in wires:
        if len(w) == 5:
            if charIn(wireDigits[7], w):
                wireDigits[3] = w       # found 3

            if charIn(w, wireDigits[9]) and not charIn(wireDigits[7], w):
                wireDigits[5] = w       # found 5

    for w in wires:
        if w not in wireDigits:
            wireDigits[2] = w 

    for p, d in enumerate(digits):

        for i in range(10):

            if set(d) == set(wireDigits[i]):

                counter2 += pow(10, 3-p) * i


        if (len(d) in (segmentNum[1], segmentNum[4], segmentNum[7], segmentNum[8])):
            counter1 += 1

    #print(wires)
    #print(digits)

print(counter1)
print(counter2)
            
print('THE END')
