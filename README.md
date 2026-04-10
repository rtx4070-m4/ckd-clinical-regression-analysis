
---
title: "Multivariate Regression Framework for Estimating GFR in CKD Patients"
author: "Chaudhary Tanuj"
date: "`r Sys.Date()`"
output:
  github_document:
    toc: true
    toc_depth: 3
---

# 🧬 CKD GFR Prediction using Multivariate Regression

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Regression-green)
![Healthcare](https://img.shields.io/badge/Domain-Healthcare-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

Chronic Kidney Disease (CKD) is a progressive medical condition affecting millions of patients worldwide. Monitoring kidney function is critical to prevent progression to kidney failure.

The **Glomerular Filtration Rate (GFR)** is the gold standard measure of kidney filtration capacity. However, direct measurement of GFR is expensive and time‑consuming. This project builds a **statistical and machine learning framework** to estimate GFR using routinely available clinical biomarkers.

This repository demonstrates a **complete biomedical data science pipeline**, including:

- Data preprocessing
- Robust outlier detection
- Feature selection
- Regression modeling
- Model diagnostics
- Visualization and interpretation

---

# 🔬 Analytical Pipeline

```text
Raw CKD Dataset
      │
      ▼
Data Cleaning
(Remove IDs, Missing values)
      │
      ▼
MAD Outlier Removal
(Median ± 3 × MAD)
      │
      ▼
Feature Selection
(LASSO, PCA, Forward Selection)
      │
      ▼
Model Development
(Linear, LASSO, Ridge, PCR)
      │
      ▼
Model Evaluation
(SSE, R², AIC)
      │
      ▼
Residual Analysis
(Model diagnostics)
      │
      ▼
Visualization & Dashboard
```

---

# 📊 Dataset

The dataset contains **1659 patient observations** and the following predictors:

| Variable | Description |
|--------|-------------|
| Age | Patient age in years |
| SerumCreatinine | Kidney filtration biomarker |
| BUNLevels | Blood urea nitrogen |
| HemoglobinLevels | Oxygen transport capacity |
| SystolicBP | Blood pressure |
| ProteinInUrine | Kidney damage indicator |
| GFR | Target variable |

---

# 🏥 Clinical Interpretation

## Serum Creatinine

Creatinine is a metabolic waste product filtered by kidneys.

Typical range:

```
0.5 – 5.0 mg/dL
```

Higher creatinine levels indicate **reduced kidney filtration**.

---

## Blood Urea Nitrogen

BUN measures nitrogen waste in the bloodstream.

```
7 – 60 mg/dL
```

Elevated BUN indicates impaired kidney function.

---

## Hemoglobin

Hemoglobin measures oxygen transport.

CKD frequently causes anemia due to reduced erythropoietin.

Typical range:

```
9 – 17 g/dL
```

---

# ⚙️ Data Preprocessing

## Missing Value Handling

| Variable Type | Method |
|---------------|-------|
| Numerical | Median Imputation |
| Categorical | Mode Imputation |

Median is preferred because clinical biomarkers often contain **extreme values**.

---

## Data Normalization

Clinical biomarkers have different measurement scales.

Normalization was performed using **StandardScaler**.

---

# 🚨 Outlier Detection

## Median Absolute Deviation (MAD)

MAD is a robust statistical measure used to detect extreme observations.

```
MAD = median(|Xi − median(X)|)
```

Outliers were detected using:

```
Median ± 3 × MAD
```

MAD is preferred for biomedical data because:

- robust to extreme values
- does not assume normal distribution
- effective for skewed clinical variables

---

# 🔍 Feature Selection

Three complementary methods were used.

## LASSO Regression

LASSO introduces an L1 penalty:

```
min (Σ(yi − Xiβ)² + λ Σ|βj|)
```

Advantages:

- automatic variable selection
- prevents overfitting
- improves model interpretability

---

## Principal Component Analysis (PCA)

PCA reduces dimensionality by transforming correlated predictors into orthogonal components.

```
PC1 = a1X1 + a2X2 + ... + apXp
```

This helps remove **multicollinearity between biomarkers**.

---

## Forward Stepwise Selection

Predictors are added incrementally based on statistical significance and AIC improvement.

Example:

```
GFR ~ Creatinine
GFR ~ Creatinine + BUN
GFR ~ Creatinine + BUN + Hemoglobin
```

---

# 🤖 Model Development

Four regression models were implemented:

| Model | Description |
|------|-------------|
| Linear Regression | Ordinary least squares |
| LASSO Regression | L1 regularization |
| Ridge Regression | L2 regularization |
| PCR | PCA + regression |

---

# 📈 Model Evaluation

Three metrics were used.

## SSE

```
SSE = Σ (yi − ŷi)²
```

Measures prediction error.

Lower values indicate better performance.

---

## R²

```
R² = 1 − SSE / SST
```

Measures variance explained by the model.

Typical interpretation:

| R² | Meaning |
|---|---|
| 0.2–0.4 | weak |
| 0.4–0.6 | moderate |
| 0.6–0.8 | strong |
| >0.8 | very strong |

---

## AIC

```
AIC = 2k − 2 ln(L)
```

Balances model accuracy and complexity.

Lower values indicate better models.

---

# 🧪 Residual Diagnostics

Residuals:

```
ei = yi − ŷi
```

Diagnostics performed:

- Residual vs predicted plots
- Normality checks
- Durbin–Watson test
- Cook’s distance

A valid regression model should show:

```
random residual distribution
constant variance
independent errors
approximately normal residuals
```

---

# 📊 Visualization

Key visualizations include:

- Feature importance plots
- Residual diagnostic plots
- PCA variance plots
- Model comparison charts

These visualizations help clinicians interpret the results more easily.

---

# 🔑 Key Findings

Important predictors of kidney function include:

```
SerumCreatinine
BUNLevels
ProteinInUrine
HemoglobinLevels
```

These biomarkers directly reflect **kidney filtration efficiency**.

---

# 📁 Repository Structure

```
CKD_GFR_Project
│
├── data
│   └── ckd_dataset.csv
│
├── notebooks
│   └── analysis.ipynb
│
├── src
│   ├── data_cleaning.py
│   ├── mad_outlier.py
│   ├── feature_selection.py
│   ├── models.py
│   ├── evaluation.py
│   └── residual_analysis.py
│
├── results
│   ├── plots
│   └── tables
│
└── main.py
```

---

# 🛠 Technologies Used

| Category | Tools |
|-------|------|
| Language | Python |
| Libraries | pandas, numpy |
| ML | scikit‑learn |
| Statistics | statsmodels |
| Visualization | matplotlib, seaborn, plotly |
| Environment | Jupyter Notebook |

---

# 🚀 Future Work

Potential improvements include:

- Deep learning models for CKD progression
- Integration with hospital clinical systems
- Real‑time predictive dashboards
- Survival analysis for CKD outcomes

---

# 👨‍💻 Author

**Chaudhary Tanuj**  
Biomedical Data Science Project

---

# 📜 License

MIT License
