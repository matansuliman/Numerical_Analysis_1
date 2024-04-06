import numpy as np
from decimal import Decimal

# fixed point method
# p is a fixed point of g if g(p)=p
# prerequisites:
#   f(x) E C[a,b] such that f([a,b])E[a,b]
#   df(x) exsist in (a,b) and exsists 0<k<1 such that |df(x)|<k for all xE(a,b)
# conclusions:
#   |Pn - P| <= k^n * max{p0-a, b-p0}
# @param f is the function to find fixed point meaning f(x)=x
# @param p0 is the firat guess
# @param Nmax is the maximum iterations for finding the root
# @param TOL is the tolerance to find the root
def steffensens_method(f, p0, Nmax, TOL):
    print('index        Pn             f(Pn)')
    n = 0
    while n <= Nmax:
        p1 = f(p0)
        p2 = f(p1)
        numerator = np.power(p1 - p0, 2)
        denominator = (p2 - 2*p1 + p0)
        if denominator == 0:
            print(f'Methound divded by 0 after {n} iterations, found: {p0}')
            return n
        p = p0 - (numerator / denominator)
        print(f' {n:2d}     {p0:3.10f}   {f(p0):3.10f}')
        if np.abs(p - p0) < TOL: 
            print(f'Methound succeded after {n} iterations, found: {p0}')
            return n
        n += 1
        p0 = p #update Pn
    print(f'Methound failed after {Nmax} iterations, found: {p0}')
    return Nmax