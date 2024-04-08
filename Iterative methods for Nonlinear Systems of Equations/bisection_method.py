import math
import numpy as np
import sympy as sp



def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s




def bisection_method(f, a, b, tol=1e-6):

    c, k = 0, 0
    steps = max_steps(a, b, tol)

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))


    while abs(b - a) > tol and k <= steps:
        c = (a + b) / 2

        if f(c) == 0:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f(a), f(b), c, f(c)))
        k += 1

    return c

def find_all_roots(f, a, b, tol=1e-4):
    roots = []
    x = np.linspace(a, b, 1000)

    x_sym = sp.symbols('x')
    f_sym = f(x_sym)

    for i in range(len(x) - 1):
        if np.sign(f(x[i])) != np.sign(f(x[i + 1])):
            interval = sp.Interval(x[i], x[i + 1])
            try:
                root = sp.nsolve(f_sym, (interval.start + interval.end)/2, tol=tol)
                # Check if the root is not already in the list with some tolerance
                if all(abs(root - r) > tol for r in roots):
                    roots.append(root)
            except ValueError:
                print(f"Could not find root within tolerance in interval {interval}")

    return roots

if __name__ == '__main__':
    # Git:https://github.com/danielbogus99/Numerical-analysis-task-1
    # Date: 18.03.2024
    # Group: Eytan Stryzhack 336244959,
    # Daniel Boguslavsky 207915729
    # , Shifra Avigdor 207067125,
    # David Moalem 203387337

    # Name: Daniel Boguslavsky
    f = lambda x: (2*x**2+7*x**3-6)/(3*x**2-6)
    start = 0
    end = 3

    roots = find_all_roots(f, start, end)
    print(roots)