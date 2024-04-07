import numpy as np
import matplotlib.pyplot as plt

# newtons divided difference formula
# prerequisites:
#   all X0,...,Xn are distinct numbers
# @param X0,...,Xn
# @param f(X0),...,f(Xn)
def newtons_divided_difference_formula(x_arr, fx_arr):
    n = len(x_arr)
    F = [ [0 for i in range(n)] for j in range(n)]
    for j in range(n): F[0][j] = fx_arr[j]
    
    for i in range(1, n):
        for j in range(1,i+1):
            numerator = F[j-1][i] - F[j-1][i-1]
            denominator = x_arr[i] - x_arr[i-j]
            F[j][i] = numerator / denominator
            #print(f'({j},{i}) = ( ({j-1},{i}) - ({j-1},{i-1}) ) / X{i} - X{i-j}')
            #print(f'({j},{i}) = {F[j][i]}')
    
    P = [F[i][i] for i in range(1, n)]
    return F, P


def printF(F):
    print('F:')
    for i in range(len(F)):
        for j in range(len(F)):
            print(f'({i},{j}) {F[i][j]:3.7f}', end=" ")
        print()
    print('')


f1 = lambda x: 1 / (1 + pow(x,2))
xi_formula = lambda i,n: -5+10*((i-1)/(n-1))


def interpolatory_polynomial(x, x_arr, F):
        val = F[0][0]
        for i in range(1,len(F)):
            temp = F[i][i]
            for j in range(i): temp = temp * (x - x_arr[j])
            val += temp
        return val

def print_interpolatory_polynomial(x, x_arr, F):
        print(f'P{len(F)-1}(x) = %.7f' % F[0][0], end='')
        for i in range(1,len(F)):
            print(f' %+.7f' % F[i][i], end='*')
            for j in range(i):
                print(f'(x%+.1f)' % x_arr[j], end='')
        print('')

x = np.linspace(-5,5)
n_arr = [5]

#example 1 in page 124
x_arr = [1.0,1.3,1.6,1.9,2.2]
fx_arr =[0.7651977,0.6200860,0.4554022,0.2818186,0.1103623] 
F, P = newtons_divided_difference_formula(x_arr=x_arr, fx_arr=fx_arr)
print(x_arr)
print(fx_arr)
printF(F)
print_interpolatory_polynomial(x, x_arr, F)
print(f'P4(1.5) = {interpolatory_polynomial(1.5, x_arr=x_arr, F=F):2.7f}')
print(f'P4(1.1) = {interpolatory_polynomial(1.1, x_arr=x_arr, F=F):2.7f}')
print(f'P4(2.0) = {interpolatory_polynomial(2.0, x_arr=x_arr, F=F):2.7f}')
#plt.plot(x, interpolatory_polynomial(x, x_arr=x_arr, F=F), label=f'exmple')


for n_i in n_arr:
    x_arr = [xi_formula(i,n_i) for i in range(n_i)]
    fx_arr = [f1(xi) for xi in x_arr]
    F, P = newtons_divided_difference_formula(x_arr=x_arr, fx_arr=fx_arr)
    print(fx_arr)
    print(x_arr)
    printF(F)
    print_interpolatory_polynomial(x, x_arr, F)
    plt.plot(x, interpolatory_polynomial(x, x_arr=x_arr, F=F), label=f'n={n_i}')

plt.plot(x, f1(x), label='1/(1+x^2)')
plt.ylim(-1,8)
plt.legend(loc='upper center')
plt.show()