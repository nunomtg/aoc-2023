import time


start_time = time.perf_counter_ns()

######################################
import sys

sys.path.insert(0, "../..")
from scanf import scanf
from itertools import cycle
from math import lcm


data = open("input.txt").read().splitlines()

instr, d = data[0], {}
for line in data[2:]:
    curr, ll, rr = scanf("%s = \(%s, %s\)", line)  # Fix this in scanf
    d[curr] = (ll, rr)

start_points = [c for c in d.keys() if c.endswith("A")]

periods = []
for start in start_points:
    curr = start
    for c, i in enumerate(cycle(instr)):
        if curr.endswith("Z"):
            periods.append(c)
            break
        curr = d[curr][0] if i == "L" else d[curr][1]

part1 = periods[start_points.index("AAA")]
part2 = lcm(*periods)
# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
