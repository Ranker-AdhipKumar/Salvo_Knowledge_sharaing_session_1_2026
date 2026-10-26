"""
Salvo - Knowledge Sharing Session 1 (2026)
Topic: Linear Regression Demonstration
Description: Fits a simple linear regression model (study hours vs. exam score)
             and visualizes the fitted regression line against observed data.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Data: hours studied -> exam score
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
score = np.array([48, 60, 62, 74, 76])

# 2. Fit the model
model = LinearRegression().fit(hours, score)

# 3. Read the results
print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))
print("R2:", round(model.score(hours, score), 2))
print("Score for 6 hours:", model.predict([[6]])[0])

# 4. Plot the data and the fitted line
plt.scatter(hours, score, color="red", label="Data")
plt.plot(hours, model.predict(hours), label="Fit")
plt.xlabel("Hours"); plt.ylabel("Score")
plt.legend(); plt.show()
