import math
from math import sqrt
import numpy as np

from colors import bcolors


def gaussian_quadrature(f, a, b, n):
    """
    Gaussian Quadrature for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of nodes and weights to use.

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    # Define the nodes and weights for Gaussian Quadrature
    nodes, weights = np.polynomial.legendre.leggauss(n)

    # Transform nodes from [-1, 1] to [a, b]
    x = 0.5 * (b - a) * nodes + 0.5 * (a + b)

    # Calculate the integral using the Gaussian Quadrature formula
    integral = sum(weights[i] * f(x[i]) for i in range(n))
    integral *= 0.5 * (b - a)

    return integral


def sub_division(f,a,b,tol,entire,results):

    a_z = a+(b-a)/2.  #sub-divides intervals
    b_k = a+(b-a)/2.
    entire=gaussian(f,a,b)
    right=gaussian(f,a_z,b)
    left=gaussian(f,a,b_k)
    if abs(entire-(left+right))<tol * max(abs(entire), (abs(left)+abs(right))):
        results.append(entire)
        return entire
    x=sub_division(f,a_z,b,tol,right,results)+sub_division(f,a,b_k,tol,left,results)
    results.append(x)
    return x

def gaussian(f,a,b):
    #f: function that needs to be integrated
    #a,b: bounds of the integral (a<b)
    #this function is just the normal gaussian quadrature calculation with known weights
    #also uses an interval transformation so instead of just the standard interval of -1 to 1, you can use any interval
    u=(b-a)/2.*(5./9*f((b-a)/2.*-1.*sqrt(3./5)+(b+a)/2.)+8./9*f((b+a)/2.)+5./9*f((b-a)/2.*sqrt(3./5)+(b+a)/2.))
    return u

def adaptive_gaussian_quadrature(f,a,b,tol,results):
    #returns the approximate integral of f from a to b with an upper bound on the error given by the tolerance
    return sub_division(f,a,b,tol,gaussian(f,a,b),results)



if __name__ == '__main__':
    a = 0
    b = 2
    n = 4
    tol =1e-6
    f = lambda x: math.e**(3*x)

    results = []
    res = adaptive_gaussian_quadrature(f,-1,1, tol,results)
    for i in range(len(results)):
        print(f'-Result number {i+1} : {results[i]}')
    print(bcolors.OKBLUE,'\nIntegral value is', res, bcolors.ENDC) #input intervals and tolerance here