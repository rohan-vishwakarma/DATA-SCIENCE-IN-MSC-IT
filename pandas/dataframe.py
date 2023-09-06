import abc
import pandas as pd


mydataset = {
    'Name' : ["rohan", "priya", "aishwarya"],
    'City' : ["thane", "mumbai", "pune"],
    'Gender' : ["Male", "Female", "Female"],
}


frame = pd.DataFrame(mydataset)


print(frame)
