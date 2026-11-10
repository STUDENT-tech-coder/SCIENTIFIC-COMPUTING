import numpy as np
from scipy.integrate import simpson
print("--- PARAMETER CHANGE: evening peak raised from 1.8 to 2.4 kW (reading at t=6 h) ---")
t=np.array([0,2,4,6,8,10,12.]); p=np.array([0.8,1.0,1.4,1.8,1.6,1.2,0.9]); p2=p.copy(); p2[3]=2.4
for name,pp in (("original",p),("changed",p2)):
    print(f"{name}: trapezoid {np.trapezoid(pp,t):.3f} kWh | Simpson {simpson(pp,x=t):.3f} kWh")
print("--- Accuracy check on a known integral: integral of sin(x), 0..pi = 2 ---")
for n in (5,9,17):
    x=np.linspace(0,np.pi,n); print(f"n={n:>2}: trapezoid err {abs(np.trapezoid(np.sin(x),x)-2):.2e} | Simpson err {abs(simpson(np.sin(x),x=x)-2):.2e}")
print("--- RELATED CASE: river discharge (m^3/s) logged hourly, total volume ---")
th=np.arange(0,7.)*3600; q=np.array([12,15,24,38,41,29,20.])
vol_t=np.trapezoid(q,th); vol_s=simpson(q,x=th)
print(f"Trapezoid {vol_t:,.0f} m^3 | Simpson {vol_s:,.0f} m^3 | difference {abs(vol_t-vol_s):,.0f} m^3")
print(f"Mean discharge {vol_t/th[-1]:.2f} m^3/s")
