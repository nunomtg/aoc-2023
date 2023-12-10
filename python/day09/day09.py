import time

start_time = time.perf_counter_ns()

######################################
from itertools import pairwise

data = open("input.txt").read().splitlines()


def calculate_line(line):
    nums = list(map(int, line.split()))
    first_nums, last_nums = [nums[0]], [nums[-1]]
    while True:
        nums = [x2 - x1 for x1, x2 in pairwise(nums)]
        if not sum(nums):
            return sum(last_nums), sum(first_nums[::2]) - sum(first_nums[1::2])
        first_nums.append(nums[0])
        last_nums.append(nums[-1])


part1, part2 = (sum(i) for i in zip(*[calculate_line(line) for line in data]))

# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
