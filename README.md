# Qiskit Fall Fest 2026 — Phase 1
## O1: Max-Cut (Backup)

This is a **separate backup project** for **O1 — Max-Cut** under the Quantum Optimization track. It follows the same Phase-1 architecture-aware workflow used in the primary S3 project, including the same illustrative Processor A/B definitions, noise proxies, reproducibility conventions, CI checks, AI disclosure and reporting style.

## Important scope note
The supplied official materials confirm O1 as **Max-Cut** and require an A/B comparison, problem-specific metric, architecture/resource metrics, reproducibility and evidence-based interpretation. They do not provide a complete Max-Cut graph instance in the materials used here. Therefore the graph instance in `data/o1_instance.json` is explicitly **participant-defined and reproducible**, not organizer-certified.

The Processor A/B JSON files intentionally use the **same illustrative processor data and noise parameters as the S3 project** so that the backup changes the optimization problem while preserving the architecture baseline.

## Phase-1 workflow
1. Select exactly one PS: **O1 — Max-Cut**.
2. Define a transparent weighted graph instance.
3. Compute an exact classical Max-Cut reference.
4. Build a p=1 QAOA statevector model.
5. Route the same logical cost interactions onto Processor A and Processor B.
6. Apply the same illustrative noise proxies used in the S3 baseline.
7. Measure noisy expected cut, approximation ratio, optimal-cut probability and uncertainty.
8. Compare depth, two-qubit operations, SWAPs and physical qubits.
9. Explain architecture effects using measured evidence.
10. Stop at Processor A/B; no Phase-2 processor work is included.

## Repository structure
```text
QFF2026_O1_MaxCut_Phase1_Project/
├── README.md
├── main.ipynb
├── requirements.txt
├── requirements-practice.txt
├── data/
│  ├── raw/o1_instance.json
│  ├── processed/
│  ├── o1_instance.json
│  ├── practice_config.json
│  └── guide_settings.json
├── processors/
│  ├── processor_A.json
│  └── processor_B.json
├── src/
│  ├── problem.py
│  ├── processors.py
│  ├── routing.py
│  ├── metrics.py
│  ├── qaoa.py
│  ├── benchmark.py
│  └── visualization.py
├── scripts/
│  ├── build_notebook.py
│  ├── run_benchmark.py
│  ├── make_figures.py
│  └── validate_submission.py
├── results/
│  ├── tables/AB_comparison.csv
│  └── figures/
├── report/report.md
├── docs/
├── tests/
└── .github/workflows/ci.yml
```

## Installation
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
```
For the lightweight deterministic benchmark:
```bash
pip install -r requirements-practice.txt
```

## Run
```bash
python scripts/run_benchmark.py
pytest -q
python scripts/validate_submission.py
```

## Metrics
Problem-specific:
- exact classical optimum
- ideal QAOA expected cut
- noisy expected cut
- approximation ratio
- probability of sampling an optimal cut
- standard error

Architecture/resource:
- logical edges
- two-qubit operations
- SWAP count
- depth proxy
- physical qubits

## Interpretation framework
The analysis answers: What changed? What routing was introduced? How much extra two-qubit work appeared? Did the noisy Max-Cut objective change? Which conclusions are tied to topology, and which depend on the illustrative noise proxy?

## AI disclosure
AI-assisted development was used. The submitting team must verify all code and numerical results and disclose assistance according to the official competition policy.

## Limitations
This backup is not a claim of official O1 benchmark data. The graph instance is participant-defined because no organizer-provided Max-Cut instance was supplied in the materials available for this project. Processor definitions and noise proxies are illustrative comparators inherited from the S3 project baseline.
