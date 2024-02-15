from colors import bcolors


def machine_epsilon():
    eps = 1
    while (1 + eps) > 1:
        eps = eps / 2

    eps = eps * 2
    return eps


if __name__ == '__main__':
    m_eps = machine_epsilon()
    print(bcolors.OKBLUE, "Machine Precision  : ", m_eps, bcolors.ENDC)

    expression = abs(3.0 * (4.0 / 3.0 - 1) - 1)
    print("\nResult of abs(3.0 * (4.0 / 3.0 - 1) - 1) :")
    print(bcolors.FAIL, "before using machine epsilon: {}".format(expression), bcolors.ENDC)
    print(bcolors.OKGREEN, "After correcting with machine epsilon: {}".format(expression - m_eps), bcolors.ENDC)
