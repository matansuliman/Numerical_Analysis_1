import numpy as np
from decimal import Decimal

#update bisection

# bisection
# prerequisites:
#   f(x) E C[a,b]
#   an initial interval such that f(a)*f(b)<0 , meaning opposite signs
# @param f is the function to find root
# @param a is the left bound
# @param b is the right bound
# @param Nmax is the maximum iterations for finding the root
# @param TOL is the tolerance to find the root
def bisect(f, a, b, Nmax, TOL):
    print('index         An             Cn            Bn           f(Cn)')
    n = 0
    while n <= Nmax:
        c = (a+b)/2.0
        print(f' {n:2d}    {a:3.10f}  {c:3.10f}  {b:3.10f}  {f(c):3.10f}')
        if f(c) == 0 or (b-a)/2 < TOL: 
            print(f'Methound succeded after {n} iterations, found: {Decimal(c)}')
            return
        else: n += 1
        if f(c)*f(a) < 0: b = c
        else: a = c
    print(f'Methound failed after {Nmax} iterations, found: {Decimal(c)}')


def func1(x):
    return np.exp(x) - 1

# find x when e^x - 1 = 0
bisect(func1, a=-2.5, b=1, Nmax=25, TOL=pow(10, -5))
print(f'the actual root is x=0')
