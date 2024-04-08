from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix, \
    swap_rows_elementary_matrix
import numpy as np


def inverse(matrix):
    print(bcolors.OKBLUE,
          f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n",
          bcolors.ENDC)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        # Check if the diagonal element is zero, if yes, swap rows
        if matrix[i, i] == 0:
            # Find a row below with a non-zero element in the same column and swap them
            for k in range(i + 1, n):
                if matrix[k, i] != 0:
                    swap_elementary_matrix = swap_rows_elementary_matrix(n, i, k)
                    print(f"elementary matrix to swap R{i + 1} and R{k + 1}:\n {swap_elementary_matrix} \n")
                    matrix = np.dot(swap_elementary_matrix, matrix)
                    identity = np.dot(swap_elementary_matrix, identity)
                    print(f"The matrix after elementary operation :\n {matrix}")
                    print(bcolors.OKGREEN,
                          "------------------------------------------------------------------------------------------------------------------",
                          bcolors.ENDC)
                    break
            else:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print(bcolors.OKGREEN,
                  "------------------------------------------------------------------------------------------------------------------",
                  bcolors.ENDC)
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(i, n):
            if i != j and matrix[j, i] != 0:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN,
                      "------------------------------------------------------------------------------------------------------------------",
                      bcolors.ENDC)
                identity = np.dot(elementary_matrix, identity)

    for i in range(n-1, -1,-1):
        for j in range(i, -1,-1):
            if i != j and matrix[j, i] != 0:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(bcolors.OKGREEN,
                      "------------------------------------------------------------------------------------------------------------------",
                      bcolors.ENDC)
                identity = np.dot(elementary_matrix, identity)

    return identity


if __name__ == '__main__':
    A = np.array(([[1, 2, 3, 4],
           [2, 3, 4, 5],
           [8, 8, 8, 8],
           [24,15,22,1],
           ]))

    try:
        A_inverse = inverse(A)
        print(bcolors.OKBLUE, "\nInverse of matrix A: \n", A_inverse)
        print(
            "=====================================================================================================================",
            bcolors.ENDC)

    except ValueError as e:
        print(str(e))
