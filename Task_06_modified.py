import numpy as np
print("--- PARAMETER CHANGE: observed memory 72 -> 80 GB ---")
A = np.array([[4.,2.],[8.,12.]])
for b in ([20.,72.],[20.,80.]):
    x = np.linalg.solve(A, np.array(b)); print("b =", b, "-> x =", np.round(x,4))
print("--- RELATED CASE: mesh currents in a three-loop circuit ---")
# 10 V source in loop 1, 5 V in loop 3 (opposing); resistances in ohms
R = np.array([[ 30., -10.,   0.],
              [-10.,  35., -15.],
              [  0., -15.,  40.]])
V = np.array([10., 0., -5.])
I = np.linalg.solve(R, V)
print("Mesh currents (A):", np.round(I, 5))
print("Residual norm:", np.linalg.norm(V - R@I))
print("Condition number of R:", round(np.linalg.cond(R), 2))
