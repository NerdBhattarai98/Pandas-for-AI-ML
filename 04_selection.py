import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Anbit Bhattarai\Desktop\Pandas-for-AI-ML\Data\Data.csv",index_col = "Name")
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

print(df.loc["Muk"])
print(df.iloc[df.index.get_loc("Muk")])
# Print the last 5 rows using .tail().

print(df.tail(5))
# Level 2: Selection and filtering
# Show all Pokémon taller than 1.5 m, with only the Height and Weight columns.

mask = df["Height"] > 1.5
print(df[mask],["Height","Weight"])
# Show Pokémon with Weight between 20 and 60 (use &).
mask = (df["Weight"] > 20) & (df["Weight"] < 60)
print(df[mask])
# Show every 3rd Pokémon from row 0 to row 20 using iloc.
print(df.iloc[0:21:3])
# Print the names (index) of all Pokémon whose name starts with "P". Hint: df.index.str.startswith("P").

print(df[df.index.str.startswith("P")])
print(df.index.str.startswith("P").sum())
# Level 3: Sorting and calculations
# Find the 3 lightest and the 3 heaviest Pokémon.
print(df["Weight"].sort_values(ascending= False).head(3))
print(df.sort_values(by= "Weight" ,ascending= False).head(3))
print(df.sort_values(by= "Weight" ,ascending= False).tail(3))
# Add a column Weight_lb (kg × 2.205), rounded to 1 decimal.
df["Weight_lbs"] = df["Weight"] * 2.205
print(df)
# Add a column Size that is "Big" if Height > 1.5, otherwise "Small". Hint: np.where(condition, "Big", "Small") after import numpy as np.
df["Size"] = np.where(df["Height"] >1.5,"Big","Small")
print(df)
# Use idxmax() and idxmin() to find the tallest and shortest Pokémon by name.
tallest = df["Height"].idxmax()
print(f"Tallest Pokémon: {tallest}")

smallest = df["Height"].idxmin()
print(f"Smallest Pokemon: {smallest}")

# idxmax(): Returns the index label (or row name) of the maximum value in a column.
# idxmin(): Returns the index label (or row name) of the minimum value in a column.

print(df.idxmax()) #Returns for each

# Level 4: Exploration (ML-style)
# Run df.info(), df.describe(), and df.isnull().sum(). Write a comment explaining what each tells you.
print(df.info())

# <class 'pandas.DataFrame'>
# Index: 150 entries, Bulbasaur to Mewtwo
# Data columns (total 9 columns):
#  #   Column      Non-Null Count  Dtype  
# ---  ------      --------------  -----  
#  0   No          150 non-null    int64  
#  1   Type1       150 non-null    str    
#  2   Type2       67 non-null     str    
#  3   Height      150 non-null    float64
#  4   Weight      150 non-null    float64
#  5   Legendary   150 non-null    int64  
#  6   BMI         150 non-null    float64
#  7   Weight_lbs  150 non-null    float64
#  8   Size        150 non-null    str    
# dtypes: float64(4), int64(2), str(3)
# memory usage: 15.8+ KB
# None

# Dimensions (Index: 150 entries, 9 columns): Your dataset has 150 rows (Pokémon) and 9 columns. The index uses Pokémon names (ranging from Bulbasaur to Mewtwo), confirming your index_col = "Name" worked.

# Missing Values (Non-Null Count): Most columns show 150 non-null, meaning they have no missing data. However, Type2 only has 67 non-null, which means 83 Pokémon do not have a secondary type (they have missing/NaN values).

# Data Types (Dtype): It shows you the type of data stored in each column:

# int64: Whole numbers (like No, Legendary)

# float64: Decimals (like Height, Weight, BMI, Weight_lbs)

# str: Text strings (like Type1, Type2, Size)




# Memory Usage (15.8+ KB): How much RAM your DataFrame is currently taking up in your computer's memory (very lightweight here!).

print(df.describe())
#                No      Height      Weight   Legendary         BMI   Weight_lbs
# count  150.000000  150.000000  150.000000  150.000000  150.000000   150.000000
# mean    75.500000    1.200000   46.231333    0.026667   32.851333   101.940090
# std     43.445368    0.963634   59.547388    0.161647   23.305876   131.301991
# min      1.000000    0.200000    0.100000    0.000000    0.000000     0.220500
# 25%     38.250000    0.700000    9.925000    0.000000   20.725000    21.884625
# 50%     75.500000    1.000000   30.000000    0.000000   29.500000    66.150000
# 75%    112.750000    1.500000   56.375000    0.000000   38.675000   124.306875
# max    150.000000    8.800000  460.000000    1.000000  153.100000  1014.300000\





# In the Python data analysis library pandas, the df.describe() method is used to generate descriptive statistics of a DataFrame
# , string (object or text) columns are completely ignored by df.describe()
print(df.describe(include=['object']))

#         Type1   Type2   Size
# count     150      67    150
# unique     15      11      2
# top     Water  Poison  Small
# freq       28      19    118

# Type1: The most common value is Water, and it appears 28 times in that column.

# Type2: The most common value is Poison, and it appears 19 times in that column. (Note: The count is only 67 because many rows have missing/null values for Type2).

# Size: The most common value is Small, and it appears 118 times out of the 150 rows.

df.to_csv("pokemon_with_bmi.csv")

print(df.isnull().sum())

# No             0
# Type1          0
# Type2         83
# Height         0
# Weight         0
# Legendary      0
# BMI            0
# Weight_lbs     0
# Size           0
# dtype: int64
#_________________________________________________________________________________________________________________________________________________________________________
# Find the mean and median of Height and Weight. Are they very different? What might that mean?

print(df["Height"].mean())
print(df["Height"].median())

# 1.2
# 1.0

# Use df["Size"].value_counts() to count how many are Big vs Small.

print(df["Size"].value_counts())
# If your CSV has a Type column, use df.groupby("Type")[["Height", "Weight"]].mean().
print(df.groupby("Type1")[["Height", "Weight"]].mean())



