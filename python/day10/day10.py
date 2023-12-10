import time

start_time = time.perf_counter_ns()

######################################
import networkx as nx

data = open("input.txt").read().splitlines()

R, C = len(data), len(data[0])
g = nx.create_empty_copy(nx.grid_2d_graph(R, C))
start_pos = None

for r in range(R):
    for c in range(C):
        match data[r][c]:
            case "|":
                # Up
                if r > 0 and data[r - 1][c] in "|7F":
                    g.add_edge((r, c), (r - 1, c))
                # Down
                if r < R - 1 and data[r + 1][c] in "|LJ":
                    g.add_edge((r, c), (r + 1, c))
            case "-":
                # Left
                if c > 0 and data[r][c - 1] in "-FL":
                    g.add_edge((r, c), (r, c - 1))
                # Right
                if c < C - 1 and data[r][c + 1] in "-J7":
                    g.add_edge((r, c), (r, c + 1))
            case "L":
                # Up
                if r > 0 and data[r - 1][c] in "|7F":
                    g.add_edge((r, c), (r - 1, c))
                # Right
                if c < C - 1 and data[r][c + 1] in "-J7":
                    g.add_edge((r, c), (r, c + 1))
            case "J":
                # Up
                if r > 0 and data[r - 1][c] in "|7F":
                    g.add_edge((r, c), (r - 1, c))
                # Left
                if c > 0 and data[r][c - 1] in "-FL":
                    g.add_edge((r, c), (r, c - 1))
            case "7":
                # Down
                if r < R - 1 and data[r + 1][c] in "|LJ":
                    g.add_edge((r, c), (r + 1, c))
                # Left
                if c > 0 and data[r][c - 1] in "-FL":
                    g.add_edge((r, c), (r, c - 1))
            case "F":
                # Down
                if r < R - 1 and data[r + 1][c] in "|LJ":
                    g.add_edge((r, c), (r + 1, c))
                # Right
                if c < C - 1 and data[r][c + 1] in "-J7":
                    g.add_edge((r, c), (r, c + 1))
            case ".":
                pass
            case "S":
                start_pos = (r, c)
                up, down, left, right = False, False, False, False
                if data[r - 1][c] in "|7F":
                    up = True
                    g.add_edge((r, c), (r - 1, c))
                if data[r + 1][c] in "|LJ":
                    down = True
                    g.add_edge((r, c), (r + 1, c))
                if data[r][c - 1] in "-FL":
                    left = True
                    g.add_edge((r, c), (r, c - 1))
                if data[r][c + 1] in "-J7":
                    right = True
                    g.add_edge((r, c), (r, c + 1))
                match (up, down, left, right):
                    case (True, True, False, False):
                        S = "|"
                    case (False, False, True, True):
                        S = "-"
                    case (True, False, False, True):
                        S = "L"
                    case (True, False, True, False):
                        S = "J"
                    case (False, True, True, False):
                        S = "7"
                    case (False, True, False, True):
                        S = "F"
                data[r] = data[r][:c] + S + data[r][c + 1 :]
            case _:
                assert False

path = nx.find_cycle(g, start_pos)

part1 = len(path) // 2

bound = [pos[0] for pos in path]
part2 = 0

for r in range(R):
    n = 0
    for c in range(C):
        if (r, c) in bound:
            if data[r][c] in "LJ|":
                n += 1
            continue

        if n % 2:
            part2 += 1

# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
