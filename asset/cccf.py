import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
"""
 🔢 Rating Converter Web-App 🔢


"""
print("Importing the required libraries....\n")
time.sleep(2)

print('Running the program....\n')
time.sleep(2)
cccf = pd.read_csv('asset\cccf.csv')
print('Loading the dataset....\n')
time.sleep(2)
print(cccf.head())
time.sleep(5)
print()

print("Getting info....\n")
time.sleep(1)
print("Info of the dataset is\n")
time.sleep(2)
print(cccf.info())
time.sleep(5)
print()

cc = cccf.loc[:, ['cc_username', 'cc_rating']]
print("Fetching the data of codechef users....\n")
time.sleep(1)
print("Data of codechef users is\n")
time.sleep(2)
print(cc.head())
time.sleep(5)
print()

cf = cccf.loc[:, ['cf_username', 'cf_rating']]
print("Fetching the data of codeforces users....\n")
time.sleep(1)
print("Data of codeforces users is\n")
time.sleep(1)
print(cf.head())
time.sleep(5)
print()

print("Processing the data....\n")
time.sleep(2)
new = cccf.dropna(how='any')
print("Dataset after handling NaN values is\n")
time.sleep(2)
print(new.head())
time.sleep(5)
print()

print("Applying Linear Regression to get a relation between the ratings of both the platforms by using np.polyfit which provides a best fit curve based on least square method....\n")
time.sleep(4)
slope, intercept = np.polyfit(
    new['cc_rating'], new['cf_rating'], 1)  # cf=m*cc+b
print("The slope and intercept obtained are",
      slope, "and", intercept, "respectively\n")
time.sleep(2)

print("The correlation between the codeforces and codechef rating can be given as....")
time.sleep(2)
print(cc['cc_rating'].corr(cf['cf_rating']))
time.sleep(3)
print()

print("Now filling the dataset's NaN value by the result obtained by the Linear Regression model....")
time.sleep(3)
cccf['cf_rating'] = cccf['cf_rating'].fillna(cccf['cc_rating']*slope+intercept)
cccf['cc_rating'] = cccf['cc_rating'].fillna(
    (cccf['cf_rating']-intercept)/slope)

final_csv = cccf
print("Dataset after filling the NaN value is\n")
time.sleep(2)
print(final_csv)
time.sleep(5)
print()


print("Getting info....\n")
time.sleep(2)
print("Info of the dataset is\n")
print(final_csv.info())
time.sleep(5)
print()
print("No null values are present now\n")
time.sleep(2)

print("Adding the final .csv file....\n")
time.sleep(3)
final_csv.to_csv('asset/final_csv.csv', index=False)

print("Plot of the final dataset is available in assets directory\n")
sns.lmplot(
    data=new,
    x="cc_rating", y="cf_rating", height=8, aspect=1.5, fit_reg=True, scatter=True
)
