import pandas as pd

import os

import test.py

directory = r"C:\Users\super\PyCharmProjects\untitled\GW_data_strip"
identity = "_processed"

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print(filename)
        filepath = os.path.join(directory, filename)

        data = pd.read_csv(filepath)
        print(data)
        print(data.mean(axis = 0))
        data.to_csv(r'C:\Users\super\PyCharmProjects\untitled\GW_data_processing\%s %s.csv'%(filename,identity),index = None, header = True)

    else:
        continue



data.head()

#Gov Win Rate
#Opp Win Rate
#Average Speaks
#Average Ranks

def gwr(data);

    return