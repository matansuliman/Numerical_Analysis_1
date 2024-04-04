import numpy as np
from decimal import Decimal

# p is a fixed point of g if g(p)=p
# prerequisites:
#   f(x) E C[a,b] such that f([a,b])E[a,b]
#   df(x) exsist in (a,b) and exsists 0<k<1 such that |df(x)|<k for all xE(a,b)
# conclusions:
#   |Pn - P| <= k^n * max{p0-a, b-p0}
# @param f is the function to find fixed point meaning f(x)=x
# @param po is the firat guess
# @param Nmax is the maximum iterations for finding the root
# @param TOL is the tolerance to find the root
def fixedPoint(f, p0, Nmax, TOL):
    print('index        Pn             f(Pn)')
    n = 0
    while n <= Nmax:
        p = f(p0)
        print(f' {n:2d}    {p0:3.10f}    {f(p0):3.10f}')
        if np.abs(p - p0) < TOL: 
            print(f'Methound succeded after {n} iterations, found: {Decimal(p0)}')
            return
        n += 1
        p0 = p #update p
    print(f'Methound failed after {Nmax} iterations, found: {Decimal(p0)}')


def func1(x):
    return np.exp(x) - 2

# find x when e^x - 2 = x
# find root when f(x) = e^x - 2 - x
fixedPoint(func1, p0=0, Nmax=17, TOL=pow(10, -5))
