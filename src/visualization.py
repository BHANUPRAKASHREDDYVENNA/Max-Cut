from pathlib import Path
import csv

def make_figures(csv_path,out_dir):
    rows=list(csv.DictReader(open(csv_path,encoding="utf-8")))
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    for name,title,fields in [
        ("AB_performance.svg","Processor A/B Max-Cut objective",["noisy_expected_cut"]),
        ("architecture_tradeoffs.svg","Architecture resource trade-offs",["two_qubit_ops","swaps","depth_proxy"])
    ]:
        width,height=760,420
        maxv=max(float(r[f]) for r in rows for f in fields) or 1
        bars=[]
        x=80
        for r in rows:
            for f in fields:
                v=float(r[f]); h=260*v/maxv
                bars.append(f'<rect x="{x}" y="{330-h:.1f}" width="55" height="{h:.1f}" fill="#4f46e5"/>')
                bars.append(f'<text x="{x+27}" y="355" text-anchor="middle" font-size="12">{r["processor"][-1]} {f}</text>')
                x+=75
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"><text x="30" y="30" font-size="22">{title}</text>{"".join(bars)}</svg>'
        (out/name).write_text(svg,encoding="utf-8")
