import argparse
import subprocess
from statistics import mean, stdev
from scanf import scanf

parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("--d", type=int, default=1)
parser.add_argument("--I", type=int, default=50)
parser.add_argument("--B", type=int, default=1)
args = parser.parse_args()


def run_python(day: str):
    out = subprocess.run(
        ["python", f"{day}.py"], cwd=f"python/{day}", capture_output=True
    )
    time = scanf("Python program executed in %f ms", out.stdout.decode("utf-8"))[0]
    return time


def run_rust(day: str):
    out = subprocess.run(
        [f"rust/{day}/target/release/{day}.exe"],
        cwd=f"rust/{day}",
        capture_output=True,
    )
    time = scanf("Rust program executed in %f ms", out.stdout.decode("utf-8"))[0]
    return time


DAY = f"day{args.d:02}"
ITERS = args.I

exec_times_python = [run_python(DAY) for i in range(ITERS)]
if args.B:
    exec_times_rust = [run_rust(DAY) for i in range(ITERS)]


print(
    f"Python program executed in {mean(exec_times_python):.1f} ± {stdev(exec_times_python):.1f} ms"
)
if args.B:
    print(
        f"Rust program executed in {mean(exec_times_rust):.1f} ± {stdev(exec_times_rust):.1f} ms"
    )
    print(f"Speedup: {mean(exec_times_python)/mean(exec_times_rust):.1f}x")
