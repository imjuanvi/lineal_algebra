"""
Created on Sun Aug  7 00:06:26 2022
@author: Juanvi
"""

# Import the library
import numpy as np


# We define the functions
def determinant(matrix):
    return int(np.linalg.det(matrix))

def adjoint_matrix(matrix):

    try:
        det = determinant(matrix)
        if det != 0:
            adjoint = None
            adjoint = np.linalg.inv(matrix) * det
            return adjoint
        else:
            raise Exception("The determinant of the matrix is zero")
    except Exception as not_work:
        print("could not find adjoint matrix due to",not_work)


def inverse_matrix(adj_matrix, determinant):
    return np.multiply(adj_matrix,1/determinant)

# We define the identity matrix
identity = np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])

# This is the matrix of which we want to know the inverse
matrix = np.array([[2,0,1],[1,1,-4],[3,7,-3]])


# We calculate the inverse
inverse = inverse_matrix(adjoint_matrix(matrix),determinant(matrix))

# We calculate the multiplication of both matrices
mult = np.round_(np.matmul(matrix,inverse))

# We obtain a final result
if not (identity==mult).all():
    print('There was an error when calculating the inverse matrix')
else:
    for count, i in enumerate(inverse):
        for j in inverse[count]:
            print(round(j,3),end="   ")
        print()