#!/usr/bin/python3
import sys


def isSafe(board, row, col, n):
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

# Check for queens in the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # If safe, return True
    return True


def solveNQueens(board, row, n):
    # Base case: all rows are filled
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
            return True

    # Recursive case: try all possible columns for current row
    res = False
    for j in range(n):
        if isSafe(board, row, j, n):
            board[row][j] = 1
            res = solveNQueens(board, row+1, n) or res
            board[row][j] = 0

    return res


if __name__ == '__main__':
    # Get input argument
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

    # Initialize board
    board = [[0 for i in range(n)] for j in range(n)]

    # Solve N Queens problem
    solveNQueens(board, 0, n)
