import numpy
puzzle = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 0, 0, 9],
          [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0],
          [0, 0, 1, 0, 5, 0, 9, 3, 0],
          [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2],
          [1, 2, 0, 0, 0, 7, 4, 0, 0],
          [0, 4, 9, 2, 0, 6, 0, 0, 7]]
# input sudoku puzzle here


def check_possible(y, x, n):
    global puzzle
    for i in range(0, 9):
        if puzzle[y][i] == n:
            return False
    for j in range(0, 9):
        if puzzle[j][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[y0+i][x0+j] == n:
                return False
    return True


def display(list_):
    for i in range(9):

        if i % 3 == 0 and not i == 0:
            print('='*36, end='')
            print()
        for j in range(9):
            if j % 3 == 0 and not j == 0:
                print(' ‖  ', end='')
            print(list_[i][j], ' ', end='')
        print('')


def solve():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if check_possible(y, x, n):
                        puzzle[y][x] = n
                        solve()
                        puzzle[y][x] = 0

                return

    print(display(puzzle))
    input('more soln')


solve()
