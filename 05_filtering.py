import pandas as pd
import numpy as np

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


# Warm-up (single condition)

# Show all Pokémon with a Height below 1.
print(df[df["Height"] <1 ])

# Show all Pokémon with a Weight between 50 and 100 (inclusive).

print(df[(df["Weight"] >= 50) & (df["Weight"] <= 100)])
# Show all Pokémon whose Type1 is “Grass”.

print(df["Type1"] == "Grass")
# Show all non-Legendary Pokémon. (Hint: use == False or ~.)
mask = df[~(df["Legendary"] == 1)] 
print(mask)
# Combining conditions
# 5. Find Pokémon that are both Legendary and taller than 1.54.

print(df[(df["Legendary"] == 1) & (df["Height"] > 1.54)])
# 6. Find Pokémon that are Type1 “Electric” or Type1 “Ground”.
print(df[((df["Type1"] == "Electric") | (df["Type1"] == "Ground"))])
# 7. Find Pokémon that are heavy (Weight >= 200) but not tall (Height < 2).

print(df[(df["Weight"] >= 200) & (df["Height"] < 2)])
# 8. Find Pokémon with Type1 “Dragon” and a missing Type2. (Hint: .isna().)

print(df[(df["Type1"] == "Dragon") & (df["Type2"].isna())])

# Using other methods
# 9. Use .isin() to get all Pokémon whose Type1 is Water, Fire, or Grass.
# Check which rows have a Type1 that is Water, Fire, or Grass

mask = df["Type1"].isin(["Water","Fire","Grass"])
print(df[mask])
# 10. Use .str.startswith("Char") to find all Pokémon whose Name starts with “Char”.

print(df[df["Name"].str.startswith("Char")])
# 11. Count how many Legendary Pokémon there are. (Hint: len() or .shape[0].)
print(df[df["Legendary"] == 1].shape[0])
print(df[df["Legendary"] == 1].shape[1])
print(df[df["Legendary"] == 1])
# 12. Use .query() to rewrite your tall filter.
# query() is a method that lets you filter a DataFrame using a human-readable, SQL-like string expression.
filtered_df = df.query(" Height > 1.5")
print(filtered_df)

# Challenge
# 13. Find the Pokémon with the highest BMI, then show only the Name and BMI columns.
print(df.sort_values(by="BMI",ascending=False)[["Name","BMI"]].head(1))

# 14. Find the average Weight of Fire-type Pokémon (checking both Type1 and Type2).
fire = df[(df["Type1"] == "Fire") | (df["Type2"] == "Fire")]
print(np.nanmean(fire["Weight"]))
# 15. Show the top 5 tallest Legendary Pokémon, sorted from tallest to shortest.

print(df.sort_values(by="Height",ascending= False).head(5))