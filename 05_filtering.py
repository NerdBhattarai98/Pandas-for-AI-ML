import pandas as pd

df = pd.read_csv(r"C:\Users\Anbit Bhattarai\Desktop\Pandas-for-AI-ML\pokemon_with_bmi.csv")
print(df)

tall = df[df["Height"] >= 2]
print(tall)
#Filtered Pokemon with height lower

heavy = df[df["Weight"] >= 200]
print(heavy)

legendary = df[df["Legendary"] == True]
legendary = df[df["Legendary"] == 1]
print(legendary)

type = df[(df["Type1"] == "Water") |(df["Type2"] == "Water")]
print(type)

ff = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff)