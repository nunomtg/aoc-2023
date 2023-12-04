import time


start_time = time.perf_counter_ns()


######################################
import sys

sys.path.insert(0, "../..")
from scanf import scanf
from collections import deque

data = open("input.txt").read().splitlines()
scores = []
for card in data:
    ll, rr = scanf("%s \| %s", scanf("%s: %s", card)[1])
    got_right = set(ll.split()) & set(rr.split())
    scores.append(len(got_right))
score_1 = sum(map(lambda x: 2 ** (x - 1) if x > 0 else 0, scores))
score_2, q = 0, deque(range(len(scores)))
while q:
    score_2 += 1
    curr_card = q.popleft()
    q.extend(range(curr_card + 1, curr_card + scores[curr_card] + 1))
# print(f"Part 1: {score_1}")
# print(f"Part 2: {score_2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
