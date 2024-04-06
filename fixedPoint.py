import numpy as np

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
def fixedPoint(f, p0, Nmax, TOL):
    #print('index        Pn             f(Pn)')
    n = 0
    while n <= Nmax:
        p = f(p0)
        print(f' {n:2d}     {p0:3.15f}     {p:3.15f}')
        if np.abs(p - p0) < TOL: 
            print(f'Method succeded after {n} iterations, found: {p}')
            return n
        
        n += 1
        p0 = p #update Pn
    print(f'Method failed after {Nmax} iterations, found: {p}')
    return Nmax