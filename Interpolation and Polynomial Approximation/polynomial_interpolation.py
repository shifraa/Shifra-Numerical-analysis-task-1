from colors import bcolors
from matrix_utility import *


def polynomialInterpolation(table_points, x):
    x_data = [point[0] for point in table_points]
    y_data = [point[1] for point in table_points]

    # Perform polynomial interpolation using numpy. poly fit
    coefficients = np.polyfit(x_data, y_data, deg=len(x_data) - 1)

    # Construct the polynomial function
    polynomial = np.poly1d(coefficients)

    # Evaluate the polynomial at the specified point
    result = polynomial(x)

    print(bcolors.OKBLUE, "The coefficients of the polynomial:", bcolors.ENDC)
    print(coefficients)

    print(bcolors.OKBLUE, "\nThe polynom:", bcolors.ENDC)
    print(polynomial)

    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result)

    return result


if __name__ == '__main__':
    table_points = [(1.2, 1.31), (1.3, 2.69), (1.4, 1.30), (1.5, -1.25), (1.6, -2.1)]
    x = 1.65
    # x = 1.47
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x, '\n')
    polynomialInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n",
          bcolors.ENDC)

