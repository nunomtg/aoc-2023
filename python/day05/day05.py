import time


start_time = time.perf_counter_ns()


######################################
import sys

sys.path.insert(0, "../..")
from scanf import scanf
from collections import deque
from dataclasses import dataclass

data = open("input.txt").read().splitlines()
data.append("")


@dataclass
class SMap:
    x1: int
    x2: int

    def get_next(self, origin, delta):
        y1, y2 = origin

        if y2 < self.x1 or self.x2 < y1:
            return None, None

        new_x1 = max(self.x1, y1) + delta
        new_x2 = min(self.x2, y2) + delta

        to_change = [
            SMap(start, end)
            for start, end in [(self.x1, y1 - 1), (y2 + 1, self.x2)]
            if start < end
        ]

        return SMap(new_x1, new_x2), to_change if to_change else None


def solve_for_init_range(ranges):
    for line in data[2:]:
        if line.endswith(":"):
            rules, new_ranges, q = [], [], deque(ranges)
        elif line == "":
            while q:
                r = q.popleft()
                for rule in rules:
                    match r.get_next(rule[0], rule[1]):
                        case (None, None):
                            continue
                        case (good, None):
                            new_ranges.append(good)
                            break
                        case (good, check_again):
                            q.extend(check_again)
                            new_ranges.append(good)
                            break
                else:
                    new_ranges.append(r)
            ranges = new_ranges
        else:
            d, o, length = scanf("%d %d %d", line)
            rules.append(((o, o + length - 1), d - o))
    return min(map(lambda x: x.x1, ranges))


initial_ranges = list(map(int, data[0].split(": ")[1].split()))
# can't wait to be able to use 3.12 so I can use batched() <3
part1 = solve_for_init_range([SMap(a, a) for a in initial_ranges])
part2 = solve_for_init_range(
    [SMap(a, a + b - 1) for a, b in zip(initial_ranges[::2], initial_ranges[1::2])]
)
# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
