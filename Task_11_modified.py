from scipy.optimize import root_scalar
def make(cf):
    npv=lambda r: sum(c/(1+r)**t for t,c in enumerate(cf))
    d=lambda r: sum(-t*c/(1+r)**(t+1) for t,c in enumerate(cf) if t>0)
    return npv,d
print("--- PARAMETER CHANGE: initial investment 10000 -> 9000 ---")
for inv in (10000,9000):
    npv,d=make([-inv,3000,3500,4000,2500])
    r=root_scalar(npv,fprime=d,x0=0.1,method="newton",xtol=1e-12)
    print(f"Investment {inv}: IRR = {r.root:.4%} ({r.iterations} Newton iterations)")
print("--- RELATED CASE: true interest rate on a loan ---")
# Receive 100,000 KES, repay 9,500 KES monthly for 12 months
cf=[100000]+[-9500]*12
npv,d=make(cf)
m=root_scalar(npv,fprime=d,x0=0.02,method="newton",xtol=1e-12)
s=root_scalar(npv,x0=0.01,x1=0.03,method="secant",xtol=1e-12)
print(f"Monthly rate (Newton): {m.root:.6%} | (Secant): {s.root:.6%}")
print(f"Nominal annual (x12): {12*m.root:.4%} | Effective annual: {(1+m.root)**12-1:.4%}")
print(f"Total repaid: {9500*12:,} KES -> interest paid {9500*12-100000:,} KES")
