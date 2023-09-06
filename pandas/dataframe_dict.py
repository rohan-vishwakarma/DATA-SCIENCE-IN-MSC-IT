import sys
import os
import pandas as pd

dictionary = {
    "name": "rohan",
    "age" : 12,
    "city": "thane"
}
a = 12

data = pd.DataFrame(dictionary, index=['1'])

print(data)