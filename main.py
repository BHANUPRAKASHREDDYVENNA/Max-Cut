from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parent
if __name__=="__main__":
    runpy.run_path(str(ROOT/"scripts/run_benchmark.py"),run_name="__main__")
