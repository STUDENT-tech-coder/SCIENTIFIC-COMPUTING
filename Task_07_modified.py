import numpy as np, time
from scipy.linalg import lu_factor, lu_solve
print("--- PARAMETER CHANGE: diagonal 4 -> 6 (stronger coupling to ground) ---")
A1 = np.array([[4.,-1,0],[-1,4,-1],[0,-1,3]]); A2 = np.array([[6.,-1,0],[-1,6,-1],[0,-1,5]])
b = np.array([15.,10,10])
print("Original:", np.round(np.linalg.solve(A1,b),4)); print("Changed :", np.round(np.linalg.solve(A2,b),4))
print("--- RELATED CASE: 500 x 500 structural model, 2000 load vectors ---")
rng = np.random.default_rng(1); n=500
M = rng.random((n,n)) + n*np.eye(n)
loads = rng.random((n, 2000))
t0=time.perf_counter()
for j in range(2000): np.linalg.solve(M, loads[:,j])
t_repeat = time.perf_counter()-t0
t0=time.perf_counter(); lu,piv = lu_factor(M)
for j in range(2000): lu_solve((lu,piv), loads[:,j])
t_lu = time.perf_counter()-t0
x_ref = np.linalg.solve(M, loads[:,0]); x_lu = lu_solve((lu,piv), loads[:,0])
print(f"Re-solve every time: {t_repeat:.2f}s | LU once + reuse: {t_lu:.2f}s | ratio {t_repeat/t_lu:.1f}x")
print("Max difference between methods:", np.max(np.abs(x_ref-x_lu)))
