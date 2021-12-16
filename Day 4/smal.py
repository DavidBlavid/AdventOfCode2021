import numpy as np

class Board:                            # objects represent one board
    def __init__(self, board):
        self.b, self.c = board, np.ones((5, 5))

    def m(self, n):                     # mark n and return true if bingo
        if n in self.b:                 # mark if number in board
            self.c[np.where(self.b == n)] = 0

        return (0 in self.c.sum(0) or 0 in self.c.sum(1))

with open('Day 4/input.txt') as f:      # get input

    dl = f.readline()[:-1].split(',')   # get drawn numbers
    nf, br, bl = True, [], []           # first found, b removed, b list

    for p, l in enumerate(f):           # create objects for boards
        if p % 6 == 0:                  # save current board
            if p != 0: bl.append(Board(nb))
            nb = np.zeros((5, 5))   
        else:                           # input values in board
            nb[(p % 6) - 1] = [int(l[i:i+2]) for i in range(0, 14, 3)]

for i in dl:                            # go through all drawn numbers
    for b in bl:                        # go through all boards
        if b.m(int(i)):                 # mark and check for bingo
            
            if nf or len(bl) == 1:      # is first or last board?
                print(sum(sum(b.b * b.c)) * int(i))
                nf = False
            br.append(b)                # mark to be removed

    bl = [b for b in bl if b not in br] # remove board if had bingo
