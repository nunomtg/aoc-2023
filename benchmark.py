import time
import argparse
import subprocess
from statistics import mean, stdev

parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("--d", type=int, default=1)
parser.add_argument("--I", type=int, default=10)
args = parser.parse_args()


def run_python(day: str):
    start_time = time.perf_counter_ns()

    subprocess.run(["python", "day01.py"], cwd="python/day01")

    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    return execution_time


def run_rust(day: str):
    start_time = time.perf_counter_ns()

    subprocess.run(["rust/day01/target/release/day01.exe"], cwd="rust/day01")

    end_time = time.perf_counter_ns()
    execution_time = end_time - start_time
    return execution_time


DAY = f"day{args.d:02}"
ITERS = args.I

exec_times_python = [run_python(DAY) for i in range(ITERS)]
exec_times_rust = [run_rust(DAY) for i in range(ITERS)]


print(
    f"Python program executed in {mean(exec_times_python)*1e-6:.1f} +- {stdev(exec_times_python)*1e-6:.1f} ms"
)
print(
    f"Rust program executed in {mean(exec_times_rust)*1e-6:.1f} +- {stdev(exec_times_rust)*1e-6:.1f} ms"
)
print(f"Speedup: {mean(exec_times_python)/mean(exec_times_rust):.1f}x")
