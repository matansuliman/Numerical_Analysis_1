import numpy as np

# bisection method
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
        print(f' {n:2d}    {a:3.15f}  {c:3.15f}  {b:3.15f}  {f(c):3.15f}')
        if f(c) == 0 or (b-a)/2 < TOL: 
            print(f'Methound succeded after {n} iterations, found: {c}')
            return
        else: n += 1
        if np.sign(f(a)) == np.sign(f(c)): a = c
        else: b = c
    print(f'Methound failed after {Nmax} iterations, found: {c}')


f1 = lambda x: np.exp(x) - 1
# find x when e^x - 1 = 0
bisect(f1, a=-2.5, b=1, Nmax=25, TOL=pow(10, -5))
print(f'the actual root is x=0')
