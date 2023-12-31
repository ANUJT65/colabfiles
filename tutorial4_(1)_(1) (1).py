# -*- coding: utf-8 -*-
"""Tutorial4_(1)_(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1azo3Bb3-6LsIDox8h9G0hknFvdb_kPIV
"""

#DV

#Anuj Tadkase
#CSAI-A
#ROLL NUM 64


#1)finding relationships corr method:calculate relationship among each column in your dataset
#2)BSN correlation test between 2 variables :
#experiance,salary
#3) eg of linear regression = data.csv
#4)correlation matrix
#5)regression table
#6)regression coeff
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

mydata = pd.read_csv("data.csv")
print(mydata)

#CREATING DATA FRAME
df = pd.DataFrame(
   {
      "experience": [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35],
      "salary": [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 200000, 230000, 250000, 300000, 350000, 400000]

   }
)


col1, col2 = "experience", "salary"
corr = df[col1].corr(df[col2])
print(corr)



#CORRELATION MATRIX
df = pd.DataFrame(mydata)
corr_matrix = df.corr()
print(corr_matrix)

#CORRELATION OF 2 COLUMNS
experience = [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30, 35]
salary = [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 200000, 230000, 250000, 300000, 350000, 400000]
pearson_corr = np.corrcoef(experience, salary)[0, 1]

#PLOT CHART OF THE 2 VARIABLES
plt.figure(figsize=(8, 6))
plt.scatter(experience, salary, alpha=0.5)
plt.title('Bivariate Scatterplot: Experience vs Salary')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

print(f"Pearson Correlation Coefficient: {pearson_corr:.2f}")
#CORELATION COEFFICIENT

x = [ [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35] ]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

print(x)

print(y)

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"coefficients: {model.coef_}")

y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")

y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)
print(f"predicted response:\n{y_pred}")

x_new = np.arange(10).reshape((-1, 2))
x_new



y_new = model.predict(x_new)
y_new

csv = pd.read_csv('data.csv')
x = df.iloc[:,:-1].values
y = df.iloc[:,:-1].values
print(x)
x, y = np.array(x), np.array(y)

model = LinearRegression().fit(x, y)
#FITTING MODEL
r_sq = model.score(x, y)
#FINDING OUT R_SQ
print(f"coefficient of determination: {r_sq}")

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
#COEFFICIENT OF DETERMINATION

print(f"intercept: {model.intercept_}")
#INTERCEPT

print(f"coefficients: {model.coef_}")
#MODEL COEFFICIENT

y_pred = model.predict(x)
#PREDICTING X

print(y_pred)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([15, 11, 2, 8, 25, 32])
#Transform input data
transformer = PolynomialFeatures(degree=2, include_bias=False)

transformer.fit(x)

x_ = transformer.transform(x)
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

model = LinearRegression().fit(x_, y)
r_sq = model.score(x_, y)

print(f"coefficient of determination: {r_sq}")

print(f"coefficients: {model.coef_}")

print(f"intercept: {model.intercept_}")