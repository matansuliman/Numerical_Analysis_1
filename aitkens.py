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
def aitkens_method(f, p0, Nmax, TOL):
    #print('index        Pn             f(Pn)')
    n = 0
    p_prev = p0  # Store the previous value of p
    p_prev_prev = p0  # Store the value before the previous value of p

    p_hat_prev = -1
    p_hat = -1

    numerator = lambda p0, p1: np.power(p1 - p0, 2)
    denominator = lambda p0, p1, p2: (p2 - 2*p1 + p0)
    hat = lambda p0, p1, p2: p0 - (numerator(p0, p1) / denominator(p0, p1, p2))

    while n <= Nmax:
        p = f(p0)
        if n >= 2:
            if denominator(p_prev_prev, p_prev, p0) == 0:
                print(f'Method failed (division by 0) after {n-2} iterations, found: {p_hat}')
                return n-2
            else: p_hat = hat(p_prev_prev, p_prev, p0)
            print(f' {n-2:2d}    {p_hat:3.15f}    {f(p_hat):3.15f}')
        if n >= 3:
            if np.abs(p_hat - p_hat_prev) < TOL:
                print(f'Method succeeded after {n-2} iterations, found: {p_hat}')
                return n-2
        
        n += 1
        p_prev_prev = p_prev  # Update the value before the previous value of p
        p_prev = p0  # Update the previous value of p
        p0 = p  # Update Pn
        p_hat_prev = p_hat
    print(f'Method failed after {Nmax} iterations, found: {p0}')
    return Nmax