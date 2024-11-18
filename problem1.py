import numpy as np
import pandas as pd

h = 1/4
t0 = 0
w0 = 0
t_end = 1


def rk_step(f, t, w, h):
    s1 = f(t, w)
    s2 = f(t + h / 2, w + h / 2 * s1)
    s3 = f(t + h / 2, w + h / 2 * s2)
    s4 = f(t + h, w + h * s3)
    w_inext = w + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4)

    return w_inext, (s1, s2, s3, s4)

def solve_rk4(f, t0, w0, t_end, h):
    results = []
    t = t0
    w = w0

    while (t <= t_end):
        w_inext, (s1, s2, s3, s4) = rk_step(f, t, w, h)
        print(f"{t:<15} {w:<20} {s1:<20} {s2:<20} {s3:<20} {s4:<20}")
        w = w_inext
        t+=h
    return results

def dif_eq(t, y):
    return t + y

print(f"{'t':<15} {'w':<20} {'s1':<20} {'s2':<20} {'s3':<20} {'s4':<20}")
print("=" * 120)
results = solve_rk4(dif_eq, t0, w0, t_end, h)
