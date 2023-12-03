########################################################################################################
# Slightly altered version of https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py #
########################################################################################################

import argparse
import subprocess
import tomllib

# Usage: ./get_input.py --y 2023 --d 1
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.
SESSION = tomllib.load(open("session_id.toml", "rb"))["session"]

parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("--y", type=int, default=2023)
parser.add_argument("--d", type=int, default=4)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.y}/day/{args.d}/input --cookie "session={SESSION}"'
output = subprocess.check_output(cmd, shell=True)
output = output.strip()
with open(f"python/day{args.d:02}/input.txt", "wb") as f:
    f.write(output)
