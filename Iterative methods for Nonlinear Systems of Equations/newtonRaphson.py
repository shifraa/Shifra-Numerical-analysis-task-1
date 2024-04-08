from colors import bcolors

def newton_raphson(f, df, p0, TOL, start, end, N=50):
    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))

    for i in range(N):
        if df(p0) == 0:
            if f(p0) == 0:
                return p0
            print("Derivative is zero at p0, method cannot continue.")
            return

        p = p0 - f(p0) / df(p0)

        if p > end:
            return "EMPTY"
        if p < start:
            return "EMPTY"

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully

        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p

    return p

if __name__ == '__main__':
    try:
        f = lambda x: x**2 -5*x + 2
        df = lambda x: 2*x -5
        TOL = 1e-6
        N = 100
        start = 0
        end = 5
        roots = []

        for x in range(int(start), int(end)+1):
            p0 = x
            root = newton_raphson(f, df, p0, TOL, start, end, N)
            if root != "EMPTY":
                root = round(root, 6)
                if root not in roots:
                    roots.append(root)


        if roots:
            print(bcolors.OKBLUE + "\nThe equation f(x) has approximate roots at x = {}".format(roots) + bcolors.ENDC)
        else:
            print("No roots found in the specified range.")
    except:
        print("Error occurred during the calculation.")
