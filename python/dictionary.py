import pandas as pd

data = {
  "Names": ["Kriti", "rohan", "tanvi"],
  "City": ["Bhandup", "Thane", "Badlapur"]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
a = df.columns[0:2]

print(a) 
print(df)