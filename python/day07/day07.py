import time


start_time = time.perf_counter_ns()

######################################
import sys

sys.path.insert(0, "../..")
from scanf import scanf
from dataclasses import dataclass
from collections import Counter


def get_card_rank(card, part: str):
    if part == "2":
        c = Counter(card)
        if c["J"] == 5:
            return 6
        most_common = c.most_common(1)[0][0]

        card = card.replace(
            "J", most_common if most_common != "J" else c.most_common(2)[1][0]
        )

    c = Counter(card)
    match (len(c), c.most_common(1)[0][1]):
        case (1, _):
            return 6
        case (2, 4):
            return 5
        case (2, _):
            return 4
        case (3, 3):
            return 3
        case (3, _):
            return 2
        case (4, _):
            return 1
        case (_, _):
            return 0


@dataclass
class CHand:
    card: str
    rank: int
    bid: int

    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(5):
                if self.card[i] != other.card[i]:
                    return card_score[self.card[i]] < card_score[other.card[i]]
        return self.rank < other.rank


data = open("input.txt").read().splitlines()

ALL_HANDS_1, ALL_HANDS_2 = [], []
for hand in data:
    hand, bid = scanf("%s %d", hand)
    ALL_HANDS_1.append(CHand(hand, get_card_rank(hand, "1"), bid))
    ALL_HANDS_2.append(CHand(hand, get_card_rank(hand, "2"), bid))


card_score = {c: i for i, c in enumerate("23456789TJQKA")}
part1 = sum([(rank + 1) * hand.bid for rank, hand in enumerate(sorted(ALL_HANDS_1))])
card_score["J"] = -1
part2 = sum([(rank + 1) * hand.bid for rank, hand in enumerate(sorted(ALL_HANDS_2))])
# print(f"Part 1: {part1}")
# print(f"Part 2: {part2}")
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
