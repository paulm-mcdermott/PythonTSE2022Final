import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

# load csv into dataframe
coffeebar_df = pd.read_csv('../Data/Coffeebar_2016-2020.csv', sep=';')
print(coffeebar_df.head(5))

#all food types served, dropped NaN
print(coffeebar_df["FOOD"].dropna().unique())

# all drinks types served, always order drink so no dropna
print(coffeebar_df["DRINKS"].unique())

# count unique customer ids
print(len(coffeebar_df["CUSTOMER"].unique()))

# bar chart for food order frequency
# TO DO: make it prettier, find better solution than plt.show()
coffeebar_df["FOOD"].value_counts().plot.bar()
plt.show()

# bar chart for drink order frequency
# TO DO: make it prettier, find better solution than plt.show()
coffeebar_df["DRINKS"].value_counts().plot.bar()
plt.show()

# TO DO: more cool plots

# TO DO: part 1 last bullet
# convert time to date time for easier extraction of timestamp
coffeebar_df['DATETIME'] = pd.to_datetime(coffeebar_df['TIME'])
print(coffeebar_df['DATETIME'])

# add column that is just the time stamp
coffeebar_df['TIMESTAMP'] = coffeebar_df['DATETIME'].dt.time
print(coffeebar_df['TIMESTAMP'])

# get food counts for each timestamp
print(coffeebar_df[['TIMESTAMP','FOOD']].groupby('TIMESTAMP').value_counts())










