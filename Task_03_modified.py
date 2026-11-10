import numpy as np, timeit
print("--- PARAMETER CHANGE: array size ---")
rng = np.random.default_rng(42)
for n in (100_000, 1_000_000, 3_000_000):
    x = rng.uniform(5, 250, n)
    def loop():
        out=[]
        for v in x:
            s=v/1000.0; out.append(s**2)
        return out
    def vec():
        return (x/1000.0)**2
    lt = timeit.timeit(loop, number=1); vt = timeit.timeit(vec, number=3)/3
    print(f"n={n:>9,}  loop={lt:.4f}s  vectorized={vt:.5f}s  speed-up={lt/vt:.0f}x")
print("--- RELATED CASE: mobile-money fees on 1,000,000 transactions ---")
amounts = rng.uniform(50, 70_000, 1_000_000)   # KES
def fee_loop():
    out=[]
    for a in amounts:
        out.append(min(max(a*0.01, 5.0), 108.0))
    return out
def fee_vec():
    return np.clip(amounts*0.01, 5.0, 108.0)
lt = timeit.timeit(fee_loop, number=1); vt = timeit.timeit(fee_vec, number=3)/3
f = fee_vec()
print(f"Mean fee KES {f.mean():.2f}; total fees KES {f.sum():,.0f}; capped at 108: {(f==108).mean():.1%}")
print(f"loop={lt:.3f}s vectorized={vt:.4f}s speed-up={lt/vt:.0f}x")
