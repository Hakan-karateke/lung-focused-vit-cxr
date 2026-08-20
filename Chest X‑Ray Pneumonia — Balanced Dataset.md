About Dataset
Title
Pediatric Chest X‑Ray Pneumonia — Balanced Dataset

Subtitle
8,530 frontal chest X‑rays (NORMAL vs PNEUMONIA) — preprocessed, balanced, ready for classification experiments

Data Card Summary
Attribute	Value	Notes
Total images	8,530	NORMAL: 4,265; PNEUMONIA: 4,265
Classes	2	NORMAL; PNEUMONIA
Original source	Guangzhou Women and Children’s Medical Center	Pediatric AP chest X‑rays, ages 1–5
File types	JPEG	8‑bit RGB after conversion
License	CC BY 4.0	Cite original Cell paper and Mendeley dataset
About the Dataset
Short description
Chest X‑ray images (anterior‑posterior) of pediatric patients used to detect pneumonia. Images were quality‑checked and labeled by expert physicians; evaluation set reviewed by a third expert. This release is a balanced version created by controlled undersampling and augmentation to produce equal class counts.

Original citation
Kermany, D., et al., Cell 2018. Figure S6 and dataset referenced in the Cell paper. Data mirror: Mendeley.
link

Origin Acknowledgement
Data collected at: Guangzhou Women and Children’s Medical Center, Guangzhou.
link

Folder Structure to Publish
balanced_dataset/
├─ train/
│  ├─ NORMAL/ (3400 images)
│  └─ PNEUMONIA/ (3400 images)
├─ val/
│  ├─ NORMAL/ (850 images)
│  └─ PNEUMONIA/ (850 images)
├─ test/
│  ├─ NORMAL/ (15 images)
│  └─ PNEUMONIA/ (15 images)
├─ README.md
└─ LICENSE.txt
Contents
train/ — images for training (per-class counts)
val/ — validation images (per-class counts)
test/ — test images (per-class counts)
LICENSE.txt — CC BY 4.0
README.md — this file
Origin and citation
Data originally collected at Guangzhou Women and Children’s Medical Center and published in Kermany et al., Cell 2018. Mirror: Mendeley dataset. Please cite the Cell paper and the Mendeley DOI when using this dataset.

Usage notes
Preprocessing: resize to model input (e.g., 224×224), normalize using ImageNet or dataset mean/std.
Data leakage caution: do not mix augmented variants of the same original across splits.
Clinical caution: dataset for research only; not a substitute for clinical diagnosis.
Baseline suggestions
Models: ResNet50, DenseNet121, EfficientNet-B0.
Metrics: accuracy, precision, recall, F1, AUC-ROC.
Explainability: Grad‑CAM recommended for model inspection.
Ethical Considerations and Limitations
Clinical caution: Not for diagnostic use.
Bias: Single‑center pediatric cohort; limited generalizability.
Privacy: Images are de‑identified in the original dataset; follow institutional review and local regulations.
Reproducibility Checklist
Publish original raw counts and the random seed used.
Include exact augmentation code and library versions.
Provide CSV split files (filename, label).
State hardware and software environment (Python, PyTorch/Torchvision versions).


https://data.mendeley.com/datasets/rscbjbr9sj/2

Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images for Classification
Published: 6 January 2018
|
Version 2
|
DOI:
10.17632/rscbjbr9sj.2
Contributors:
Daniel Kermany
,
Kang Zhang
,
Michael Goldbaum
Description
Dataset of validated OCT and Chest X-Ray images  described and analyzed in "Deep learning-based classification and referral of treatable human diseases". The OCT Images are split into a training set and a testing set of independent patients. OCT Images are labeled as (disease)-(randomized patient ID)-(image number by this patient) and split into 4 directories: CNV, DME, DRUSEN, and NORMAL.

Download All 6.55 GB

Files

zip
ChestXRay2017.zip
1.15 GB

zip
code2017.zip
19.3 KB

gz
OCT2017.tar.gz
5.4 GB
Steps to reproduce
Instructions found in README 

Institutions
University of California San Diego
Categories
Applied Sciences
Licence

CC BY 4.0

![mendeley section](image.png)