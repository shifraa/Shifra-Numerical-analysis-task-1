def checkIfSquare(mat):
    """
    this function checks if the matrixis square.
    :param mat: matrix - type list
    :return: boolean
    """
    rows = len(mat)
    for i in mat:
        if len(i) != rows:
            return False
    return True


def isDDM(m, n):
    """
     check the if given matrix is Diagonally Dominant Matrix or not.
    :param m: the matrix, type list.
    :param n: size of the matrix (nxn)
    :return: boolean
    """
    # for each row
    for i in range(0, n):

        # for each column, finding sum of each row.
        sum1 = 0
        for j in range(0, n):
            sum1 = sum1 + abs(m[i][j])

        # removing the diagonal element.
        sum1 = sum1 - abs(m[i][i])

        # checking if diagonal element is less than sum of non-diagonal element.
        if (abs(m[i][i]) < sum1):
            return False
    return True


def rowSum(row, n, x):
    """
    caculates the rowws sum
    :param row: a single row from the matrix
    :param n: the row's size
    :param x: the x vector with results
    :return: the sum
    """
    sum1 = 0
    for i in range(n):
        sum1 += row[i] * x[i]
    return sum1


def checkResult(result, last_result, n, epsilon):
    """
    checking if the result is accurate enough
    :param result: the most recent result
    :param last_result: the previous result
    :param n: the size of the result vector
    :return: boolean
    """
    for i in range(n):
        if abs(result[i] - last_result[i]) > epsilon:
            return False
    return True


def Jacobi(mat, b, epsilon =0.000001):  # mat needs to be a list, example: l1 = [[2,3],[4,5]]
    """
    caculating matrix to find vareables vector accourding to yaakobi's algorithem
    :param mat: the matrix
    :param b: the result vector
    :return: the variables vector
    """
    # input check
    n = len(mat)
    if not checkIfSquare(mat):
        return "matrix is not square"
    if len(b) != n:
        return "b is not in the right size"

    # check if Diagonally Dominant Matrix
    if not isDDM(mat, n):
        print("matrix is not Diagonally Dominant")


    # taking a guess: all zeros
    last_result = list()
    for i in range(n):
        last_result.append(0)

    result = last_result.copy()

    print("all results:\nx\t\ty\t  z")
    count =0
    while True:
        for i in range(n):  # for each variable
            result[i] = b[i] - (rowSum(mat[i], n, last_result) - mat[i][i] * last_result[i])
            result[i] /= mat[i][i]


        print("i = "+str(count)+": "+str(result))
        count+=1
        if checkResult(result, last_result, n, epsilon):
            return result
        last_result = result.copy()




