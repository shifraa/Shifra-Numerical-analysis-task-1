from colors import bcolors


def neville(x_data, y_data, x_interpolate):
    n = len(x_data)

    # Initialize the tableau
    tableau = [[0.0] * n for _ in range(n)]

    for i in range(n):
        tableau[i][0] = y_data[i]

    for j in range(1, n):
        for i in range(n - j):
            tableau[i][j] = ((x_interpolate - x_data[i + j]) * tableau[i][j - 1] -
                             (x_interpolate - x_data[i]) * tableau[i + 1][j - 1]) / (x_data[i] - x_data[i + j])

    return tableau[0][n - 1]

if __name__ == '__main__':
    # Example usage:
    x_data = [1, 2, 5, 7]
    y_data = [1, 0, 2, 3]
    x_interpolate = 3

    interpolated_value = neville(x_data, y_data, x_interpolate)
    print(bcolors.OKBLUE, f"\nInterpolated value at x = {x_interpolate} is y = {interpolated_value}", bcolors.ENDC)