import numpy as np, matplotlib.pyplot as plt
from scipy.stats import norm
print("--- PARAMETER CHANGE: capacity 1000 -> 1100, and N 100000 -> 1000 ---")
for cap,N,seed in ((1000,100_000,42),(1100,100_000,42),(1000,1_000,42),(1000,1_000,7),(1000,1_000,99)):
    d=np.random.default_rng(seed).normal(850,120,N); p=(d>cap).mean()
    print(f"capacity={cap}, N={N:>7,}, seed={seed}: estimate {p:.4%} | exact {norm.sf((cap-850)/120):.4%}")
print("--- RELATED CASE: will a 3-stage project finish within 30 days? ---")
rng=np.random.default_rng(42); N=200_000
design=rng.triangular(5,8,14,N); build=rng.triangular(10,14,25,N); test=rng.triangular(3,5,10,N)
total=design+build+test
print(f"Mean total {total.mean():.2f} days | 90th percentile {np.percentile(total,90):.2f} days")
print(f"P(total > 30 days) = {(total>30).mean():.2%} | P(total > 35) = {(total>35).mean():.2%}")
plt.hist(total,bins=60,color="0.6",edgecolor="black"); plt.axvline(30,color="black",linestyle="--",label="30-day deadline")
plt.xlabel("Total project duration (days)"); plt.ylabel("Frequency"); plt.title("Monte Carlo project duration"); plt.legend(); plt.show()
