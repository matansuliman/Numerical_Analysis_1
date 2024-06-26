import numpy as np

# secant method
# prerequisites:
#   f(x) E C[a,b]
#   an initial interval such that f(a)*f(b)<0 , meaning opposite signs
# @param f is the function to find fixed point meaning f(x)=x
# @param p0 is the firat guess
# @param Nmax is the maximum iterations for finding the root
# @param TOL is the tolerance to find the root
def secant_method(f, p0, p1, Nmax, TOL):
    print('index        Pn            f(Pn)')
    n = 2
    q0 = f(p0)
    q1 = f(p1)
    print(f' {0:2d}    {p0:3.15f}    {f(q0):3.15f}')
    print(f' {1:2d}    {p1:3.15f}    {f(q1):3.15f}')
    while n <= Nmax:
        p = p1 - q1*((p1-p0)/(q1-q0))
        print(f' {n:2d}    {p:3.15f}    {f(p):3.15f}')
        if np.abs(p - p1) < TOL: 
            print(f'Methound succeded after {n} iterations, found: {p}')
            return
        n += 1
        q = f(p)
        if q*q1<0:
            p0 = p
            q0 = q
        else: 
            p1 = p
            q1 = q
    print(f'Methound failed after {Nmax} iterations, found: {p}')


f1 = lambda x: np.cos(x) - x
# find root of f(x) = cos(x) - x
secant_method(f1, p0=0.5, p1=np.pi/4, Nmax=17, TOL=pow(10, -3))
