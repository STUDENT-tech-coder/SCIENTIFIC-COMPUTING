import numpy as np
from scipy.optimize import minimize
def solve(cA,cB,capA,capB,req,x0=(5,3)):
    r=minimize(lambda z:cA*z[0]+cB*z[1],x0,method="SLSQP",bounds=[(0,None)]*2,
               constraints={"type":"ineq","fun":lambda z:capA*z[0]+capB*z[1]-req})
    return r
print("--- PARAMETER CHANGE: Type A cost 12 -> 8 ---")
for cA in (12,8):
    r=solve(cA,18,100,170,1000); print(f"cost A={cA}: A={r.x[0]:.3f}, B={r.x[1]:.3f}, cost={r.fun:.2f}")
print("--- RELATED CASE: matatu fleet to move at least 400 passengers per hour ---")
# 14-seater: KES 3000/trip, 33-seater: KES 6500/trip
r=solve(3000,6500,14,33,400,x0=(10,5))
print(f"Continuous: small={r.x[0]:.3f}, large={r.x[1]:.3f}, cost={r.fun:,.0f}")
best=None
for a in range(0,40):
    for b in range(0,20):
        if 14*a+33*b>=400:
            c=3000*a+6500*b
            if best is None or c<best[0]: best=(c,a,b,14*a+33*b)
print("Best whole-vehicle plan (cost, small, large, seats):",best)
print("Cost per seat: small", round(3000/14,1), "| large", round(6500/33,1))
