import numpy as np

counter1 = counter2 = 0
board = np.loadtxt('Day 11/input.txt') // 10 ** np.arange(10)[:, None] % 10

while True:
    board = (board > 0) * board + 1                 # prepare board for iter
    if board.sum() == 100: break                    # flashes synchronized?

    while np.any(board >= 10):                      # were there any flashes?
        nextBoard = np.pad(board, 1)
        counter1 += np.sum(board >= 10) * (counter2 < 100)

        for yp, y in enumerate(board):              # go through all octopi
            for xp, x in enumerate(y):

                if board[yp, xp] >= 10:             # is octopus glowing?

                    for xoff in range(0, 3):        # incr all adjacent
                        for yoff in range(0, 3):
                            nextBoard[yp + yoff, xp + xoff] += 1

                    nextBoard[yp + 1, xp + 1] = -10
        board = nextBoard[1:-1, 1:-1]
    counter2 += 1

print(counter1)
print(counter2)