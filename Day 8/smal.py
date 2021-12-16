wd = [0] * 10   # save digit rep as wire letters
counter1 = counter2 = 0

def charIn(a, b): return set(a).issubset(set(b))                    # a in b?

for l in open('Day 8/input.txt').readlines():
    p1, p2 = l[:-1].split(' | ')
    wires, digits = p1.split(' '), p2.split(' ')

    for w in wires:
        if   len(w) == 2: wd[1] = w                                 # found 1
        elif len(w) == 4: wd[4] = w                                 # found 4
        elif len(w) == 3: wd[7] = w                                 # found 7
        elif len(w) == 7: wd[8] = w                                 # found 8

    tempE = ''.join([x for x in wd[8] if x not in wd[1]])

    for w in wires * 3:
        if len(w) == 5: # possible: 2, 3, 5
            if charIn(wd[7], w): wd[3] = w                          # found 3
            if charIn(w, wd[9]) and not charIn(wd[7], w): wd[5] = w # found 5
            if wd[3] and wd[5] and w not in wd: wd[2] = w           # found 2

        if len(w) == 6: # possible: 0, 6, 9
            if charIn(tempE, w): wd[6] = w                          # found 6
            if charIn(wd[4], w): wd[9] = w                          # found 9
            if wd[6] and wd[9] and w not in wd: wd[0] = w           # found 0

    for p, d in enumerate(digits):
        for i in range(10):
            if set(d) == set(wd[i]):
                counter1 += i in (1, 4, 7, 8)
                counter2 += i * pow(10, 3 - p)

print(counter1)
print(counter2)