"""
Salvo - Knowledge Sharing Session 1 (2026)
Topic: Logistic Regression Demonstration
Description: Fits a logistic regression model (study hours vs. exam pass/fail)
             and visualizes the predicted probability sigmoid curve.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Data: hours studied -> passed (1) or failed (0)
hours = np.arange(1, 11).reshape(-1, 1)
passed = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1])

# 2. Fit the model
model = LogisticRegression().fit(hours, passed)

# 3. Predict
p = model.predict_proba([[5]])[0, 1]
print("P(pass) at 5 hours:", round(p, 2))
print("Class for 2 hours:", model.predict([[2]])[0])

# 4. Plot the probability curve
x = np.linspace(0, 11, 100).reshape(-1, 1)
prob = model.predict_proba(x)[:, 1]
plt.scatter(hours, passed, color="red", label="Data")
plt.plot(x, prob, label="P(pass)")
plt.axhline(0.5, linestyle="--", color="gray")
plt.xlabel("Hours"); plt.ylabel("P(pass)")
plt.legend(); plt.show()
