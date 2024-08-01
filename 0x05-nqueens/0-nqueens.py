#!/usr/bin/python3
# the Nqueens grandmaster cheese game


import sys


def is_valid(board, row, col):
    """ checking validity """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """ boarding """
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1


def print_solution(board):
    """ print output """
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def main():
    """ main function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
