# Task_07_Decision_Making

Project: Syracuse Football Ethical Decision Report — September 30, 2025
Objective: Provide reproducible, ethical, and actionable recommendations for Syracuse University Football leadership based on cumulative team statistics. Focus is on process transparency, fairness, and risk-tiered decision-making.

#Contents:
data/ — raw input files (e.g., cume.pdf)
docs/ — final reports (ethical_decision_report.md)
Prompt/ - Prompt used to produce results
README.md — this file


#How to reproduce:
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
Contact: After pushing updates, email repository link to jrstrome@syr.edu.
