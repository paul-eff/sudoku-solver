# Code written by Paul Ferlitz on Sunday, 3. March 2020
# GitHub: https://github.com/GigaWarTrex
# Repo: https://github.com/GigaWarTrex/sudoku-solver

"""
Imports
"""
from Solver import Solver


if __name__ == "__main__":
    # Init
    stage = 1
    size = 9
    sudokuGrid = None

    # Work Loop
    while True:
        # Size stage
        if stage == 1:
            try:
                # Get size
                size = int(input('Please enter the size of your Sudoku: '))
                print('Your Sudoku size was set to', str(size)+'x'+str(size)+'\n')
                # Enter next stage
                stage = 2
            except ValueError:
                # Catch error and repeat
                print('There was an error with your size.')
                continue
        # Sudoku entering stage
        if stage == 2:
            print('Now enter every row from top to botton.')
            print('Make sure that the numbers are correct and seperated by commas.')
            print('Enter empty fields as 0.\n')

            #Pre init
            row = 1
            # Working Loop 2
            while True:
                # Check row count
                if row <= size:
                    # Init array
                    numArray = [None] * size
                    # Get and clean row
                    line = input('Row['+str(row)+']: ')
                    line = line.replace(' ', '')
                    while line.startswith(','):
                        line = line[1:]
                    while line.endswith(','):
                        line = line[:len(line)-1]
                    line = line.split(',')
                    # Check row length
                    if len(line) == size:
                        try:
                            # Parse input to int array
                            for i in range(0, size):
                                num = int(line[i])
                                if num >= 0 and num <= size:
                                    numArray[i] = int(line[i])
                                else:
                                    print('Number', num, 'is outside the allowed range.')
                                    continue
                        except Exception:
                            print( 'There was a conversion error. Please retype the row.')
                            continue
                        # Save row to grid
                        sudokuGrid[row-1] = numArray
                        # Increment row count
                        row = row + 1
                    else:
                        print('Each row must contain', size, 'entries. Please retype the row.')
                        continue
                else:
                    # Enter next stage
                    stage = 3
                    break
        # Solving stage
        if stage == 3:
            # Solve and print Sudoku
            Solver(size, sudokuGrid)
