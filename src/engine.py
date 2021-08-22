import numpy as np
import pandas as pd

col = ['name', 'categories', 'like', 'nope', 'ingredient']
foodlist = pd.read_csv('../data/foodList.csv', usecols=col)


def combine_functions(data):
    func = []
    for i in range(0, data.shape[0]):
        func.append(str(data['name'][i]) + ' ' + str(data['categories'][i]) + ' ' + str(data['like'][i])+ ' ' + str(data['nope'][i]))

    return func

# eliminating all NaN value from that data frame 
foodlist.dropna(subset=["categories"], inplace=True)

# Sorting the column of like
foodlist.sort_values(["like"], inplace=True, ascending=False)
print(foodlist)

def chosenCategory(category):
    list = []
    count = 0
    for i in range(3):
        if i == "western" or i == "japanese":
            list.append(category)
            count += 1
    for i in list:
        print (i)

list = []
count = 0
index = 0
for i in foodlist['categories']:
    print(i)

    if i == "western" or i == "japanese":
            list.append(i)
            print(foodlist['ingredient'][index])
            count += 1
    index += 1
print(list)
print(count)




# def swipe_count(x):
#     like_count = 0
#     pass_count = 0

#     for i in range(3):
#         if not list:
#             chosenCategory()
        