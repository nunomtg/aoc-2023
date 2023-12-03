import time

start_time = time.perf_counter_ns()

######################################
from collections import defaultdict
from math import prod

data = open("input.txt").read().splitlines()
MAX_ROW, MAX_COL = len(data), len(data[0])


def adjacent(row, col):
    for dr, dc in [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]:
        r, c = row + dr, col + dc
        if 0 <= r < MAX_ROW and 0 <= c < MAX_COL:
            yield r, c


symbols, score_1, gears = "#$%&*+-/=@", 0, defaultdict(lambda: [])

for row in range(MAX_ROW):
    col = 0
    while col < MAX_COL:
        good, gear, num = False, None, ""
        while col < MAX_COL and data[row][col].isdigit():
            num += data[row][col]
            for r, c in adjacent(row, col):
                if data[r][c] in symbols:
                    good = True
                if data[r][c] == "*" and gear is None:
                    gear = (r, c)
            col += 1
        if good:
            score_1 += int(num)
        if gear:
            gears[gear].append(int(num))

        col += 1

score_2 = sum(prod(x) for x in gears.values() if len(x) > 1)
# print("Part 1:", score_1)
# print("Part 2:", score_2)
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
