# Phase 1 compliance matrix

| Requirement | Evidence |
|---|---|
| Exactly one PS | O1 — Max-Cut |
| Core solution | src/problem.py, src/qaoa.py, src/benchmark.py |
| Processor A/B | processors/ |
| Problem metrics | expected cut, approximation ratio, optimal probability |
| Resource metrics | SWAPs, two-qubit operations, depth proxy, qubits |
| Results | results/tables and results/figures |
| Reproducibility | fixed graph, shots, seeds, parameters |
| Environment | requirements files |
| Automation | GitHub Actions CI |
| AI disclosure | README/report |
