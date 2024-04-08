from colors import bcolors


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result

if __name__ == '__main__':

    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [1.31, 2.69, 1.30, -1.25, -2.1]
    x_a = 1.47  # The x1-value where you want to interpolate
    x_b = 1.65  # The x2-value where you want to interpolate
    y_a = lagrange_interpolation(x_data, y_data, x_a)
    y_b = lagrange_interpolation(x_data, y_data, x_b)
    print(bcolors.OKBLUE, "\nInterpolated value at xa =", x_a, "is ya =", y_a, bcolors.ENDC)
    print(bcolors.OKBLUE, "\nInterpolated value at xb =", x_b, "is yb =", y_b, bcolors.ENDC)


