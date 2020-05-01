import numpy as np

sudokuGrid = [[4,5,0,0,0,0,0,0,0],
            [0,0,2,0,7,0,6,3,0],
            [0,0,0,0,0,0,0,2,8],
            [0,0,0,9,5,0,0,0,0],
            [0,8,6,0,0,0,2,0,0],
            [0,2,0,6,0,0,7,5,0],
            [0,0,0,0,0,0,4,7,6],
            [0,7,0,0,4,5,0,0,0],
            [0,0,8,0,0,9,0,0,0]]

def validInput(x,y,n):
    for i in range(0,9):
        if sudokuGrid[y][i] == n or sudokuGrid[i][x] == n:
            return False
            
    for h in range(0,3):
        for i in range(0,3):
            if sudokuGrid[int(y/3)*3+h][int(x/3)*3+i] == n:
                return False
    return True

def solveGrid():
    for x in range(0,9):
        for y in range(0,9):
            if sudokuGrid[y][x] == 0:
                for n in range(1,10):
                    if validInput(x,y,n):
                        sudokuGrid[y][x] = n
                        solveGrid()
                        sudokuGrid[y][x] = 0
                return

def doTheThing():
    print('==> Solving:\n',np.matrix(sudokuGrid))
    print()
    solveGrid()
    print('==> Solution:\n',np.matrix(sudokuGrid))

if __name__ == '__main__':
    doTheThing()