
from utilities import *
import pandas as pd 
from sklearn.datasets import make_blobs

# helloWorld()

# load and clean the data
df = loadAndCleanData("creditData.csv")

# df_new = loadAndCleanData("newLoans.csv")

# df2 = computePDF("age",df)

# df3= viewDistribution("age", df)

# df4 = computeDefaultRisk('age',2, df, 1)
# print("The probability is: ")
# print(computeProbability("age",[0,40],df))

print("The probability  for [0:40] is: ")
print(computeDefaultRisk("SeriousDlqin2yrs", "age",[0,40],df ))
print("The probability  for [40:80] is: ")
print(computeDefaultRisk("SeriousDlqin2yrs", "age",[40,80],df ))
print("The probability  for [80:120] is: ")
print(computeDefaultRisk("SeriousDlqin2yrs","age",[80,120],df ))


