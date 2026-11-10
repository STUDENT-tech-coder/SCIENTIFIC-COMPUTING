import numpy as np
def cent(A):
    w,v = np.linalg.eig(A); i=np.argmax(w.real); vec=np.abs(v[:,i].real); return w[i].real, vec/vec.sum()
print("--- PARAMETER CHANGE: add the missing A-D link (network becomes complete) ---")
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]],float)
lam,c = cent(A); print("Original:", round(lam,4), np.round(c,4))
A2 = A.copy(); A2[0,3]=A2[3,0]=1
lam,c = cent(A2); print("Changed :", round(lam,4), np.round(c,4))
print("--- RELATED CASE: campus Wi-Fi, one core switch (S) and four access points ---")
nodes = ["Core","AP1","AP2","AP3","AP4"]
W = np.array([[0,1,1,1,1],
              [1,0,1,0,0],
              [1,1,0,0,0],
              [1,0,0,0,1],
              [1,0,0,1,0]],float)
lam,c = cent(W)
print("Dominant eigenvalue:", round(lam,4))
for n_,s in zip(nodes,c): print(f"{n_}: {s:.4f}")
