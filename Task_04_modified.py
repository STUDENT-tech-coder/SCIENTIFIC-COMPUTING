import numpy as np, math
from decimal import Decimal
print("--- PARAMETER CHANGE: approximation 1.414 -> 1.4142 ---")
t = np.sqrt(2)
for a in (1.414, 1.4142, 1.41421356):
    ae = abs(t-a); print(f"approx={a}: absolute={ae:.2e}, relative={ae/t:.4%}")
print("--- RELATED CASE: adding 0.10 KES one million times ---")
s = 0.0
for _ in range(1_000_000): s += 0.10
print(f"Naive float sum   : {s:.10f}")
print(f"math.fsum         : {math.fsum([0.10]*1_000_000):.10f}")
d = sum([Decimal('0.10')]*1_000_000)
print(f"Decimal sum       : {d}")
print(f"Drift (naive-exact): {s-100000:.3e} KES")
print("Equal to 100000.0?", s == 100000.0, "| isclose?", np.isclose(s, 100000.0))
