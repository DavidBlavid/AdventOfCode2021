
import numpy as np
from math import sqrt

import matplotlib.pyplot as plt

# for each position
board = []
costs = []
prev = []   # saves node before this node with lowest cost

# open / closed list
open_list = []
closed_list = []

for ln in open('Day 15/input.txt').readlines():

    board.append([int(x) for x in ln[:-1]])


boardLength = len(board)

bigBoard = board.copy()
bigBoard = np.tile(bigBoard, (5, 5))

for y in range(boardLength * 5):
    for x in range(boardLength * 5):
        extra = y // boardLength + x // boardLength
        bigBoard[y, x] += extra
        if bigBoard[y, x] >= 10: bigBoard[y, x] -= 9

board = bigBoard.copy()
boardLength = len(board)

board = np.array(board)
costs = np.array(costs)
prev = np.array(prev)

costs = np.copy(board)
costs.fill(99999)

prev = np.arange(boardLength * boardLength * 2)
prev.shape = (boardLength, boardLength, 2)
prev.fill(-1)

print(prev)
print(prev.shape)



# F = G + H
# F -> Gesamtkosten
# G -> Distanz momentanter Knoten zu Anfang
# H -> Geschätze Distanz zum Ende (Heuristik)

def cost(x, y):

    g = 0

    while not (x == 0 and y == 0):

        if (x, y) in closed_list:
            g += costs[y, x]
            break

        g += board[y, x]
        x, y = prev[y, x]

    return g

neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)] #ruld

currentPosition = (0, 0)

while True:

    minVal = 9999999

    for o in open_list:

        if costs[o[1], o[0]] < minVal:
            minVal = costs[o[1], o[0]]
            currentPosition = o

    if currentPosition in open_list:

        open_list.remove(currentPosition)
        
    closed_list.append(currentPosition)

    cx = currentPosition[0]
    cy = currentPosition[1]

    costs[cy, cx] = cost(cx, cy)

    if cx == boardLength - 1 and cy == boardLength - 1:
        break

    for n in neighbours:
        nb_x = cx + n[0]
        nb_y = cy + n[1]

        if nb_x in range(boardLength) and nb_y in range(boardLength):

            if (nb_x, nb_y) not in closed_list:

                if (nb_x, nb_y) in open_list:

                    if costs[cy, cx] + board[nb_y, nb_x] < costs[nb_y, nb_x]:
                        prev[nb_y, nb_x] = currentPosition
                        costs[nb_y, nb_x] = costs[cy, cx] + board[nb_y, nb_x]

                else:
                    open_list.append((nb_x, nb_y))
                    prev[nb_y, nb_x] = currentPosition
                    costs[nb_y, nb_x] = costs[cy, cx] + board[nb_y, nb_x]

    if len(closed_list) % 2500 == 0:
        print(len(closed_list), len(open_list))

    if len(closed_list) % 25000 == 0:
        plt.title(len(closed_list))
        plt.imshow(np.where(costs != 99999, costs, 0), interpolation='nearest', origin = 'upper')
        plt.colorbar()
        plt.show(block = 'False')

x = y = boardLength - 1

g = 0

print(str(x) +  ' '  + str(y) + ' (' + str(board[y, x]) + ') | ', end = '')

while not (x == 0 and y == 0):
    g += board[y, x]
    x, y = prev[y, x]
    costs[y, x] = 3000
    print(str(x) +  ' '  + str(y) + ' (' + str(board[y, x]) + ') | ', end = '')

print()
print(g)

plt.title(len(closed_list))
plt.imshow(np.where(costs != 99999, costs, 0), interpolation='nearest', origin = 'upper')
plt.colorbar()
plt.show()
