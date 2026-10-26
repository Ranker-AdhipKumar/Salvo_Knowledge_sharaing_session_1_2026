# Salvo: Knowledge Sharing Session 1 (2026)

Welcome to the repository for **Knowledge Sharing Session 1 (2026)** hosted by **Salvo** — the official AI club of SASTRA.

> **Conducted by:** Adhip Kumar & C. G. Rajiv Subramaniam  
> **Topic:** Regression Analysis — Intuition, Mathematics, and Practical Implementation

---

## 📌 Overview

This session introduces foundational regression techniques in machine learning, bridging theoretical formulations with hands-on Python implementations:

1. **Linear Regression:** Modeling continuous outcomes, understanding parameters (slope, intercept), assessing goodness-of-fit ($R^2$), and plotting regression lines.
2. **Evaluation & Residual Analysis:** Computing Sum of Squared Errors (SSE), MAE, MSE, and RMSE.
3. **Multiple Linear Regression:** Multivariate relationships with multiple continuous predictors.
4. **Data Preprocessing:** Categorical one-hot encoding (`pd.get_dummies`) and feature standardization (`StandardScaler`).
5. **Model Validation:** Out-of-sample testing via `train_test_split` and publication-quality visual plots.
6. **Logistic Regression & Decision Boundaries:** Probabilistic classification, sigmoid curves, odds ratios, and 2D classification decision regions.

---

## 📂 Repository Structure

```text
Salvo_Knowledge_sharaing_session_1_2026/
├── presentations/
│   ├── 01_Regression_Theory_and_Concepts.pptx  # Conceptual theory deck (18 slides)
│   └── 02_Regression_in_Code_Walkthrough.pptx  # Code walkthrough deck (9 slides)
├── notebooks/
│   └── 01_regression_analysis_handson.ipynb    # Interactive Jupyter / Colab session notebook
├── code/
│   ├── 01_linear_regression.py                 # Linear regression demo & visualization
│   ├── 02_logistic_regression.py               # Logistic regression probability curve demo
│   └── 03_decision_boundary.py                 # 2D decision boundary & region plotting
├── requirements.txt                            # Python dependencies (numpy, pandas, scikit-learn, matplotlib)
├── .gitignore                                  # Standard git ignore rules
├── LICENSE                                     # License
└── README.md                                   # Session documentation & guide
```

---

## 📓 Interactive Google Colab Notebook

You can open and execute the complete session notebook directly in your browser with zero local setup:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ranker-AdhipKumar/Salvo_Knowledge_sharaing_session_1_2026/blob/main/notebooks/01_regression_analysis_handson.ipynb)

The notebook includes step-by-step markdown explanations, formulas, code, and pre-rendered outputs for:
- Environment Setup & Library Installation
- Data Loading & Exploration
- Model Training (OLS Slope & Intercept)
- Inference on New Student Data
- SSE Calculation & Residual Verification
- Model Evaluation ($R^2$, MAE, MSE, RMSE)
- Multiple Linear Regression Modeling
- Categorical Feature Encoding (One-Hot Encoding)
- Feature Scaling (`StandardScaler`)
- Train-Test Split Validation & High-Resolution Matplotlib Plotting

---

## ⚙️ Getting Started

### 1. Prerequisites
- Python 3.8 or higher installed on your system.

### 2. Environment Setup
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Ranker-AdhipKumar/Salvo_Knowledge_sharaing_session_1_2026.git
cd Salvo_Knowledge_sharaing_session_1_2026
pip install -r requirements.txt
```

---

## 🚀 Running the Code Examples

### Standalone Python Scripts
Run any demo script directly from the terminal:

```bash
# 1. Simple Linear Regression
python code/01_linear_regression.py

# 2. Logistic Regression (Sigmoid probability curve)
python code/02_logistic_regression.py

# 3. Logistic Regression Decision Boundary (2D contours)
python code/03_decision_boundary.py
```

### Jupyter Notebook
Launch Jupyter Lab or Notebook locally:

```bash
jupyter notebook notebooks/01_regression_analysis_handson.ipynb
```

---

## 📚 Session Slides
The presentation slide decks are provided in the [`presentations/`](presentations/) directory:
- [**01_Regression_Theory_and_Concepts.pptx**](presentations/01_Regression_Theory_and_Concepts.pptx): Conceptual foundations, derivations, and loss functions.
- [**02_Regression_in_Code_Walkthrough.pptx**](presentations/02_Regression_in_Code_Walkthrough.pptx): Step-by-step code explanation and visual output interpretation.

---

## 👥 Contributors
- **Adhip Kumar**
- **C. G. Rajiv Subramaniam**
- **Salvo — The Official AI Club of SASTRA**
