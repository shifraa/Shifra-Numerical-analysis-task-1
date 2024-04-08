import numpy as np
from colors import bcolors
from matrix_utility import swap_row ,scalar_multiplication_elementary_matrix


def gaussianElimination(mat):
    N = len(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:

        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"
    print(np.array(mat))
    # if matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)


def forward_substitution(mat):
    N = len(mat)
    for k in range(N):
        pivot_row = k
        v_max = mat[pivot_row][k]
        for i in range(k + 1, N):
            if abs(mat[i][k]) > abs(v_max):
                v_max = mat[i][k]
                pivot_row = i

        # if a principal diagonal element is zero,it denotes that matrix is singular,
        # and will lead to a division-by-zero later.

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)



        # Normalize the current row by dividing all elements by the pivot element (diagonal element)
        pivot_element = mat[k][k]
        for j in range(k, N + 1):
            mat[k][j] /= pivot_element

        for i in range(k + 1, N):
            #  Compute the multiplier
            m = mat[i][k] / mat[k][k]

            # subtract fth multiple of corresponding kth row element
            for j in range(k, N + 1):  # Iterate from k to N instead of k+1 to N for normalization
                mat[i][j] -= mat[k][j] * m

            # filling lower triangular matrix with zeros
            mat[i][k] = 0

    return -1


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


if __name__ == '__main__':

    A_b = np.array([[2, 3, 4, 5],
                    [2, 3, 4, 5]
                    [2, 3, 4, 5]
                    [2, 3, 4, 5]])
    np.array(A_b)


    result = gaussianElimination(A_b)

    if isinstance(result, str):
        print(result)
    else:
        print(bcolors.OKBLUE, "\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
