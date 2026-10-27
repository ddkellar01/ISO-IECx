"""Local test runner script executing compliance audits and test suites."""
import subprocess
import sys

def run_evaluations():
    print("Running pytest evaluation suites...")
    result = subprocess.run(["pytest", "-v", "tests/"])
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_evaluations()
