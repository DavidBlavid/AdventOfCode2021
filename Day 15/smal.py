import numpy as np

def cost(x, y, cl, ca, ba, pa):
    g = 0
    while not (x == 0 and y == 0):
        if (x, y) in cl:
            g += ca[y, x]
            break
        g += ba[y, x]
        x, y = pa[y, x]

    return g

def dijkstra(ba):

    cx = cy = g = 0
    ol, cl = [], []
    neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)] #ruld

    ca = ba.copy()

    pa = -np.arange(len(ba) * len(ba) * 2)
    pa.shape = (len(ba), len(ba), 2)

    while True:

        minCost = 10**10
        for ox, oy in ol:
            if ca[oy, ox] < minCost:
                minCost = ca[oy, ox]
                cx, cy = ox, oy
    
        if (cx, cy) in ol: ol.remove((cx, cy))
        cl.append((cx, cy))
        ca[cy, cx] = cost(cx, cy, cl, ca, ba, pa)
    
        if cx == len(ba) - 1 and cy == len(ba) - 1:
            break
         
        for ox, oy in neighbours:
            nx = cx + ox
            ny = cy + oy
    
            if nx in range(len(ba)) and ny in range(len(ba)):
                if (nx, ny) not in cl:
                    if (nx, ny) in ol:
                        if ca[cy, cx] + ba[ny, nx] < ca[ny, nx]:
                            pa[ny, nx] = (cx, cy)
                            ca[ny, nx] = ca[cy, cx] + ba[ny, nx]
                    else:
                        ol.append((nx, ny))
                        pa[ny, nx] = (cx, cy)
                        ca[ny, nx] = ca[cy, cx] + ba[ny, nx]

    while not (cx == 0 and cy == 0):
        g += ba[cy, cx]
        cx, cy = pa[cy, cx]

    return g

board = []

for ln in open('Day 15/input.txt').readlines():
    board.append([int(x) for x in ln[:-1]])

board = np.array(board)
bigBoard = np.tile(board, (5, 5))

for y in range(len(bigBoard)):
    for x in range(len(bigBoard)):
        bigBoard[y, x] += y // len(board) + x // len(board)
        if bigBoard[y, x] >= 10: bigBoard[y, x] -= 9

print(dijkstra(board))
print(dijkstra(bigBoard))