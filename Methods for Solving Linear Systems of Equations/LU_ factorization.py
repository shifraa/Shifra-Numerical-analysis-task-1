import numpy as np

from colors import bcolors
from matrix_utility import swap_rows_elementary_matrix, row_addition_elementary_matrix


def lu(A):
        N = len(A)
        L = np.eye(N) # Create an identity matrix of size N x N

        for i in range(N):
    
            # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
            pivot_row = i
            v_max = A[pivot_row][i]
            for j in range(i + 1, N):
                if abs(A[j][i]) > v_max:
                    v_max = A[j][i]
                    pivot_row = j

            # if a principal diagonal element is zero,it denotes that matrix is singular,
            # and will lead to a division-by-zero later.
            if A[i][pivot_row] == 0:
                raise ValueError("can't perform LU Decomposition")

            # Swap the current row with the pivot row
            if pivot_row != i:
                e_matrix = swap_rows_elementary_matrix(N, i, pivot_row)
                print(f"elementary matrix for swap between row {i} to row {pivot_row} :\n {e_matrix} \n")
                A = np.dot(e_matrix, A)
                print(f"The matrix after elementary operation :\n {A}")
                print(bcolors.OKGREEN,"---------------------------------------------------------------------------", bcolors.ENDC)

            for j in range(i + 1, N):
    
                #  Compute the multiplier
                m = -A[j][i] / A[i][i]
                e_matrix = row_addition_elementary_matrix(N, j, i, m)
                e_inverse = np.linalg.inv(e_matrix)
                L = np.dot(L, e_inverse)
                A = np.dot(e_matrix, A)
                print(f"elementary matrix to zero the element in row {j} below the pivot in column {i} :\n {e_matrix} \n")
                print(f"The matrix after elementary operation :\n {A}")
                print(bcolors.OKGREEN,"---------------------------------------------------------------------------", bcolors.ENDC)

        U = A
        return L, U


# function to calculate the values of the unknowns
def backward_substitution(mat):
    N = len(mat)
    x = np.zeros(N)  # An array to store solution

    # Start calculating from last equation up to the first
    for i in range(N - 1, -1, -1):

        x[i] = mat[i][N]

        # Initialize j to i+1 since matrix is upper triangular
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]

        x[i] = (x[i] / mat[i][i])

    return x

def lu_solve(A_b):
    L, U = lu(A_b)
    print("Lower triangular matrix L:\n", L)
    print("Upper triangular matrix U:\n", U)

    result = backward_substitution(U)
    print(bcolors.OKBLUE,"\nSolution for the system:")
    for x in result:
        print("{:.6f}".format(x))

# Git:
# Date: 18.03.2024
# Group: Eytan Stryzhack 336244959, Daniel Boguslavsky 207915729, Shifra Avigdor 207067125, David Moalem 203387337


# Name: Daniel Boguslavsky

if __name__ == '__main__':
    A_b= np.array([[2, 3, 4,5],
                  [2, 3, 4,5]
                   [2, 3, 4,5]
                   [2, 3, 4,5]])


    lu_solve(A_b)