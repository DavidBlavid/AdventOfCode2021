import numpy as np
from numpy.core.fromnumeric import repeat

class Board:

    # nums is a 5x5 array
    def __init__(self, board):

        self.board = board
        self.marked = np.ones((5, 5))


    def mark(self, n):

        if n == 16:
            print(self.board, n)

            print(n in self.board)
        
        if int(n) in self.board:
            pos = np.where(self.board == n)
            self.marked[pos] = 0

    def check_bingo(self):

        # check cols
        sum_c = self.marked.sum(axis = 0)
        # check rows
        sum_r = self.marked.sum(axis = 1)

        #print(self)
        print(sum_c, sum_r)
        #print(5 in sum_c, 5 in sum_r)

        return ((0. in sum_c) or (0. in sum_r))

with open('Day 4/input.txt') as file:
    draws = file.readline()[:-1].split(',')
    print(draws)
    file.readline()

    read_pos = 0
    new_board = np.zeros((5, 5))

    boards = []

    for line in file:

        if read_pos == 5:

            boards.append(Board(new_board))

            new_board = np.zeros((5, 5))
            read_pos = 0

        else:

            nums = [int(line[i:i+2]) for i in range(0, 14, 3)]

            new_board[read_pos] = nums

            read_pos += 1


    first_winner = None
    last_winner = None

    first_i = 0
    last_i = 0

    print(boards[1].board)

    for i in draws:

        removed_boards = []

        print('Mark ', str(i), ' Boards: ', len(boards))

        for b in boards:

            b.mark(int(i))

            if b.check_bingo():

                print('BINGO!')

                if first_winner is None:
                    first_winner = b
                    first_i = int(i)
                    print('FIRST WINNER!')

                if len(boards) == 1:
                    last_winner = b
                    last_i = int(i)
                    print('LAST WINNER!')
                    break

                print(b)
                removed_boards.append(b)

        if not last_winner is None:
            break

        for r in removed_boards:
            boards.remove(r)

    print('====================')

    print(first_winner.board, '\n', first_winner.marked)
    print(first_winner.board * first_winner.marked, first_i)
    print(sum(sum(first_winner.board * first_winner.marked)) * first_i)

    print()

    print(last_winner.board, '\n', last_winner.marked)
    print(last_i)
    print(sum(sum(last_winner.board * last_winner.marked)))
    print(sum(sum(last_winner.board * last_winner.marked)) * last_i)
