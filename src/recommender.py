import numpy as np
import pandas as pd

col_list = ["id", "categories", "name", "popularity", "calories", "like", "nope"]
foodlist = pd.read_csv('../data/foodList.csv', usecols=col_list)

# foodlist.catergoies = foodlist.catergoies.str.lower()


# print(foodlist["categories"])
max_list = []
nope_list = []

for x in foodlist:
    for item in foodlist[x]:
        
        if x == "like":
            max_list.append(item)
            print(max_list)
            # find the maximum value from the list 
            maxNum = max(max_list)
            # print(maxNum)
            #     
        elif x == "nope":
            nope_list.append(item)
            print(nope_list)
            # find the min Nope value from the list 
            minNope = min(nope_list)
            print(minNope)
               

    