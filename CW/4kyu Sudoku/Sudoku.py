import numpy as np


def validSolution(board):
    a = np.array(board)
    for i in range(9):
        if len(np.unique(a[i, :])) != 9 or len(np.unique(a[:, i])) != 9:
            return False
    for i in (0,3,6):
        for j in range(0,3,6):
            if len(np.unique(a[i:i+3,j:j+3])) != 9:
                return False
    return True

# or sum(a[i, :]) != 45 or sum(a[:, i]) != 45
print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
