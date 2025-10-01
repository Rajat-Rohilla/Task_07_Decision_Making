# Task_07_Decision_Making

README (Repository Overview)

Project: Syracuse Football Ethical Decision Report — September 30, 2025

Objective: Provide reproducible, ethical, and actionable recommendations for Syracuse University Football leadership based on cumulative team statistics. Focus is on process 

transparency, fairness, and risk-tiered decision-making.

Contents:

data/ — raw input files (e.g., cume.pdf)

src/ — analysis scripts (e.g., reproducible_analysis.py)

notebooks/ — Jupyter notebooks for exploratory analysis and visualization

docs/ — final reports (ethical_decision_report.md)

How to reproduce:

Clone repository: git clone <repo-url>

Install Python 3.10+ with numpy, scipy, pandas

Run python src/reproducible_analysis.py

Outputs will replicate bootstrap estimates, sensitivity analysis, and summary stats

Next steps for contributors:

Add play-by-play CSV exports once obtained

Extend code to compute per-play EPA and adjusted efficiency

Ensure all future analyses log seeds and document edits to LLM outputs

Ethics and compliance:

No player-level private/medical data included in current repo

Any extension to biometric/tracking data requires explicit consent and IRB/ethics approval

Personnel recommendations require human/legal review

AI Prompt (Audit Log for LLM)

Exact prompt used to generate this report:

"Take the attached cumulative team statistics PDF (cume.pdf) for Syracuse University Football as of Sep 30, 2025 and produce a stakeholder-facing decision report focusing on ethics, 
reliability, and process documentation. Include: stakeholder context, data provenance, recreated descriptive stats and visuals, code and seeds, uncertainty quantification (CIs/bootstrap), bias/fairness checks, robustness/sensitivity, and a 3-tier recommendation structure (operational, investigatory, high-stakes). Save every prompt and raw output, and annotate edits."

Model response handling:

Initial raw output was refined for clarity

Clarified ambiguous stat labels (sacks, turnovers)

Inserted bootstrap confidence intervals and sensitivity tests

Added ethical/privacy/legal section for robustness

Closing notes

This repository ensures transparency, reproducibility, and ethical accountability in sports analytics decision-making. Immediate operational actions can begin this week, while investigatory steps require new data collection. High-stakes decisions must follow human and legal review channels. review

