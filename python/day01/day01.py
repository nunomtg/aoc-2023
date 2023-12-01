# import time

# # Start the timer
# start_time = time.perf_counter_ns()
############################################
############################################
############################################
import re

input = open("input.txt", "r").read()

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

pattern_1 = re.compile(r"(1|2|3|4|5|6|7|8|9)")
pattern_2 = re.compile(
    r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
)
sum_1, sum_2 = 0, 0

for line in input.split("\n"):
    g_1, g_2 = pattern_1.findall(line), pattern_2.findall(line)
    sum_1 += numbers[g_1[0]] * 10 + numbers[g_1[-1]]
    sum_2 += numbers[g_2[0]] * 10 + numbers[g_2[-1]]

# print(f"Part 1: {sum_1}\nPart 2: {sum_2}")
############################################
############################################
############################################

# end_time = time.perf_counter_ns()
# execution_time = end_time - start_time

# print(f"Python program executed in {execution_time*1e-6:.3f} ms")
