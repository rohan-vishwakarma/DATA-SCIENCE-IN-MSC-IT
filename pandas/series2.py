import pandas as pd


calories = {'day-1' :'hello', "day-2": 'by'}

df = pd.Series(calories, index=['day-1', 'day-2'])
print(df)


# OUTPUT

# day-1    hello
# day-2       by
# dtype: object