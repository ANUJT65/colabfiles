# -*- coding: utf-8 -*-
"""lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wtn2LKnMh_9hzzv1bxA-OVFKYNvQAC-H
"""

# Write a Python program to display some basic statistical details like percentile, mean, standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and
# ‘Iris-versicolor’ of iris.csv dataset.
#name= anuj tadkase, roll num = 64, div cs ai-A



import pandas as pd
import numpy as np

mydata = pd.read_csv("IRIS.csv")
print(mydata)

mydata.mean()
#mean of whole table

mydata.describe()
#brief description of data

mydata.std()
#std deviation of entire data

mydata.groupby("species").mean()
#gives mean of data by species

mydata.groupby("species").std()
#gives std deviation of data by species

mydata.groupby("species").quantile(0.5)
#percentile by species

mydata.groupby("species").quantile(0.25)
#25th percentile by species

mydata.groupby("species").quantile(0.1)
#100 percentile of entire table

sepals = np.percentile(mydata['sepal_length'], [25, 50, 75])
#using percentile by np
# Display the percentiles
print("25th Percentile of sepal_length:", sepals[0])
print("Median (50th Percentile) of sepal_length:", sepals[1])
print("75th Percentile of sepal_length:", sepals[2])

sepals = np.percentile(mydata['sepal_length'], [10, 90, 20])
#using percentile by np
# Display the percentiles
print("10th Percentile of sepal_length:", sepals[0])
print(" (90th Percentile) of sepal_length:", sepals[1])
print("20th Percentile of sepal_length:", sepals[2])

sepals2 = np.percentile(mydata['sepal_width'], [10, 90, 20])
#using percentile by np
# Display the percentiles
print("10th Percentile of sepal_width:", sepals2[0])
print(" (90th Percentile) of sepal_width:", sepals2[1])
print("20th Percentile of sepal_width:", sepals2[2])

sepals3 = np.percentile(mydata['petal_length'], [10, 90, 20])
#using percentile by np
# Display the percentiles
print("10th Percentile of petal_length:", sepals3[0])
print(" (90th Percentile) of petal_length:", sepals3[1])
print("20th Percentile of petal_length:", sepals3[2])

sepals4 = np.percentile(mydata['petal_width'], [10, 90, 20])
#using percentile by np
# Display the percentiles
print("10th Percentile of petal_width:", sepals4[0])
print(" (90th Percentile) of petal_width:", sepals4[1])
print("20th Percentile of petal_width:", sepals4[2])

mydata.quantile(0.5)
#50th percentile by table

mydata.quantile(0.25)
#25th percentile of table

mydata.quantile(0.10)

#10th percentile

mydata.quantile(0.90)
#90th percentile using pandas

mydata.quantile(0.75)
#75th percentile using pandas

#summary
#in this assignment we have actually found out various ways in which we can find the mean ,
#description of data set,also various ways in which we can find percentile or quantile of different datas of the flowers.
#we have used various commands like groupby,quantile,percentile,mean,description etc.
#we have used the data set IRIS.csv
#in the assignment we have also found out various parameters by grouping by species also like mean length,width of sepals and petals also various percentiles  aswell