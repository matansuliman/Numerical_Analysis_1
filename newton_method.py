import numpy as np

# newton method
# prerequisites:
#   f(x) E C^2[a,b]
#   df(x) exsist in (a,b)
#   if pE(a,b) such that f(p)=0 and df(p)!=0 then exists l>0 such that pn converge to p for any p0E[p-l,p+l]
# @param f is the function to find root
# @param p0 is the firat guess
# @param Nmax is the maximum iterations for finding the root
# @param TOL is the tolerance to find the root
def newtons_method(f, df, p0, Nmax, TOL):
    print('index        Pn             f(Pn)')
    n = 0
    while n <= Nmax:
        p = p0 - (f(p0)/ df(p0))
        print(f' {n:2d}    {p:3.15f}    {f(p):3.15f}')
        if np.abs(p - p0) < TOL: 
            print(f'Methound succeded after {n} iterations, found: {p}')
            return
        n += 1
        p0 = p #update p
    print(f'Methound failed after {Nmax} iterations, found: {p}')

f1 = lambda x: np.cos(x) - x
d_f1 = lambda x: - np.sin(x) - 1
# find root of f(x) = cos(x) - x
newtons_method(f1, df=d_f1, p0=np.pi/4, Nmax=17, TOL=pow(10, -10))
