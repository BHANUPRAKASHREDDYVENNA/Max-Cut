from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=["README.md","main.py","requirements.txt","processors/processor_A.json","processors/processor_B.json","data/o1_instance.json","results/tables/AB_comparison.csv","report/report.md",".github/workflows/ci.yml"]
missing=[x for x in required if not (ROOT/x).exists()]
if missing: raise SystemExit("Missing required files:\n- "+"\n- ".join(missing))
print("Submission structure OK")
