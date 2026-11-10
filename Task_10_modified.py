import numpy as np
from scipy.optimize import root_scalar
print("--- PARAMETER CHANGE: heat-gain coefficient 10 -> 40 ---")
for c in (10,40):
    f=lambda T: T-25-c*np.exp(-T/20)
    r=root_scalar(f,bracket=[20,60],method="bisect",xtol=1e-10)
    g=lambda T: 25+c*np.exp(-T/20); T=30.0; n=0
    for n in range(1,200):
        Tn=g(T)
        if abs(Tn-T)<1e-10: T=Tn; break
        T=Tn
    print(f"c={c}: bisection {r.root:.6f} C ({r.iterations} it) | fixed-point {T:.6f} C ({n} it) | |g'(root)|={c/20*np.exp(-r.root/20):.3f}")
print("--- RELATED CASE: bakery break-even quantity ---")
# Revenue 450 KES/loaf-box; cost = 60000 fixed + 120/unit + 0.002*q^2 (overtime)
def profit(q): return 450*q-(60000+120*q+0.002*q**2)
r=root_scalar(profit,bracket=[1,400],method="bisect",xtol=1e-6)
print(f"First break-even quantity: {r.root:.2f} units ({r.iterations} bisection steps)")
r2=root_scalar(profit,bracket=[1000,200000],method="bisect",xtol=1e-6)
print(f"Second break-even (overtime costs overtake revenue): {r2.root:.1f} units")
print(f"Profit at 100000 units: KES {profit(100000):,.0f}")
