import pandas as pd
import os
import sys

file_path = 'C:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'

# Read the CSV file into a Pandas DataFrame
file = pd.read_csv(file_path,header=0,low_memory=False, encoding="latin-1")

print(file)
            

    

