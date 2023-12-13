import time

start_time = time.perf_counter_ns()

######################################
from dataclasses import dataclass


@dataclass
class Tile:
    tile: list[str]
    tile_T: list[str]
    R: int
    C: int
    r1: int = 0
    c1: int = 0
    r2: int = 0
    c2: int = 0
    _part1: int = 0
    _part2: int = 0

    def __init__(self, tile):
        self.tile = tile
        self.R = len(tile)
        self.tile_T = ["".join(row) for row in zip(*tile)]
        self.C = len(self.tile_T)
        self.get_reflection()
        self.get_smudged_reflection()
        Tile._part1 += self.c1 + 100 * self.r1
        Tile._part2 += self.c2 + 100 * self.r2

    @staticmethod
    def check_reflection(tile, row):
        good = all(a == b for a, b in zip(tile[row - 1 :: -1], tile[row:]))
        return row if good else 0

    @staticmethod
    def line_diff(line1, line2):
        diff = sum(a != b for a, b in zip(line1, line2))
        return diff

    @staticmethod
    def check_smudged_reflection(tile, row, row1):
        if row == row1:
            return 0
        good = sum(
            Tile.line_diff(a, b) for a, b in zip(tile[row - 1 :: -1], tile[row:])
        )
        return row if good == 1 else 0

    def get_reflection(self):
        self.r1 = sum(Tile.check_reflection(self.tile, row) for row in range(self.R))
        self.c1 = sum(Tile.check_reflection(self.tile_T, row) for row in range(self.C))

    def get_smudged_reflection(self):
        self.r2 = sum(
            Tile.check_smudged_reflection(self.tile, row, self.r1)
            for row in range(self.R)
        )
        self.c2 = sum(
            Tile.check_smudged_reflection(self.tile_T, row, self.c1)
            for row in range(self.C)
        )


_ = tuple(
    Tile(line.strip().split("\n")) for line in open("input.txt").read().split("\n\n")
)

# print("Part 1:", Tile._part1)
# print("Part 2:", Tile._part2)
######################################

end_time = time.perf_counter_ns()
execution_time = end_time - start_time

print(f"Python program executed in {execution_time*1e-6:.3f} ms")
