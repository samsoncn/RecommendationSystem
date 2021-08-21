import numpy as np
import pandas as pd

col = ['name', 'categories', 'like']
foodlist = pd.read_csv('../data/foodList.csv', usecols=col)


def combine_functions(data):
    func = []
    for i in range(0, data.shape[0]):
        func.append(str(data['name'][i]) + ' ' + str(data['categories'][i]) + ' ' + str(data['like'][i]))

    return func

# eliminating all NaN value from that data frame 
foodlist.dropna(subset=["categories"], inplace=True)

# Sorting the column of like
foodlist.sort_values(["like"], inplace=True, ascending=False)
print(foodlist)