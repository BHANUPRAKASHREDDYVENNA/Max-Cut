import itertools,json
from pathlib import Path
def load_instance(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def cut_value(bits,edges):
    b=list(bits); return sum(float(w) for u,v,w in edges if b[int(u)]!=b[int(v)])
def brute_force_optimum(n,edges):
    best=-1.; best_bits=[]
    for bits in itertools.product((0,1),repeat=n):
        value=cut_value(bits,edges)
        if value>best: best,best_bits=value,list(bits)
    return best,best_bits
