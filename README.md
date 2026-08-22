# Paper draft — MISO RIS-ISAC-NOMA (Comm. Letters style)

## Files
- `main.tex` — the draft (IEEEtran, `journal` option = Comm. Letters layout).
- `figs/` — the 5 selected figures (+2 optional, copied but commented out in the .tex).

## Compile
Easiest: upload this `draft/` folder to **Overleaf**, set compiler to **pdfLaTeX**, compile `main.tex`.
Locally: `pdflatex main` (no .bib needed — references are inline `thebibliography`).

## Figures used (best, non-redundant)
| Label in paper | File | Source plot |
|---|---|---|
| Fig. 1 training | `fig_training.jpg` | MAML loss vs iterations |
| Fig. 2 ablation CDF | `fig_cdf.jpg` | sum-rate CDF |
| Fig. 3 QoS bars | `fig_qos.jpg` | QoS violation 29.4%→0.1% |
| Fig. 4 R vs N | `fig_rate_N.jpg` | sum-rate vs RIS size |
| Fig. 5 R & QoS vs P | `fig_rate_P.jpg` | 4-scheme headline |
| (optional) | `fig_improvement.jpg` | per-metric improvement — commented out |
| (optional) | `fig_perleg.jpg` | per-leg R_n/R_f/R_s CDFs — commented out |

**Dropped** (low value / redundant): power-allocation histograms, weighted-sum-rate
histogram, RIS-phase heatmap, rate-vs-QoS-margin scatter, Fig-8-in-Mbps.

## TODO before submission (search `PLACEHOLDER` in main.tex)
1. Author block, affiliations, grant/funding line, venue/volume in `\markboth`.
2. Fill the **2026 CommLet** citation `[2]` from the PDF (authors, vol/no/pages).
3. Confirm exact numeric values in the Results text match your final plots
   (medians, %s, thresholds) — I pulled them from the plot annotations.
4. Replace the JPEGs with vector PDF/EPS exports if you have them (sharper print).
5. Optional: add a system-model schematic as Fig. 1 (you said more plots are coming).

## Notes on accuracy
- System model (cascade channel, cluster-MRT NOMA, null-space sensing beam, SIC,
  OMA-TDMA baseline, 0.7/0.3 objective, per-link QoS) matches the generator/trainer.
- The MAML description matches the working pipeline: network predicts the power
  split, RIS phase optimized per channel by an unrolled inner loop, second-order
  meta-gradients. Tweak wording if you change the method.
