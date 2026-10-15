import pandas as pd

# aggregate? = reduces set of values to a describing single value

df = pd.read_csv(r"C:\Users\Anbit Bhattarai\Desktop\Pandas-for-AI-ML\pokemon_with_bmi.csv")

#Whole Dataframe
print(df.mean(numeric_only= True))
print(df.sum(numeric_only= True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

#For single columns
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count())

#groupby( - function)


group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count().sort_values(ascending=False).head(1))

# Warm-up (whole DataFrame / single columns)

# Find the average Weight of all Pokémon.
print(df["Weight"].mean())
# Find the maximum BMI and the minimum BMI.
print(df["BMI"].max())
# Find the total number of Pokémon (rows) in the dataset.
print(df["Name"].count())
# Use .describe() on the Height and Weight columns. What do you notice?
print(df["Height"].describe())
# Find the median Height. How does it compare to the mean?
print(df["Height"].mean())
print(df["Height"].median())

#median is 1.2 ans mean is 1.0 that means the outliers there are not much as these values are close to each other
# Basic groupby
# 6. Find the average Weight for each Type1.

group = df.groupby("Type1")
print(group["Weight"].mean())
# 7. Find the maximum Height for each Type1.

print(group["Height"].max())
# 8. Count how many Pokémon there are in each Type1.
print(group["Height"].count())
# 9. Find the total Weight for each Type1, sorted from highest to lowest.
print(group["Weight"].sum().sort_values(ascending = False))
# 10. Find the average BMI for Legendary vs non-Legendary Pokémon.

# legend = df.groupby("Legendary")
# print(legend["BMI"].mean())
# Going a bit further
# 11. Which Type1 has the highest average Weight? (Hint: .idxmax() or .sort_values().head(1).)

print(group["Weight"].mean().sort_values(ascending= False).head(1))
# 12. Which Type1 has the lowest average Height?
print(group["Height"].mean().sort_values().head(1))
# 13. Use .agg() to get the min, max, and mean Height for each Type1 in one table.
print(group["Height"].agg(["min", "max", "mean"]))
# 14. Use .agg() with a dictionary to get the mean Height and the max Weight for each Type1 at once.


