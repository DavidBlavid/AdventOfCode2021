import numpy as np

board = []

for ln in open('Day 11/input.txt').readlines():

    board.append([int(x) for x in ln[:-1]])

board = np.array(board)

counter1 = counter2 = 0


#board = np.array([[5, 9, 0], [9, 8, 0], [2, 1, 0]])
#board = np.array([[9, 9, 9], [9, 1, 9], [9, 9, 9]])

while True:
    print(counter2)

    nextBoard = board.copy()

    for yp, y in enumerate(board):
        for xp, x in enumerate(y):
            nextBoard[yp, xp] = board[yp, xp] + 1

    board = nextBoard.copy()

    while np.any(board.flatten() >= 10):
        nextBoard = np.pad(board.copy(), ((1, 1), (1, 1)), 'constant')

        counter1 += np.sum(board.flatten() >= 10)

        for yp, y in enumerate(board):
            for xp, x in enumerate(y):

                if board[yp, xp] >= 10:

                    for xoff in range(0, 3):        # 0, 1, 2
                        for yoff in range(0, 3):    # 0, 1, 2

                            nextBoard[yp + yoff, xp + xoff] += 1

                    nextBoard[yp + 1, xp + 1] = -100

        board = nextBoard[1:-1, 1:-1]
    
    for yp, y in enumerate(board):
            for xp, x in enumerate(y):

                board[yp, xp] = max(board[yp, xp], 0)

    counter2 += 1

    if board.sum() == 0:
        break


print('\n=== END ===\n')

print(board)
print(counter1)
print(counter2)
