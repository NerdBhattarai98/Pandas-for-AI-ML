#Learn to import CSV and JSON Files
#CSV - Comma Seperated Values
#JSON - JavaScript Object Notation

import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\anbit\OneDrive\Desktop\Pandas-for-AI-ML\Data\Data.csv")
print(df)
#Gives out truncated value (First 5 and Last 5)

#To print all the data not a truncated version

print(df.to_string())
print("The Sum is",df["Weight"].sum())

print("The Average of weight is",(df["Weight"].sum())/len(df))

#To read a json file



print("The median of the weight is: ",np.median(df["Weight"]))

q1,q2,q3 = np.percentile(df["Weight"],[25,50,75])
print(q1)
print(q2)
print(q3)

InQuRa = q3 - q1
print(InQuRa)

UL = q3 + 1.5 * InQuRa

LL = q1 - 1.5 * InQuRa

print(LL,UL)

mask = (df["Weight"] < LL) | (df["Weight"] > UL)
print("Outliers",df[mask])

#To read a json file:

df = pd.read_json(r"C:\Users\anbit\OneDrive\Desktop\Pandas-for-AI-ML\Data\sample1.json")
print(df.to_string())
