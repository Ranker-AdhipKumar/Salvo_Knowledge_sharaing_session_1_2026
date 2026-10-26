"""
Salvo - Knowledge Sharing Session 1 (2026)
Topic: Logistic Regression Decision Boundary
Description: Trains a logistic regression classifier on 2D synthetic blob data
             and visualizes the classification decision regions and boundary.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay

# 1. Data: two features, two classes
X, y = make_blobs(n_samples=120, centers=2,
                  cluster_std=2.2, random_state=3)

# 2. Fit the model
model = LogisticRegression().fit(X, y)

# 3. Accuracy
print("Accuracy:", round(model.score(X, y), 2))

# 4. Plot the shaded decision regions
DecisionBoundaryDisplay.from_estimator(
    model, X, cmap="coolwarm", alpha=0.5,
    response_method="predict_proba")
plt.scatter(X[:, 0], X[:, 1], c=y,
            cmap="coolwarm", edgecolor="k")
plt.xlabel("Feature 1"); plt.ylabel("Feature 2")
plt.show()
