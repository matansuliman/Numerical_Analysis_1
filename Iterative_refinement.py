import numpy as np


def Gaussian_Elimination_Scaled_Partial_Pivoting(n, A):
    
   #step 1 - Init row pointer and s
    NROW = np.zeros(n)
    s = np.zeros(n)
    for i in range(n):
        #find s
        s[i] = abs(A[i][0])
        for j in range(n): s[i] = max(s[i], abs(A[i][j]))
        if(s[i] == 0):
            print("No unique solution exists")
            return
        else: NROW[i] = i

    #step 2 - Elimination process
    M = np.zeros((n, n)) # multipliers matrix
    for i in range(n-1):

        #step 3
        p = i
        for j in range(i+1, n):
            if(abs(A[int(NROW[j])][i]) / s[int(NROW[j])] > abs(A[int(NROW[p])][i])  / s[int(NROW[p])]):
                p = j

        #step 4
        if(A[int(NROW[p])][i] == 0):
            print("No unique solution exists")
            return
        
        #step 5 - Simulated row interchange
        if(NROW[i] != NROW[p]):
            NCOPY = NROW[i]
            NROW[i] = NROW[p]
            NROW[p] = NCOPY

        #step 6
        for j in range(i+1, n):

            #step 7 - calculate multiplier
            m = A[int(NROW[j])][i] / A[int(NROW[i])][i]
            M[int(NROW[j])][i] = m #save multipliers
            
            #step 8 - Applay elimination
            for p in range(i, n+1):
                A[int(NROW[j])][p] -= m * A[int(NROW[i])][p]
        
    #step 9
    if(A[int(NROW[n-1])][n-1] == 0):
        print("No unique solution exists")
        return

    #step 10 - start backward substitution
    x = np.zeros(n) # solution
    x[n-1] = A[int(NROW[n-1])][n] / A[int(NROW[n-1])][n-1]

    #step 11
    for i in range(n-2, -1, -1): # from index n-1 to 0
        x[i] = A[int(NROW[i])][n]
        for j in range(i+1, n): x[i] -= A[int(NROW[i])][j] * x[j]
        x[i] /= A[int(NROW[i])][i]

    #step 12 - procedure completed successfully
    return x, M, NROW

"""
@param n - number of equations and unknowns
@param A - matrix plus b solution vector
@param N - maximum number of iterations
@param TOL - tolarence
@param t - number of digits of precision
"""
def Iterative_refinement(n, A, N, TOL, t):

    b = [A[i][n] for i in range(n)] #init b

    #step 0
    x, M, NROW = Gaussian_Elimination_Scaled_Partial_Pivoting(n, np.copy(A))
    COND = -1

    #step 1
    k = 1

    #step 2
    xx = np.zeros(n)
    while(k <= N):

        #step 3
        r = np.copy(b)
        for i in range(n):
            for j in range(n): r[i] -= A[i][j] * x[j]

        #step 4
        for i in range(n): A[i][n] = r[i]
        y = Gaussian_Elimination_Scaled_Partial_Pivoting(n, np.copy(A))[0]

        xx = x + y #step 5

        #step 6
        if(k == 1): COND = pow(10, t) * np.linalg.norm(y, np.inf) / np.linalg.norm(xx, np.inf)

        #step 7 - procedure was successful
        if(np.linalg.norm(x - xx, np.inf) < TOL): 
            print(f"xx: {xx}")
            print(f"COND: {COND}")
            print(f"iterations: {k}")
            return

        k += 1 #step 8
        x = xx #step 9

    #step 10 - procedure was unsuccessful
    print("Maximum number of iterations exceeded")
    print(COND)
    return

A = [
    [4, 1.33, 0, 5.33],
    [3, 1, 1, 5],
    [3, 2, 1, 6]
]
n = 3
N = 10
TOL = pow(10, -3)
t = 5
Iterative_refinement(n, A, N, TOL, t)