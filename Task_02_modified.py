import numpy as np
print("--- PARAMETER CHANGE: one reading replaced by a 40 C spike ---")
t = np.array([18.5,18.0,17.8,17.5,17.9,19.0,21.5,23.8,25.6,27.1,28.3,29.0,
              29.4,29.1,28.5,27.6,26.2,24.8,23.4,22.1,21.0,20.2,19.6,19.0])
t2 = t.copy(); t2[12] = 40.0
print(f"Original mean {t.mean():.2f}  max {t.max():.2f}")
print(f"Changed  mean {t2.mean():.2f}  max {t2.max():.2f}  median {np.median(t2):.2f}")
print("--- RELATED CASE: cold-storage sensor ---")
cs = np.array([3.2,3.5,3.9,4.4,5.1,6.0,7.2,8.6,9.1,7.4,5.8,4.6])
mean_c = cs.mean(); k = cs + 273.15
alarm = cs > 8.0
print(f"Mean {mean_c:.2f} C, min {cs.min():.1f}, max {cs.max():.1f}")
print("Readings above 8 C at positions:", np.where(alarm)[0] + 1, "->", cs[alarm])
print("Fraction above threshold:", f"{alarm.mean():.1%}")
print("First three in Kelvin:", k[:3])
