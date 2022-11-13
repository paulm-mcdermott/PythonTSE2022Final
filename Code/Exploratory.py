import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os

# #################################
# NOTES
# #################################

# This is the file that explores the given coffee bar dataset.
# At first, we get the basic information requested such as what the bar serves
# Then, we present several graphs. These will automatically save to the relevant directory

# USER NOTE: Please add your relevant directory and comment out the other directory options below.

# #################################
# #################################
# #################################


# load csv into dataframe - Please run the below line and amend as necessary to set the directory for your computer
os.path.abspath('.')
directory = '/Users/paulmcdermott/PycharmProjects/exam-mcdermott-standish-white'
# directory = '/Users/justinstandish-white/PycharmProjects/exam-mcdermott-standish-white'
coffeebar_df = pd.read_csv(directory + '/Data/Coffeebar_2016-2020.csv', sep=';')

print(coffeebar_df.head(5))

# all food types served, dropped NaN
print(coffeebar_df["FOOD"].dropna().unique())

# all drinks types served, always order drink so no dropna
print(coffeebar_df["DRINKS"].unique())

# count unique customer ids
print(len(coffeebar_df["CUSTOMER"].unique()))

# create year variable for plots
coffeebar_df['YEAR'] = pd.DatetimeIndex(coffeebar_df['TIME']).year

# #################################
# bar chart for food order frequency

ct_food = pd.crosstab(coffeebar_df['FOOD'], coffeebar_df['YEAR'])

ct_food.plot(kind="bar", stacked=True, rot=0)
plt.ylabel('Quantity Sold')
plt.xlabel('Food')
plt.title('Quantity of Food Sold, 2016-2020')
plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 1/FoodFreq.png', dpi=300)
# plt.show()

# ###################################
# bar chart for drink order frequency

ct_drinks = pd.crosstab(coffeebar_df['DRINKS'], coffeebar_df['YEAR'])

ct_drinks.plot(kind="bar", stacked=True, rot=0)
plt.ylabel('Quantity Sold')
plt.xlabel('Drinks')
plt.title('Quantity of Drinks Sold, 2016-2020')
plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 1/DrinksFreq.png', dpi=300)
# plt.show()

# ####################################
# Probabilities of different purchases

# convert time to date time for easier extraction of timestamp
coffeebar_df['DATETIME'] = pd.to_datetime(coffeebar_df['TIME'])
print(coffeebar_df['DATETIME'])

# add column that is just the time stamp
coffeebar_df['TIMESTAMP'] = coffeebar_df['DATETIME'].dt.time
print(coffeebar_df['TIMESTAMP'])


# Food
# Change Nan's to 'None' so they show up in the crosstab

coffeebar_df['FOOD'] = coffeebar_df['FOOD'].fillna("none")

ct_time_food = pd.crosstab(coffeebar_df['TIMESTAMP'], coffeebar_df['FOOD'], normalize='index')*100
print(ct_time_food)
ct_time_food.to_csv(directory + '/Results/Part 1/FoodDist.csv')
ct_time_food.plot(kind="bar", stacked=True, rot=0)

x_ticks = [0, 12, 24, 36, 66, 96, 111, 126, 141, 156, 171]
x_labels = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Percentage of Food Sales')
plt.xlabel('Time')
plt.title('Distribution of Food Sales over Time')
plt.legend(title='Food Type', loc='lower right')

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 1/FoodDist.png', dpi=300)

# plt.show()

# Observed probabilities:
# 8-11: 100% none
# 11-13: 12.5% cookie muffin pie, 62.5% sandwich
# 13-18: 13.33% (4/30) cookie muffin pie. 60% none

# #################################
# Drinks

ct_time_drinks = pd.crosstab(coffeebar_df['TIMESTAMP'], coffeebar_df['DRINKS'], normalize='index') * 100
print(ct_time_drinks)
ct_time_drinks.to_csv(directory + '/Results/Part 1/DrinksDist.csv')

ct_time_drinks.plot(kind="bar", stacked=True, rot=0)

x_ticks = [0, 12, 24, 36, 66, 96, 111, 126, 141, 156, 171]
x_labels = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Percentage of Drinks Sales')
plt.xlabel('Time')
plt.title('Distribution of Drinks Sales over Time')
plt.legend(title='Drink Type', loc='lower right')

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 1/DrinksDist.png', dpi=300)

# plt.show()

# Observed probabilities:
# 8-11: coffee 1/3, everything else 2/15
# 11-13: soda = 7/12, everything else 1/12
# 13-18: all drinks 16.66% (1/6)
