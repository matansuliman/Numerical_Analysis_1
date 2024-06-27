import numpy as np

def Gaussian_Elimination_Scaled_Partial_Pivoting(n, A):
    
    #step 1 - Init row pointer and s
    NROW = np.zeros(n)
    s = np.zeros(n)
    for i in range(n):
        #find s
        s[i] = A[i][0]
        for j in range(n): s[i] = max(s[i], A[i][j])
        if(s[i] == 0):
            print("No unique solution exists")
            return
        else: NROW[i] = i

    #step 2 - Elimination process
    for i in range(n-1):

        #step 3 - find p
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
            
            #step 8 - Apply elimination
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
    print(x)
    return

#init the matrix with the solution b => [A|b]
A = [
    [4, 1.33, 0, 5.33],
    [3, 1, 1, 5],
    [3, 2, 1, 6]
]
n = 3
Gaussian_Elimination_Scaled_Partial_Pivoting(n, A)