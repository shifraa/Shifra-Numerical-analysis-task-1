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

def find_all_roots(f, a, b, tol=1e-6):
    roots = []
    x = np.linspace(a, b, 1000)

    x_sym = sp.symbols('x')
    f_sym = f(x_sym)

    for i in range(len(x) - 1):
        if np.sign(f(x[i])) != np.sign(f(x[i + 1])):
            interval = sp.Interval(x[i], x[i + 1])
            try:
                root = sp.nsolve(f_sym, (interval.start + interval.end)/2, tol=tol)
                roots.append(root)
            except ValueError:
                print(f"Could not find root within tolerance in interval {interval}")

    return roots

if __name__ == '__main__':
    f = lambda x: x**2-x
    start = 1
    end = 3

    roots = find_all_roots(f, start, end)
    print(roots)