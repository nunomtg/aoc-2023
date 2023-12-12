import time

start_time = time.perf_counter_ns()

######################################
from functools import cache

data = map(str.split, open("input.txt").read().splitlines())
data = list(map(lambda x: (x[0], list(map(int, x[1].split(",")))), data))

data2 = []
for line, group in data:
    new_line = line + "?"
    new_line = new_line * 5
    new_line = new_line[:-1]
    data2.append((new_line, group * 5))


@cache
def count_arrangements(curr_pos, g, card_left, line, group):
    if curr_pos == len(line):
        if g[-1] == 0:
            g = g[:-1]
        return 1 if g == group else 0

    total_count = 0
    match line[curr_pos]:
        case "#":
            if g[-1] + 1 <= group[len(g) - 1]:
                total_count += count_arrangements(
                    curr_pos + 1, g[:-1] + (g[-1] + 1,), card_left, line, group
                )
        case ".":
            if g[-1] > 0:
                if g[-1] == group[len(g) - 1]:
                    total_count += count_arrangements(
                        curr_pos + 1, g + (0,), card_left, line, group
                    )
            else:
                total_count += count_arrangements(
                    curr_pos + 1, g, card_left, line, group
                )
        case "?":
            if card_left > 0 and g[-1] + 1 <= group[len(g) - 1]:
                total_count += count_arrangements(
                    curr_pos + 1, g[:-1] + (g[-1] + 1,), card_left - 1, line, group
                )
            if g[-1] > 0:
                if g[-1] == group[len(g) - 1]:
                    total_count += count_arrangements(
                        curr_pos + 1, g + (0,), card_left, line, group
                    )
            else:
                total_count += count_arrangements(
                    curr_pos + 1, g, card_left, line, group
                )
    return total_count


part1, part2 = 0, 0
for line, group in data:
    part1 += count_arrangements(
        0, (0,), sum(group) - line.count("#"), line, tuple(group)
    )
for line, group in data2:
    part2 += count_arrangements(
        0, (0,), sum(group) - line.count("#"), line, tuple(group)
    )

# print("Part 1:", part1)
# print("Part 2:", part2)
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
