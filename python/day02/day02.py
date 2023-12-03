import time

start_time = time.perf_counter_ns()

######################################
import sys

sys.path.insert(0, "../..")
from scanf import scanf

input = open("input.txt", "r").read().splitlines()

score1, score2 = 0, 0

for line in input:
    good_game = True
    id, events = scanf("Game %d:%s", line)
    master_counter = {"green": 0, "red": 0, "blue": 0}

    for event in events.split(";"):
        counter = {"green": 0, "red": 0, "blue": 0}
        for d in event.split(","):
            num, color = scanf(" %d %s", d)
            counter[color] += int(num)

        for color in counter:
            master_counter[color] = max(master_counter[color], counter[color])

        if counter["red"] > 12 or counter["green"] > 13 or counter["blue"] > 14:
            good_game = False

    if good_game:
        score1 += id

    score2 += master_counter["red"] * master_counter["green"] * master_counter["blue"]


# print(f"Part 1: {score_1}\nPart 2: {score_2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
