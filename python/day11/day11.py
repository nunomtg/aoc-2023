import time

start_time = time.perf_counter_ns()

######################################
from dataclasses import dataclass
from itertools import combinations
from copy import deepcopy

data = open("input.txt").read().splitlines()
R, C = len(data), len(data[0])


@dataclass
class Galaxy:
    r: int
    c: int

    def dist(self, other):
        return abs(self.r - other.r) + abs(self.c - other.c)


galaxies = []
empty = []
row_count = [0 for _ in range(R)]
col_count = [0 for _ in range(C)]
for r in range(R):
    for c in range(C):
        if data[r][c] == "#":
            row_count[r] += 1
            col_count[c] += 1
            galaxies.append(Galaxy(r, c))

empty_rows = [r for r in range(R) if row_count[r] == 0]
empty_cols = [c for c in range(C) if col_count[c] == 0]

dr1, dr2 = [0 for _ in range(R)], [0 for _ in range(R)]
dc1, dc2 = [0 for _ in range(C)], [0 for _ in range(C)]
for r in empty_rows:
    for rr in range(r + 1, R):
        dr1[rr] += 1
        dr2[rr] += 1_000_000 - 1
for c in empty_cols:
    for cc in range(c + 1, C):
        dc1[cc] += 1
        dc2[cc] += 1_000_000 - 1

galaxies1 = galaxies
galaxies2 = deepcopy(galaxies)
for i in range(len(galaxies)):
    galaxies1[i].r += dr1[galaxies1[i].r]
    galaxies1[i].c += dc1[galaxies1[i].c]
    galaxies2[i].r += dr2[galaxies2[i].r]
    galaxies2[i].c += dc2[galaxies2[i].c]

part1 = sum(g1.dist(g2) for g1, g2 in combinations(galaxies1, 2))
part2 = sum(g1.dist(g2) for g1, g2 in combinations(galaxies2, 2))

# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
