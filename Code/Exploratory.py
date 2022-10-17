import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

# load csv into dataframe
coffeebar_df = pd.read_csv('../Data/Coffeebar_2016-2020.csv', sep=';')
print(coffeebar_df.head(5))

#all food types served, dropped NaN
print(coffeebar_df["FOOD"].dropna().unique())

# all drinks types served, dropped NaN
print(coffeebar_df["DRINKS"].dropna().unique())

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