# Qiskit Fall Fest 2026 — Phase 1
## O1 — Max-Cut

Track: Quantum Optimization. Selected problem statement: O1 — Max-Cut. Phase 1 scope: Processor A vs Processor B only.

### Scope and evidence
The official Phase 1 materials establish O1 as Max-Cut and require one selected PS, a core solution, Processor A/B runs, problem/resource metrics, A/B comparison, reproducibility, graphs/tables, README/report, and environment specification. The public materials used here do not contain an O1-specific Challenge Kit graph instance, so the graph and processor/noise values in this repository are explicitly illustrative / participant-defined rather than official Challenge Kit values.

Replace the illustrative inputs under data/ and processors/ with the organizer-supplied O1 kit before final submission.

### Method
A p=1 QAOA-style statevector is used for a fixed five-node weighted Max-Cut graph. A brute-force search gives the exact classical optimum. The same logical edges are routed against two processor topologies. We record expected cut, approximation ratio, optimal-cut probability, standard error, SWAPs, two-qubit operations, depth proxy, and physical qubits.

### Illustrative A/B result
| Metric | Processor A | Processor B |
|---|---:|---:|
| Classical optimum | 6.00 | 6.00 |
| Noisy expected cut | 4.4945 | 4.3908 |
| Approximation ratio | 0.7491 | 0.7318 |
| Optimal-cut probability | 0.2225 | 0.2133 |
| SWAPs | 0 | 5 |
| Two-qubit operations | 7 | 22 |
| Depth proxy | 14 | 34 |

Processor B's line topology requires multi-hop routing for several logical edges, increasing the two-qubit workload and the illustrative noise proxy. These are demonstrator results, not calibrated hardware measurements.

### Run
    python -m pip install -r requirements-practice.txt
    python scripts/run_benchmark.py
    pytest -q
    python scripts/validate_submission.py

The full requirements.txt includes Qiskit and Qiskit Aer for circuit-level experimentation.

### Repository
README.md
main.py
requirements.txt
requirements-practice.txt
data/
processors/
src/
scripts/
results/
report/
docs/
tests/
.github/workflows/ci.yml

### Phase 1 boundary
Processor C and custom Processor D are excluded because they are Phase 2.

### AI disclosure
AI assistance was used for drafting and code structuring. The project owner remains responsible for verification, understanding, reproducibility, and compliance with the organizer's AI-use policy.
