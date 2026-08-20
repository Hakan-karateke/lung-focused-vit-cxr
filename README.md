# Discrimination Metrics Are Blind to Anatomical Grounding

Code, experiment outputs and manuscript source for a controlled ablation of lung
masking in chest radiograph pneumonia classification.

> **Karateke, H. and Karaduman, G.** *Discrimination Metrics Are Blind to Anatomical
> Grounding: A Controlled Ablation of Lung Masking in Chest Radiograph Pneumonia
> Classification.* Submitted to *IEEE Journal of Biomedical and Health Informatics*.

Fırat University, Elazığ, Türkiye · [Manuscript PDF](paper/main.pdf)

---

## What this study found

The starting question was practical: **does anatomical lung segmentation improve
pneumonia classification?** A three-arm ablation was built to answer it, holding the
split, the seed, the hyperparameters and the crop geometry constant so that masking
was the only variable:

| Arm | Input | Isolates |
|-----|-------|----------|
| **A — raw** | full radiograph, resized | baseline |
| **B — roi** | cropped to the lung bounding box, unmasked | the effect of *cropping* |
| **C — lung** | same crop box, lungs masked | the effect of *masking* |

B and C share an identical crop box, so the A to B step measures cropping and the
B to C step measures masking alone.

**The answer is no — and that is the interesting part.**

- **Discrimination is unchanged.** Internal-test AUC is 0.9981 / 0.9976 / 0.9982 for
  arms A / B / C. Across three training seeds every pairwise comparison is null
  (all DeLong *p* > 0.20; seed-ensemble C − A = +0.0006, *p* = 0.94). A single-seed
  run had suggested a +0.010 AUC gain; the multi-seed analysis showed that this sits
  inside the seed noise floor. It would have been a false positive.
- **Anatomical grounding is transformed.** On independent data the Lung-Focus Ratio
  is 0.011 (RSNA) and 0.017 (NIH) for the raw arm versus 0.952 and 0.951 for the
  masked arm — against a chance level of 0.236, the mean fractional lung area. The
  raw model attends to the lungs **22 times below chance**.
- **The evidence is causal, not just correlational.** Erasing both lungs costs the
  raw model 0.9% AUC (0.9981 to 0.9896). Erasing everything *outside* the lungs costs
  it 22 points (0.9981 to 0.7799). Area-matched random occlusion controls confirm the
  asymmetry is not an artefact of how much pixel area was removed.
- **Dataset leakage does not explain it.** The benchmark carries 86.6%
  class-asymmetric augmentation leakage; a source- and patient-disjoint clean test
  moves AUC by less than 0.01. The near-perfect score is not a leakage artefact — the
  extra-thoracic signal is genuinely there.

The conclusion: **AUC, accuracy and F1 cannot distinguish a model that reads the
lungs from one that reads the collimation border.** Anatomical grounding has to be
measured separately, and masking buys it at no cost to discrimination.

---

## Repository layout

```
paper/                     IEEE JBHI manuscript (LaTeX)
  main.tex                 manuscript source — compiles to exactly 8 pages
  main.pdf                 compiled manuscript
  make_paper_figures.py    regenerates every chart figure as vector PDF
  figures/                 karat1..karat5 — figures in document order
  supplementary/           panels not used in the 8-page manuscript
  AUTHORS.md               author metadata, ORCIDs, funding and COI statements
  ieeecolor.cls            IEEE template files (from IEEE Author Center)

kaggle/                    experiment notebooks, each with its saved output/
  ViT_Pneumonia_Detection-V1/              initial ViT + RRR attention penalty
  Vision transformer ... lung focused-V2/  masking pipeline
  Lung Focused VIT External Validation-V2/ RSNA and NIH external validation
  Ablation-Segmentation-V3/                three-arm controlled ablation  (core)
  Power-RSNA-V4/                           larger RSNA sample, inference only
  MultiSeed-V5/                            seed noise floor vs. effect size
  External-LFR-V6/                         LFR on independent data
  Dataset-Audit-V7/                        duplication and leakage audit
  Clean-Internal-V8/                       source- and patient-disjoint test
  Occlusion-V9/                            causal occlusion, matched controls
  Paper-Figures-V10/                       high-DPI image panels for the paper

figures/                   Turkish method flow diagrams (SVG + PNG)
  make_figures.py          regenerates them from template.html

seminer raporu.docx.md     Turkish MSc seminar report (long form)
```

