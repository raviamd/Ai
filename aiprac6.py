# Adaboost Ensemble Learning
# Implement the Adaboost algorithm to create an ensemble of weak classifiers.
# Train the ensemble model on a given dataset and evaluate its performance
# Compare the results with individual weak classifiers
import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 6]
seed = 7
num_trees = 30
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed, algorithm='SAMME')
results = model_selection.cross_val_score(model, X, Y)
print("Mean Accuracy:", results.mean())

# AdaBoost (Adaptive Boosting) - Short Answer:

# AdaBoost is an ensemble learning algorithm that combines multiple weak classifiers (models that perform slightly better than random guessing) to form a strong classifier. It focuses on instances that previous models misclassified by assigning them higher weights in the next iteration.

# Key Steps:
# Initialize weights for all training data points equally.
# Train a weak classifier (e.g., decision stump).
# Update weights: Increase the weight of misclassified samples, so they are given more importance in the next round.
# Repeat: Train the next weak classifier on the updated data.
# Combine weak classifiers: Final prediction is made based on a weighted majority vote of all weak classifiers.
# Use Case: AdaBoost is often used in classification problems, like face detection, where improving accuracy incrementally through boosting can significantly enhance performance.

