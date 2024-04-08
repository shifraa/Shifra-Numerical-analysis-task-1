from colors import bcolors


def secant_method(f, x0, x1, TOL, N=50):
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "xo", "x1", "p"))
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print(" method cannot continue.")
            return

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < TOL:
            return p  # Procedure completed successfully

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1, p))

        x0 = x1
        x1 = p

    return p


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x + 2
    TOL = 1e-6
    N = 50
    roots = []
    for x0 in range(6):
        x1 = x0 + 1
        root = secant_method(f, x0, x1, TOL, N)
        if root is not None and -5 <= root <= 0:
            root = round(root,4)
            if root not in roots:
                roots.append(root)

    print(bcolors.OKBLUE, f"\nThe equation f(x) has approximate roots at x = {roots}", bcolors.ENDC)
