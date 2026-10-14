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