Every `kaggle/*/output/` directory holds the **actual run artefacts** — logs, metrics
CSVs, statistical test results and prediction arrays — not placeholders. All numbers
in the manuscript trace back to these files.

---

## Reproducing the results

The notebooks run on Kaggle (P100/T4, 16 GB). They are ordered; later notebooks
consume earlier outputs as Kaggle datasets rather than retraining.

| # | Notebook | Needs GPU | Consumes |
|---|----------|-----------|----------|
| 1 | `Ablation-Segmentation-V3` | yes (~3 h) | the datasets below |
| 2 | `Power-RSNA-V4` | yes (inference) | V3 checkpoints |
| 3 | `MultiSeed-V5` | yes (~6 h) | V3 outputs |
| 4 | `External-LFR-V6` | yes (inference) | V3 checkpoints |
| 5 | `Dataset-Audit-V7` | no (CPU) | Kermany dataset |
| 6 | `Clean-Internal-V8` | yes (inference) | V3 checkpoints + V7 audit |
| 7 | `Occlusion-V9` | yes (inference) | V3 checkpoints |
| 8 | `Paper-Figures-V10` | yes (inference) | V3 checkpoints |

Notebook 1 is the only one that trains from scratch. Splits are pinned by
`SPLIT_SEED = 42` and every downstream notebook asserts the split fingerprints
(`train ccf23597ec992137`, `val 779ac7f6455a7ac8`, `test 3a25cbb40ab471d7`) before
running, so a silent split drift fails loudly instead of quietly changing results.

### Datasets

| Role | Source |
|------|--------|
| Internal | Chest X-Ray Pneumonia (Kermany et al.), balanced variant |
| External | RSNA Pneumonia Detection Challenge (adult) |
| External | NIH ChestX-ray14 |
| Segmentation | `ianpan/chest-x-ray-basic` — U-Net trained on CheXmask |

### Model weights

Checkpoints are **not tracked here.** The four files total ~1.3 GB, which exceeds
GitHub's per-file limit and would consume the entire free Git LFS quota. They are
available as outputs of the corresponding Kaggle notebooks, and notebook 1
regenerates them deterministically from the pinned seed.

---

## Building the manuscript

```bash
cd paper
python make_paper_figures.py      # regenerates karat2..karat5 from saved arrays
pdflatex main.tex && pdflatex main.tex
```

`make_paper_figures.py` reads only the saved `.npz` and `.csv` outputs — it never
retrains or re-runs inference, so the figures are reproducible offline in seconds.
Figure 1 (`karat1`) is the image-panel figure produced by notebook 10.

Figures follow IEEE requirements: vector PDF, Type 42 embedded fonts, and the
single-column (3.50 in) and double-column (7.16 in) widths. File names follow the
IEEE convention of the first five letters of the first author's surname plus the
figure number.

---

## Git LFS

Binary artefacts (`*.png`, `*.jpg`, `*.pdf`, `*.npz`, `*.docx`, `*.eps`) are stored in Git LFS.
Figures are regenerated on every manuscript revision, and without LFS each
regeneration would append a fresh multi-megabyte blob to history permanently.

```bash
git lfs install
git clone https://github.com/Hakan-karateke/lung-focused-vit-cxr.git
```

If you clone without `git lfs install`, binary files arrive as small text pointers.
`git lfs pull` fixes this after the fact.

---

## Not tracked

Deliberately excluded via `.gitignore`, with reasons:

- **Model checkpoints** (~1.3 GB) — see *Model weights* above.
- **`audit_near_duplicates.csv`** (84 MB) — 676k dHash pairs at 8x8 resolution. The
  threshold is far too permissive for a domain as homogeneous as chest radiography;
  157k of those pairs cross class boundaries, which is itself evidence of false
  positives. The leakage analysis reported in the paper uses exact source-filename
  matching, which is in `audit_files.csv`.
- **Preprocessing caches**, LaTeX build artefacts, third-party template archives.

---

## Citation

A BibTeX entry will be added once the manuscript reaches a citable state. Until
then please contact the corresponding author.

## Contact

**Hakan Karateke** (corresponding) — [ORCID 0009-0004-9174-4271](https://orcid.org/0009-0004-9174-4271)

**Gülşah Karaduman** — [ORCID 0000-0001-8034-3019](https://orcid.org/0000-0001-8034-3019)

## Licensing

No license has been chosen yet. Until one is added, default copyright applies and
the material is provided for review purposes only. The IEEE template files under
`paper/` are redistributed from the IEEE Author Center under IEEE's own terms.
