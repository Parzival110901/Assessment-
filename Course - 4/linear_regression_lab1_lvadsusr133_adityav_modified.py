# -*- coding: utf-8 -*-
"""Linear Regression-Lab1-lvadsusr133-AdityaV-modified.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-vXRb3r5ZMJztZRfNBk90OpZBR6B34kL
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Step 1: Read Data
df = pd.read_csv('/content/auto-mpg.csv')

# Step 2: Replace Missing Values
# Perform Label Encoding for the 'origin' column
label_encoder = LabelEncoder()
df['origin'] = label_encoder.fit_transform(df['origin'])

# Replace missing values with median for numeric columns
imputer = SimpleImputer(strategy='median')
numeric_cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year']
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

# Step 3: Remove Outliers
# No need to remove outliers for linear regression

# Step 4: Perform Exploratory Data Analysis (EDA)
# Summary Statistics
print(df.describe())

# Visualization
sns.pairplot(df)
plt.show()

# Step 5: Model Training and Testing
# Define features and target variable
X = df.drop(['mpg', 'car name'], axis=1)  # Exclude 'car name' as it's not useful for modeling
y = df['mpg']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Linear Regression Model
regression_model = LinearRegression()
regression_model.fit(X_train_scaled, y_train)

# Step 6: Model Evaluation
# Predict on test set
y_pred = regression_model.predict(X_test_scaled)

# Model Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)