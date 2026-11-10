import numpy as np
from scipy.optimize import root
print("--- PARAMETER CHANGE: circle radius 2 -> 3 (x^2+y^2=9) with the same parabola ---")
def eq(r):
    return lambda z: [z[0]**2+z[1]**2-r**2, z[1]-(z[0]**2-1)]
for guess in ([1.,1.],[-1.,1.]):
    s=root(eq(3),guess); print("guess",guess,"->",np.round(s.x,5),"converged:",s.success,"res",np.round(eq(3)(s.x),10))
print("--- RELATED CASE: cell-tower coverage circle vs a curved road ---")
# Tower at (2,1), radius 5 km. Road: y = 0.05 x^2 + 0.2 x - 3
def eq2(z):
    x,y=z; return [(x-2)**2+(y-1)**2-25, y-(0.05*x**2+0.2*x-3)]
for guess in ([6.,0.],[-5.,0.],[0.,-3.]):
    s=root(eq2,guess); print("guess",guess,"->",np.round(s.x,4),"converged:",s.success,"max|res|:",f"{np.max(np.abs(eq2(s.x))):.1e}")
