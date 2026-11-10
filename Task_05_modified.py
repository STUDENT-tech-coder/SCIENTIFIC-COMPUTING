import numpy as np
def make(angle_deg, sx, sy):
    a = np.deg2rad(angle_deg)
    R = np.array([[np.cos(a), -np.sin(a)],[np.sin(a), np.cos(a)]])
    S = np.diag([sx, sy]); return R @ S
sq = np.array([[0,0],[1,0],[1,1],[0,1]], float)
print("--- PARAMETER CHANGE: angle 45 -> 90 degrees (scale unchanged) ---")
T = make(90, 2.0, 1.5)
print(np.round(sq @ T.T, 4)); print("det =", round(np.linalg.det(T), 4))
print("--- RELATED CASE: drone survey path, rotate 30 deg and scale to map (0.5) ---")
path = np.array([[0,0],[40,0],[40,30],[0,30],[0,0]], float)   # metres
T = make(30, 0.5, 0.5)
out = path @ T.T
print(np.round(out, 3)); print("det =", round(np.linalg.det(T), 4), "(area factor)")
side_before = np.linalg.norm(path[1]-path[0]); side_after = np.linalg.norm(out[1]-out[0])
print(f"First leg length: {side_before:.1f} -> {side_after:.1f}")
