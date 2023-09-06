import pandas as pd

list_of_name= ["rohan", "ritika", "roohi", "ishika"]

df = pd.Series(list_of_name, index=[1,2,3, 4])

print(df[1], df[2])