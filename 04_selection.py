import pandas as pd

df = pd.read_csv(r"C:\Users\anbit\OneDrive\Desktop\Pandas-for-AI-ML\Data\Data.csv",index_col = "Name")
print(df)
# The error happened because you used index_col="Name" when reading your CSV file. This changes Name from 
# a regular column into the DataFrame's index.

#Selection by column
# print(df["Name"]) #This is a series

# print(df["Name"].to_string())
# print(df["Height"])
# print(df["Weight"])

# #for multiple column

# print(df[["Name","Weight"]])

# print(df[["Name","Weight"]].to_string())
# Name is no longer a regular column. It is the index.So cannot use like this
#we get error

#Selection by Rows
print(df)
# print(df.loc[0]) #Based on like index 

#We can serve "Name" as Label
# ,index_col = "Name while reading csv this is given so the name acts as column

print(df.loc["Pikachu"])
print(df.loc["Charizard"])

#If we dont want all columns while seleciton through rows

print(df.loc["Pikachu" : "Muk",["Height","Weight"]])
# df.loc["Pikachu":"Muk"] is inclusive of both ends (label slicing),

print(df.iloc[0:11:2])#11 is exclusive 
print(df.iloc[0:11:2,0:3])#11 is exclusive 

# pokemon = input("Enter a pokemon Name: ")

# try:
#     print(df.loc[pokemon])
# except:
#     print(f"{pokemon} Unavailable")

df2 = df.reset_index()
print(df2["Name"])
# # reset_index() undoes what index_col="Name" did. It moves the index back into a regular column and gives the DataFrame a fresh numeric index

print(df.sort_values("Weight", ascending=False).head(5)) #Top 5 rows based on the weight

df["BMI"] = (df["Weight"] / (df["Height"] ** 2)).round(1)
print(df[["Height", "Weight", "BMI"]].head(10))


# df[["Height", "Weight", "BMI"]] selects the three specified columns.
# .head() displays the first 5 rows of those columns.
# print() displays the result in your terminal.

# Use a raw string

# Save your result
df.to_csv("pokemon_with_bmi.csv")

# Level 1: Warm-up
# Print the shape of the DataFrame (rows, columns).
print(df.shape)
# Print only the Weight column for the first 8 Pokémon.
print(df["Weight"].head(8))
# Select the row for "Muk" using loc, then the same row using iloc (find its position first with df.index.get_loc("Muk")).
# Print the last 5 rows using .tail().
# Level 2: Selection and filtering
# Show all Pokémon taller than 1.5 m, with only the Height and Weight columns.
# Show Pokémon with Weight between 20 and 60 (use &).
# Show every 3rd Pokémon from row 0 to row 20 using iloc.
# Print the names (index) of all Pokémon whose name starts with "P". Hint: df.index.str.startswith("P").
# Level 3: Sorting and calculations
# Find the 3 lightest and the 3 heaviest Pokémon.
# Add a column Weight_lb (kg × 2.205), rounded to 1 decimal.
# Add a column Size that is "Big" if Height > 1.5, otherwise "Small". Hint: np.where(condition, "Big", "Small") after import numpy as np.
# Use idxmax() and idxmin() to find the tallest and shortest Pokémon by name.
# Level 4: Exploration (ML-style)
# Run df.info(), df.describe(), and df.isnull().sum(). Write a comment explaining what each tells you.
# Find the mean and median of Height and Weight. Are they very different? What might that mean?
# Use df["Size"].value_counts() to count how many are Big vs Small.
# If your CSV has a Type column, use df.groupby("Type")[["Height", "Weight"]].mean().
# Level 5: Mini project

# Build a small Pokémon lookup tool:

# Ask the user for a name (use .strip().title() so “pikachu” works).
# If found, print its Height, Weight, and BMI nicely formatted, for example: Pikachu: 0.4 m, 6.0 kg, BMI 37.5
# If not found, catch KeyError and suggest similar names using df.index.str.contains(...).
# Loop until the user types quit.
# Challenge questions to think about
# Why does df.loc["Pikachu":"Muk"] include Muk but df.iloc[0:5] excludes position 5?
# What happens to df after df.sort_values(...) if you don’t assign the result? Why?
# Why does df[df["Weight"] > 50 and df["Height"] < 2] raise an error?