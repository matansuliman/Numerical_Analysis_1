import numpy as np
import fixedPoint as fp
import aitkens as atk
import steffensens as stf


g1 = lambda x: np.cos(pow(x,2)) - 1
g2 = lambda x: x/2 + 2

Nmax = 20
TOL = 1e-5
p0_g1 = 1
p0_g2 = 2

print('----------fixed point--------------')
fp_g1 = fp.fixedPoint(g1, p0=p0_g1, Nmax=Nmax, TOL=TOL)
fp_g2 = fp.fixedPoint(g2, p0=p0_g2, Nmax=Nmax, TOL=TOL)
print('----------aitkens_method--------------')
atk_g1 = atk.aitkens_method(g1, p0=p0_g1, Nmax=Nmax, TOL=TOL)
atk_g2 = atk.aitkens_method(g2, p0=p0_g2, Nmax=Nmax, TOL=TOL)
print('----------steffensens_method--------------')
stf_g1 = stf.steffensens_method(g1, p0=p0_g1, Nmax=Nmax, TOL=TOL)
stf_g2 = stf.steffensens_method(g2, p0=p0_g2, Nmax=Nmax, TOL=TOL)


print( '      fp    atk    stf')
print(f'g1:  {fp_g1:3d}    {atk_g1:3d}   {stf_g1:3d}')
print(f'g2:  {fp_g2:3d}    {atk_g2:3d}   {stf_g2:3d}')




