# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:49:03 2022

@author: Juanvi
"""

# Import the library
import numpy as np

# We define the functions

def inverse(matrix):
    return np.linalg.inv(matrix)

def eigvalues(matrix):
    return np.linalg.eigvals(matrix)

def eigvector(matrix):
    eigenvalues, eigenvector = np.linalg.eig(matrix)
    return eigenvector

def P(matrix):
    return eigvector(matrix)

def D(matrix):
    e_v = eigvalues(matrix)
    D = np.zeros((3,3))
    for i in range (3):
        D[i,i] = e_v[i]
    return D

def P_inv(matrix):
    return np.linalg.inv(matrix)


# We set up the script

def diagonalization(matrix,P,D,P_inv):
    # We show the output
    print('-------------------------')
    print('The eigenvalues of the matrix are: ')
    print('-------------------------')
    for value in eigvalues(matrix):
        print(round(value),end="  ")
    print("\n")
    print('-------------------------')
    print('The base change matriz P is:')
    print('-------------------------')
    print(np.round(P,3))

    print('-------------------------')
    print('The diagonal matrix D is:')
    print('-------------------------')
    print(D)

    print('-------------------------')
    print('The inverse of P is:')
    print('-------------------------')
    print(np.round(P_inv,3))


    print('-------------------------')
    print('Let\'s check if we multiply these matrix we get the original matrix')
    print('-------------------------')
    print(P.dot(D.dot(P_inv)))


# We run the program
if __name__ == '__main__':
    # This is the matrix we want to know the inverse, eigenvalues, eigenvectors and diagonalization
    matrix = np.array([[3,-2,-1],[2,-7,-7],[-2,10,10]])
    # We calculate P, D and the inverse of P
    P = P(matrix)
    D = D(matrix)
    P_inv = P_inv(P)
    diagonalization(matrix,P,D,P_inv)



