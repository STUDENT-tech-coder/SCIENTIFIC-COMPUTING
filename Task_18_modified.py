import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
print("--- PARAMETER CHANGE: resistance 1000 -> 2000 ohms (time constant 1 s -> 2 s) ---")
for R in (1000.,2000.):
    s=solve_ivp(lambda t,V:[(5-V[0])/(R*0.001)],(0,5),[0.0],t_eval=np.linspace(0,5,200),rtol=1e-9,atol=1e-11)
    tau=R*0.001; i63=np.argmax(s.y[0]>=5*(1-np.exp(-1)))
    print(f"R={R:.0f}: tau={tau:.0f}s | V(5 s)={s.y[0,-1]:.4f} V | time to 63.2%: {s.t[i63]:.2f} s")
print("--- RELATED CASE: SIR epidemic (N=10000, beta=0.3, gamma=0.1, I0=10) ---")
N,beta,gamma=10000.,0.3,0.1
def sir(t,y):
    S,I,Rr=y; return [-beta*S*I/N, beta*S*I/N-gamma*I, gamma*I]
s=solve_ivp(sir,(0,160),[N-10,10,0],t_eval=np.linspace(0,160,321),rtol=1e-8,atol=1e-8)
S,I,Rr=s.y; ip=np.argmax(I)
print(f"R0 = {beta/gamma:.1f} | peak infected {I[ip]:.0f} on day {s.t[ip]:.0f} | final recovered {Rr[-1]:.0f} ({Rr[-1]/N:.1%})")
print("Conservation check (max |S+I+R-N|):", f"{np.max(np.abs(S+I+Rr-N)):.2e}")
plt.plot(s.t,S,label="Susceptible"); plt.plot(s.t,I,label="Infected"); plt.plot(s.t,Rr,label="Recovered")
plt.xlabel("Day"); plt.ylabel("People"); plt.title("SIR epidemic model"); plt.legend(); plt.grid(True); plt.show()
