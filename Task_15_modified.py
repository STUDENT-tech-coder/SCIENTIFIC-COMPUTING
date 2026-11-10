import numpy as np
def speeds(t,x): return np.gradient(x,t)
t=np.arange(7.); x=np.array([0,4.8,10.2,16.1,22.7,30.0,38.0])
print("--- PARAMETER CHANGE: GPS glitch, position at t=3 s changed 16.1 -> 19.1 m ---")
x2=x.copy(); x2[3]=19.1
print("Original speeds:", np.round(speeds(t,x),2)); print("Glitched speeds:", np.round(speeds(t,x2),2))
print("--- Step-size effect on f(x)=sin(x) at x=1 (true f' = cos(1) = 0.540302) ---")
for h in (0.1,0.01,1e-4,1e-8,1e-12):
    fwd=(np.sin(1+h)-np.sin(1))/h; cen=(np.sin(1+h)-np.sin(1-h))/(2*h)
    print(f"h={h:.0e}: forward err {abs(fwd-np.cos(1)):.2e} | central err {abs(cen-np.cos(1)):.2e}")
print("--- RELATED CASE: bus acceleration from speed log (km/h every 5 s) ---")
ts=np.arange(0,35,5.); v=np.array([0,18,31,41,48,52,54])/3.6
a=np.gradient(v,ts)
for tt,vv,aa in zip(ts,v,a): print(f"t={tt:>2.0f}s  speed={vv:5.2f} m/s  accel={aa:5.2f} m/s^2")
