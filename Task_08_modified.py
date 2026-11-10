import numpy as np, matplotlib.pyplot as plt
def jacobi(A,b,tol,mi=5000):
    D=np.diag(A); R=A-np.diagflat(D); x=np.zeros_like(b); e=[]
    for _ in range(mi):
        xn=(b-R@x)/D; err=np.linalg.norm(xn-x,np.inf); e.append(err); x=xn
        if err<tol: break
    return x,e
def gs(A,b,tol,mi=5000):
    x=np.zeros_like(b); e=[]
    for _ in range(mi):
        old=x.copy()
        for i in range(len(b)):
            x[i]=(b[i]-A[i,:i]@x[:i]-A[i,i+1:]@old[i+1:])/A[i,i]
        err=np.linalg.norm(x-old,np.inf); e.append(err)
        if err<tol: break
    return x,e
def tri(n): return 2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
print("--- PARAMETER CHANGE: tolerance 1e-8 -> 1e-3 (5 grid points, 100 C / 20 C) ---")
A=tri(5); b=np.array([100.,0,0,0,20.]); ex=np.linalg.solve(A,b)
for tol in (1e-8,1e-3):
    xj,ej=jacobi(A,b,tol); xg,eg=gs(A,b,tol)
    print(f"tol={tol:g}: Jacobi {len(ej)} it, max error {np.max(abs(xj-ex)):.2e}; GS {len(eg)} it, max error {np.max(abs(xg-ex)):.2e}")
print("--- RELATED CASE: metal rod, 8 interior points, ends held at 80 C and 30 C ---")
n=8; A=tri(n); b=np.zeros(n); b[0]=80; b[-1]=30; ex=np.linalg.solve(A,b)
xj,ej=jacobi(A,b,1e-8); xg,eg=gs(A,b,1e-8)
print("Direct :", np.round(ex,3)); print("GS     :", np.round(xg,3))
print(f"Iterations: Jacobi {len(ej)}, Gauss-Seidel {len(eg)}")
plt.semilogy(ej,label="Jacobi"); plt.semilogy(eg,label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change"); plt.title("Rod model: convergence"); plt.legend(); plt.grid(True); plt.show()
