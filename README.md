# Salvo: Knowledge Sharing Session 1 (2026)

Welcome to the repository for **Knowledge Sharing Session 1 (2026)** hosted by **Salvo** — the official AI club of SASTRA.

> **Conducted by:** Adhip Kumar & C. G. Rajiv Subramaniam  
> **Topic:** Regression Analysis — Intuition, Mathematics, and Practical Implementation

---

## 📌 Overview

This session introduces foundational regression techniques in machine learning, bridging theoretical formulations with hands-on Python implementations:

1. **Linear Regression:** Modeling continuous outcomes, understanding parameters (slope, intercept), assessing goodness-of-fit ($R^2$), and plotting regression lines.
2. **Logistic Regression:** Transitioning from linear to probabilistic classification, odds and log-odds, the sigmoid activation function, and probability thresholds.
3. **Decision Boundaries:** Classifying 2D non-trivial data distributions and visualizing classification margins and probability surfaces.

---

## 📂 Repository Structure

```text
Salvo_Knowledge_sharaing_session_1_2026/
├── presentations/
│   ├── 01_Regression_Theory_and_Concepts.pptx  # Theory deck (18 slides)
│   └── 02_Regression_in_Code_Walkthrough.pptx  # Code walkthrough deck (9 slides)
├── code/
│   ├── 01_linear_regression.py                 # Linear regression demo & visualization
│   ├── 02_logistic_regression.py               # Logistic regression probability curve demo
│   └── 03_decision_boundary.py                 # 2D decision boundary & region plotting
├── requirements.txt                            # Python package dependencies
├── LICENSE                                     # License
└── README.md                                   # Session documentation & guide
```

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

### 1. Linear Regression
Fits an ordinary least squares regression model on study hours versus test scores:
```bash
python code/01_linear_regression.py
```

### 2. Logistic Regression
Fits a logistic regression model to predict pass/fail probability based on study time:
```bash
python code/02_logistic_regression.py
```

### 3. Decision Boundary Visualization
Visualizes the decision regions and contour lines on synthetic two-class 2D data:
```bash
python code/03_decision_boundary.py
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
