import pandas as pd

#Data Cleaning = the process of fixing/remocing:incomplete,incorrect or irrelevant data

df = pd.read_csv(r"C:\Users\Anbit Bhattarai\Desktop\Pandas-for-AI-ML\pokemon_with_bmi.csv")

# df = df.drop(columns=["Legendary"])
# print(df)

#2 Handle Missing Data
# df = df.dropna(subset = ["Type2"])#Drops not availabale
# print(df.to_string())
# print(df.shape[0])

#fill the nan values

df = df.fillna({"Type2" : "None"})
print(df)

#Fix inconsistent values

df["Type1"] = df["Type1"].replace({"Grass" : "GRASS",
                                   "Fire" : "FIRE",
                                   "Water": "WATER"})
print(df)

#Standardize Text

df["Name"] = df["Name"].str.lower() #lower cases values

# $fix data types
df["Legendary"] = df["Legendary"].astype(bool)
print(df)

df.to_csv(r"C:\Users\Anbit Bhattarai\Desktop\Pandas-for-AI-ML\pokemon_with_bmi.csv")

#Remove duplicate values

df = df.drop_duplicates()
print(df)