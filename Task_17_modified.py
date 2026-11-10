import numpy as np, matplotlib.pyplot as plt
def euler_cool(h,T0=90,Ta=25,k=0.12,end=30):
    t=np.arange(0,end+h/2,h); T=np.zeros_like(t); T[0]=T0
    for i in range(len(t)-1): T[i+1]=T[i]+h*(-k*(T[i]-Ta))
    return t,T
ex=lambda t: 25+65*np.exp(-0.12*t)
print("--- PARAMETER CHANGE: step size h ---")
plt.plot(np.linspace(0,30,300),ex(np.linspace(0,30,300)),label="Exact")
for h in (5.0,1.0,0.1):
    t,T=euler_cool(h); print(f"h={h}: T(30)={T[-1]:.3f} C | error {abs(T[-1]-ex(30)):.4f} C")
    plt.plot(t,T,marker="o" if h>=1 else None,markersize=3,label=f"Euler h={h}")
plt.xlabel("Time (minutes)"); plt.ylabel("Temperature (C)"); plt.title("Effect of step size on Euler cooling"); plt.legend(); plt.grid(True); plt.show()
print("--- RELATED CASE: fish population in a pond (logistic growth), h = 1 month ---")
r,K,P0=0.3,5000.,200.
P=[P0]
for m in range(24): P.append(P[-1]+1.0*r*P[-1]*(1-P[-1]/K))
exact=lambda t: K/(1+(K-P0)/P0*np.exp(-r*t))
for m in (6,12,18,24): print(f"month {m:>2}: Euler {P[m]:8.1f} | exact {exact(m):8.1f} | error {abs(P[m]-exact(m)):6.1f}")
