import numpy as np
from scipy.interpolate import interp1d, CubicSpline
print("--- PARAMETER CHANGE: pretend the 11:00 reading (24.0 C) is missing ---")
h=np.array([8,9,10,11,12,13,14.]); T=np.array([18,20,22.5,24,25,25.5,25.])
mask=h!=11
lin=interp1d(h[mask],T[mask]); cub=CubicSpline(h[mask],T[mask])
print(f"True 24.00 | linear {float(lin(11)):.2f} (err {abs(float(lin(11))-24):.2f}) | cubic {float(cub(11)):.2f} (err {abs(float(cub(11))-24):.2f})")
print("--- RELATED CASE: ADC calibration table for a temperature sensor ---")
adc=np.array([0,200,400,600,800,1023.]); temp=np.array([-10,8,26,45,66,90.])
lin=interp1d(adc,temp); cub=CubicSpline(adc,temp)
for q in (100,500,950):
    print(f"ADC {q}: linear {float(lin(q)):.2f} C | cubic {float(cub(q)):.2f} C")
try:
    lin(1100)
except ValueError as e:
    print("ADC 1100 (outside table) -> ValueError:", str(e)[:60])
