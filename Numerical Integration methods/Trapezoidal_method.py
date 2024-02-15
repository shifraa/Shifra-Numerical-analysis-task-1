import math

from colors import bcolors


def trapezoidal_rule(f, a, b, n):

    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


if __name__ == '__main__':
    f = lambda x:math.e ** (x ** 2 )
    result = trapezoidal_rule(f, 0, 1, 2)
    print(bcolors.OKBLUE,"Approximate integral:", result, bcolors.ENDC)
