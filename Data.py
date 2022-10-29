# describing the data frame

print(dataframe.describe())

 

print("-----------------------------")

# finding unique values

print(dataframe['Maths_marks'].unique())

 

print("-----------------------------")

# counting unique values

print(dataframe['Maths_marks'].nunique())

 

print("-----------------------------")

# display the columns in the data frame

print(dataframe.columns)

 

print("-----------------------------")

# information about dataframe

print(dataframe.info())
