from pathlib import Path
import sys,csv,json
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.problem import load_instance,brute_force_optimum
from src.processors import load_processor
from src.qaoa import optimize_p1
from src.benchmark import benchmark
from src.visualization import make_figures
inst=load_instance(ROOT/"data/o1_instance.json"); edges=inst["edges"]; n=inst["num_qubits"]
opt,bits=brute_force_optimum(n,edges); _,gamma,beta=optimize_p1(edges,n)
rows=[]
for name in ("A","B"):
    p=load_processor(ROOT/f"processors/processor_{name}.json")
    r=benchmark(p,edges,n,gamma,beta,opt,4000,2026+ord(name)); r.update({"classical_optimum":opt,"gamma":gamma,"beta":beta,"optimal_cut_bits":"".join(map(str,bits))}); rows.append(r)
out=ROOT/"results/tables"; out.mkdir(parents=True,exist_ok=True)
with (out/"AB_comparison.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
(out/"classical_reference.json").write_text(json.dumps({"optimum":opt,"bits":bits,"gamma":gamma,"beta":beta},indent=2),encoding="utf-8")
make_figures(out/"AB_comparison.csv",ROOT/"results/figures")
print("Completed O1 A/B benchmark")
for r in rows: print(r)
