import time


start_time = time.perf_counter_ns()


######################################
import sys

sys.path.insert(0, "../..")
from scanf import scanf
from math import ceil, sqrt, floor
from functools import reduce
from operator import mul

data = open("input.txt").read().splitlines()

tt = data[0].split(":")[1].strip().split()
dd = data[1].split(":")[1].strip().split()


def sol(t, d):
    ll, rr = (
        1 / 2 * (t - sqrt(t**2 - 4 * d)) + 1e-6,
        1 / 2 * (t + sqrt(t**2 - 4 * d)) - 1e-6,
    )
    n = floor(rr) - ceil(ll) + 1
    return n


part1 = reduce(mul, [sol(t, d) for t, d in zip(map(int, tt), map(int, dd))])
part2 = sol(int("".join(tt)), int("".join(dd)))
# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
