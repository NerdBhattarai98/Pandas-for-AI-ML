#Pandas - Panel Data

#Series - 1D labeled column
#Dataframes - 2D labled table

import pandas as pd

print (pd.__version__)

#Series = A Pandas 1-Dimensional labeled array that can hold any data types
# (Eg: Single column in a spreadsheet)

data1 = [100.01,102.20,104.08]
data2 = ["A","B","C"]
data3 = [100,102,104]
data4 = [True,False,False]
series = pd.Series(data1) #Series is a constructor not a data so it is in uppercase
print(series)

#OUTPUT:
# 0    100.01
# 1    102.20
# 2    104.08
# dtype: float64


#IF DATATYPE IS CHANGED THE METADATA CHANGES TOO

series = pd.Series(data2) #Series is a constructor not a data so it is in uppercase
print(series)

# 0    A
# 1    B
# 2    C
# dtype: object

series = pd.Series(data3) #Series is a constructor not a data so it is in uppercase
print(series)

# 0    100
# 1    102
# 2    104
# dtype: int64

series = pd.Series(data4)
print(series)

# 0     True
# 1    False
# 2    False
# dtype: bool

data = [100,102,104]
series = pd.Series(data, index =["a","b","c"]) #Custom Index

print(series)

# a    100
# b    102
# c    104
# dtype: int64

#access direct values

print(series.loc["a"])#Selects the value at the "index"
# .loc mean location

#To change the value
series.loc["b"] = 200
print(series)

# a    100
# b    200
# c    104
# dtype: int64

#The elements can be accessed through interger location as well

print(series.iloc[0])
# 100

print(series.iloc[1])
# 200

print(series.iloc[2])
# 104

a = [100,102,104,200,202,204,205]

series = pd.Series(a,index = ["a","b","c","d","e","f","g"])
print(series)

#Filering the data 
#Greater than 200

print(series[series >= 200])
# d    200
# e    202
# f    204
# g    205
# dtype: int64

#less than 200
print(series[series <= 200])
# a    100
# b    102
# c    104
# d    200
# dtype: int64

#Using a dictionary

calories = {"Day 1" : 1760,
            "Day 2" : 2100,
            "Day 3" : 1700}

series = pd.Series(calories)
print(series)

#The Day Represents the index in this case
print(series.loc["Day 3"])
series.loc["Day 3"] += 1000
print(series.loc["Day 3"])
print(series)

#filer by value

print(series[series >= 2000])

# Day 2    2100
# Day 3    2700
# dtype: int64

print(series[series <= 2000])

# Day 1    1760
# dtype: int64

#Exercise

a = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard"]
pokemon = pd.Series(a,index = [1,2,3,4,5,6])
print(pokemon)

#practice qns

import pandas as pd

marks = pd.Series([72, 85, 90, 65, 58],
                  index=["Asha", "Bikash", "Chitra", "Dev", "Esha"])

prices = pd.Series([120.5, 99.0, 150.25, 80.0])

calories = {"Mon": 1800, "Tue": 2200, "Wed": 1950, "Thu": 2500}

# Print marks. What is its dtype? What is its index?
print(marks)
# Print Chitra’s mark using .loc, then Dev’s mark using .iloc.
print(marks.loc["Chitra"])
print(marks.iloc[3])
# Create a Series from the calories dictionary. What becomes the index?
calories = pd.Series(calories)
print(calories)
# when you create a Pandas Series from a dictionary, the dictionary's keys become the Series index by default, and the dictionary's values become the Series data.
# Change Esha’s mark to 63, then print the Series.

marks["Esha"] = 63
print(marks)
# Asha      72
# Bikash    85
# Chitra    90
# Dev       65
# Esha      63
# dtype: int64

# Predict
# What dtype does pd.Series([1, 2, 3.5]) have? What about pd.Series([1, 2, "3"])? What about pd.Series([True, False, True])?

#  pd.Series([1, 2, 3.5]) - this has dtype of float
# pd.Series([1, 2, "3"]) - this has dtype of object
# pd.Series([True, False, True])- this has dtype of bool


# What does prices.index show? Why are those numbers there when you didn’t give an index?
print(prices.index)
# RangeIndex(start=0, stop=4, step=1) this is shown because it auto indexes startinh from 0 to the number of object which in this case is stop-1
# What is marks.iloc[1]? What is marks.loc[1]? Which one raises an error, and why?

# marks.iloc[1]- this means at the integer location of 1 like even though the index is given an integer location starting from 0 is always there
# marks.loc[1]- the value at index 1

# marks.loc[1] - raised the error as the index consists of names rather than number in marks

# What does marks * 2 return: a number, a Series, or an error? What happens to the index?
#it returns the series multiplied but the index isn't of the values are
# What is the shape of marks? (Use marks.shape.) Compare with a NumPy 1D array of 5 elements.
print(marks.shape)
#same as 1d array with 5 elements (5,)

# Filtering
# Select students with marks of at least 70.

print(marks[marks >= 70])

# Select students with marks between 60 and 85 (inclusive). Remember the parentheses and &.

print(marks[(marks >= 60) & (marks <= 85)])


# Select students who are not above 80. Use ~ carefully.
print(marks[~(marks > 80)])
# Print only the names (the index) of students who scored above 70. Hint: marks[mask].index.

mask = marks >= 70
print(marks[mask].index)


