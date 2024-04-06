import numpy as np
from decimal import Decimal

# false position method
# @param f is the function to find fixed point meaning f(x)=x
# @param p0 is the firat guess
# @param Nmax is the maximum iterations for finding the root
# @param TOL is the tolerance to find the root
def false_position(f, p0, p1, Nmax, TOL):
    print('index        Pn            f(Pn)')
    n = 2
    q0 = f(p0)
    q1 = f(p1)
    print(f' {0:2d}    {p0:3.10f}    {f(q0):3.10f}')
    print(f' {1:2d}    {p1:3.10f}    {f(q1):3.10f}')
    while n <= Nmax:
        p = p1 - q1*((p1-p0)/(q1-q0))
        print(f' {n:2d}    {p:3.10f}    {f(p):3.10f}')
        if np.abs(p - p1) < TOL: 
            print(f'Methound succeded after {n} iterations, found: {Decimal(p0)}')
            return
        n += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    print(f'Methound failed after {Nmax} iterations, found: {Decimal(p0)}')

f1 = lambda x: np.cos(x) - x
# find root of f(x) = cos(x) - x
false_position(f1, p0=0.5, p1=np.pi/4, Nmax=17, TOL=pow(10, -5))
