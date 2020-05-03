# Code written by Paul Ferlitz on Sunday, 3. March 2020
# GitHub: https://github.com/GigaWarTrex
# Repo: https://github.com/GigaWarTrex/sudoku-solver

"""
Imports
"""
import sys


class Solver:
    # Init
    size = 9
    sudokuGrid = None

    # Constructor
    def __init__(self, size, grid):
        # Set class variables
        self.size = size
        self.sudokuGrid = grid
        print('\n==> Solving:')
        self.nicePrintGrid(self.sudokuGrid)
        # Start solving
        self.solveGrid()

    """
    Method to print a good looking Sudoku grid
    """
    def nicePrintGrid(self, grid):
        # Top row
        print('+'+'-------+'*int(self.size/3))
        # Parse every row
        for i in range(0, self.size):
            retStr = '| '
            for h in range(0, self.size):
                retStr = retStr + str(grid[i][h]) + ' '
                if (h+1) % 3 == 0:
                    retStr = retStr + '| '
            print(retStr)
            if (i+1) % 3 == 0:
                print('+'+'-------+'*int(self.size/3))

    """
    Method that checks if n can exist in field x,y
    """
    def validInput(self, x, y, n):
        # Check row and column of x,y for n
        for i in range(0, self.size):
            if self.sudokuGrid[y][i] == n or self.sudokuGrid[i][x] == n:
                return False
        # Check x,y's 3x3 square for n
        for h in range(0, 3):
            for i in range(0, 3):
                if self.sudokuGrid[int(y/3)*3+h][int(x/3)*3+i] == n:
                    return False
        return True

    """
    Method to recusivly solve Sudoku
    """
    def solveGrid(self):
        # Iterate over x
        for x in range(0, self.size):
            # Iterate over y
            for y in range(0, self.size):
                # Check if field is empty
                if self.sudokuGrid[y][x] == 0:
                    # Iterate over all possible numbers
                    for n in range(1, 10):
                        # Is valid?
                        if self.validInput(x, y, n):
                            # Save n to field
                            self.sudokuGrid[y][x] = n
                            # Keep solving with new board
                            self.solveGrid()
                            # Reset to empty
                            self.sudokuGrid[y][x] = 0
                    return
        print('\n==> Solution:')
        # Print first solution found
        self.nicePrintGrid(self.sudokuGrid)
        # Exit
        sys.exit()
