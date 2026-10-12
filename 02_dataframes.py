import pandas as pd
import numpy as np

#Dataframes in python
# Dataframes = A tabular data structure with rows And coloumns.(2D)
# Similar to Excel spreadsheet

data = {"Name": ["Spongebob","Patrick","Squidward"],
        "Age": [30,35,50],
}

df = pd.DataFrame(data)
print(df)

#Output:

#         Name  Age
# 0  Spongebob   30
# 1    Patrick   35
# 2  Squidward   50

#Output comes in Rows and Columns

#Setup Custom index

df = pd.DataFrame(data,index= ["Employee 1","Employee 2","Employee 3"])
print(df)

#                  Name  Age
# Employee 1  Spongebob   30
# Employee 2    Patrick   35
# Employee 3  Squidward   50

#To access rows

print(df.loc["Employee 2"])
# Name    Patrick
# Age          35
# Name: Employee 2, dtype: object

#selection by iloc

print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

#Add new column

df["Job"] = ["Burger Maker","Waiter","Customer"] #The number should be equal to the number of rows

print(df)

#Add new row

new_row = pd.DataFrame([{"Name": "Sandy",
                         "Age": 28,
                         "Job": "Engineer"}],index = ["Employee 4"])#Index narakhe label 0 aaucha

df = pd.concat([df,new_row])
print(df)


#Add new rows
new_rows= pd.DataFrame([{"Name": "Anbit",
                         "Age": 20,
                         "Job": "Data Engineer"},
                         {"Name": "Achut",
                         "Age": 47,
                         "Job": " Engineer"}],index = ["Employee 5","Employee 6"]
                        )

df = pd.concat([df,new_rows])
print(df)

#Practice qns for this

# Level 1: Basics (creating DataFrames)
# Create a DataFrame called students with columns
#  Name, Marks, and City for 4 students of your choice. Print it.

df = {"Name": ["Abhinav Bista","Anbit Bhattarai","Pranil Prasai","Sakshi Sapkota"],
      "Marks":[48,0,0,52],
      "City":["Tikapur","Kavrepalanchowk","Taplejung","Lumbini Allstars"]}

df = pd.DataFrame(df,index=["Student1","Student2","Student3","Student4"])
print(df)
# Recreate the same DataFrame, but use a custom index like ["Student 1", "Student 2", "Student 3", "Student 4"].
df = pd.DataFrame(df,index=["Student1","Student2","Student3","Student4"])
print(df)
# Print only the Name column using students["Name"]. What type of object do you get back? (Use type() to check.)
print(df["Name"])


# Level 2: Accessing data

# Use .loc to print the row for "Student 3".
print(df.loc["Student3"])
# Use .iloc to print the last row (hint: try a negative index).

print(df.iloc[-1])
# Print the first two rows using .iloc with slicing.

print(df.iloc[0:2])
# Using .loc, print the Marks of "Student 2" only (a single value).

print(df.loc["Student2","Marks"])
# Print the Name and City columns together (hint: pass a list of column names).
print(df.loc[:,["Name","City"]])
# Level 3: Adding columns
# Add a new column Grade with a value for each student.
df["Grade"] = ["A", "B", "A", "C"]


# Add a column Passed that is True if Marks >= 40, otherwise False. Try doing it without a loop: df["Marks"] >= 40.
df["Passed"] = df["Marks"]>40
print(df)


# Add a column Bonus Marks that is Marks + 5 for every student.
df["Marks"] += 5
print(df)
# What error do you get if you add a column with only 3 values when there are 4 rows? Try it and read the message.
# like index is 4 but you only give 3 values one


# Level 4: Adding rows

# Add a single new student using pd.concat() with a custom index label.

new_row = pd.DataFrame([{"Name": "Srijal Joshi",
                        "Marks": 52,
                        "City": "Dhangadhi",
                        "Grade": "A",
                        "Passed": True}],index = ["Student5"])

df = pd.concat([df,new_row])
print(df)
# Add two new students at once.

new_rows = pd.DataFrame([{"Name": "Princika Chapagain",
                        "Marks": 0,
                        "City": "Kathmandu",
                        "Grade": "B",
                        "Passed": False},
                        {"Name": "Kritishma Singh Maharjan Sapkota",
                        "Marks": 15,
                        "City": "Lalitpur",
                        "Grade": "B",
                        "Passed": False}],index = ["Student6","Student7"])

df = pd.concat([df,new_rows])
print(df)
# Add a new row without specifying an index. Look at what index label appears (your note says 0). Then fix it using ignore_index=True.

new_row = pd.DataFrame([{"Name": "Srijal Joshi",
                        "Marks": 52,
                        "City": "Dhangadhi",
                        "Grade": "A",
                        "Passed": True}])

df = pd.concat([df,new_row],ignore_index=True) #ignore_index=True basically removes the custom labels made earlier and starts everything from 0
print(df)

# Level 5: Mini challenges
# Create a DataFrame of 5 products with Product, Price, and Quantity. Add a Total column (Price * Quantity). Then add 2 new products and print the final table.

df1 = {"Product":["Iphone","Samsung","Xiomi","MI","OnePlus"],
      "Price":[40000,50000,60000,70000,100000],
      "Quantity":[50,700,46,99,58]}

df = pd.DataFrame(df1)
print(df)

#Add new Total Column

df["Total"] = df["Price"] * df["Quantity"]
print(df)

# Then add 2 new products and print the final table.

new_rows = pd.DataFrame([{"Product" : "Dell",
                          "Price": 53042,
                          "Quantity": 91
                         },
                          {"Product" : "Acer",
                          "Price": 5342,
                          "Quantity": 108
                          }])

new_rows["Total"] = new_rows["Price"] * new_rows["Quantity"]
df = pd.concat([df,new_rows],ignore_index= True)
print(df)
# Use df.shape, df.columns, df.index, and df.dtypes on any of your DataFrames. Write a comment explaining what each one returns.
print(df.shape)
# (7, 4) This is returned as there are 7 products and 4 rows
print(df.columns)
# Index(['Product', 'Price', 'Quantity', 'Total'], dtype='str') Gives the rows of dataset
print(df.index)
# RangeIndex(start=0, stop=7, step=1) starts from 0 ends at 6

# Print the row of the person with the highest value in a numeric column (hint: look up idxmax()).
print(df.idxmax())
# Find index of maximum value
# Product     2
# Price       4
# Quantity    1
# Total       1
# dtype: int64

# Drop a column and drop a row (hint: df.drop(...), and think about the axis parameter).
df = df.drop("Price", axis=1) #Entire column gone
print(df)

df = df.drop(1, axis=0) #Entire row of index 1 gone
print(df)

print(df.loc[df["Total"].idxmax()])# Gets max of only one rows