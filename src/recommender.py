import numpy as np
import pandas as pd

col_list = ["userId", "categories", "name", "popularity", "calories", "like", "nope"]
foodlist = pd.read_csv('../data/foodList.csv', usecols=col_list)


# print out all the data rows and cols from csv
# print(foodlist.head())
foodlist = foodlist.sample(10)
# print(foodlist.shape)


uni_users = foodlist['userId'].unique()
# print("uniUsers:" + str(len(uni_users)))

uni_dishes = foodlist['name'].unique()
# print(len(uni_dishes))


newDF = pd.DataFrame(uni_users)
newDF.columns = ['userId']
# np.isnan(newDF.columns)

for item in uni_dishes:
    newDF[item] = None

for i, user in enumerate(newDF['userId'].values):
    # if np.isnan(i) == False:
        for j in range(foodlist[foodlist['userId']==user].shape[0]):
            # print(user)
            dish_id = foodlist[foodlist['userId']==user]['name'].iloc[j]
            rating = foodlist[foodlist['userId']==user]['popularity'].iloc[j]
            newDF[dish_id][j] = rating

# print(newDF.sample(5))

user = pd.DataFrame(newDF.iloc[2])
user = user.drop(['userId'])
user[user.notnull().values]

# print(user[user.notnull().values])

subset = newDF[newDF[user[user.notnull().values].index[0]].notnull()]
subset.head()
print(subset.head())
# max_list = []
# nope_list = []

# for x in foodlist:
#     for item in foodlist[x]:
        
#         if x == "like":
#             max_list.append(item)
#             print(max_list)
#             # find the maximum value from the list 
#             maxNum = max(max_list)
#             # print(maxNum)
#             #     
#         elif x == "nope":
#             nope_list.append(item)
#             print(nope_list)
#             # find the min Nope value from the list 
#             minNope = min(nope_list)
#             print(minNope)
               

    