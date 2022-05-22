import pandas as pd
import csv

df = pd.read_csv("p130.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

print(df.shape)
print(list(df))

df.to_csv('edited.csv')