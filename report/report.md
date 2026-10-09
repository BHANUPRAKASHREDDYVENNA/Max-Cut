# O1 Max-Cut — Phase 1 Report

The selected problem statement is O1 — Max-Cut. Phase 1 stops at Processor A and Processor B.

The public materials used for this repository do not include an organizer-specific O1 graph instance, so the included five-node graph and processor/noise settings are explicitly participant-defined and illustrative.

The measured illustrative result is 4.4945 noisy expected cut on Processor A and 4.39075 on Processor B. Architecture metrics are 0 versus 5 SWAPs, 7 versus 22 two-qubit operations, and depth proxies 14 versus 34.

Interpretation: Processor B's line topology requires multi-hop routing for several logical interactions. The extra routing increases two-qubit work and therefore the illustrative stochastic noise burden. This is a topology demonstration, not calibrated hardware behavior.

Reproduce with python scripts/run_benchmark.py and inspect results/tables/AB_comparison.csv. AI assistance was used for drafting/code structuring; the project owner is responsible for verification and disclosure.
