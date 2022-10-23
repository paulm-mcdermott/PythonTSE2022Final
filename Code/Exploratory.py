import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os

# load csv into dataframe
inputfile1 = os.path.abspath('../exam-mcdermott-standish-white/Data/Coffeebar_2016-2020.csv')
# NOTE had to modify to work on mine, should be generalisable but pls check
# Uh oh, doesn't work on mine TODO: Figure this out
coffeebar_df = pd.read_csv(inputfile1, sep=';')
print(coffeebar_df.head(5))


#all food types served, dropped NaN
print(coffeebar_df["FOOD"].dropna().unique())

# all drinks types served, always order drink so no dropna
print(coffeebar_df["DRINKS"].unique())

# count unique customer ids
print(len(coffeebar_df["CUSTOMER"].unique()))

# create year variable for plots
coffeebar_df['YEAR'] = pd.DatetimeIndex(coffeebar_df['TIME']).year


# bar chart for food order frequency

ct_food = pd.crosstab(coffeebar_df['FOOD'], coffeebar_df['YEAR'])

ct_food.plot(kind="bar", stacked = True, rot=0)
plt.ylabel('Quantity Sold')
plt.xlabel('Food')
plt.title('Quantity of Food Sold, 2016-2020')
plt.gcf().set_size_inches(9,6)
plt.savefig('Results/FoodFreq.png', dpi=300)
#plt.show()

# bar chart for drink order frequency

ct_drinks = pd.crosstab(coffeebar_df['DRINKS'], coffeebar_df['YEAR'])

ct_drinks.plot(kind="bar", stacked = True, rot=0)
plt.ylabel('Quantity Sold')
plt.xlabel('Drinks')
plt.title('Quantity of Drinks Sold by Year')
plt.gcf().set_size_inches(9,6)
plt.savefig('Results/DrinksFreq.png', dpi=300)
#plt.show()


# TO DO: more cool plots

# PAUL APPROACH
# TO DO: part 1 last bullet
# convert time to date time for easier extraction of timestamp
coffeebar_df['DATETIME'] = pd.to_datetime(coffeebar_df['TIME'])
print(coffeebar_df['DATETIME'])

# add column that is just the time stamp
coffeebar_df['TIMESTAMP'] = coffeebar_df['DATETIME'].dt.time
print(coffeebar_df['TIMESTAMP'])

# get food counts for each timestamp
print(coffeebar_df[['TIMESTAMP','FOOD']].groupby('TIMESTAMP').value_counts())


# JUSTIN APPROACH
# FOOD
# Change Nan's to 'None' so they show up in the crosstab

print(coffeebar_df['FOOD'].tail(10))
coffeebar_df['FOOD'] = coffeebar_df['FOOD'].fillna("none")
print(coffeebar_df['FOOD'].tail(10))

ct_time_food = pd.crosstab(coffeebar_df['TIMESTAMP'], coffeebar_df['FOOD'], normalize = 'index')*100
print(ct_time_food)
ct_time_food.to_csv('Results/FoodDist.csv')

ct_time_food.plot(kind="bar", stacked = True, rot=0)

x_ticks = [     0,     12,     24,       36,      66,      96,      111,    126,     141,    156,        171]
x_labels = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Percentage of Food Sales')
plt.xlabel('Time')
plt.title('Distribution of Food Sales over Time')
plt.legend(title='Food Type', loc='lower right')

plt.gcf().set_size_inches(9,6)
plt.savefig('Results/FoodDist.png', dpi=300)

#plt.show()

# Drinks

ct_time_drinks = pd.crosstab(coffeebar_df['TIMESTAMP'], coffeebar_df['DRINKS'], normalize = 'index')*100
print(ct_time_drinks)
ct_time_food.to_csv('Results/DrinksDist.csv')

ct_time_drinks.plot(kind="bar", stacked = True, rot=0)

x_ticks = [     0,     12,     24,       36,      66,      96,      111,    126,     141,    156,        171]
x_labels = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Percentage of Drinks Sales')
plt.xlabel('Time')
plt.title('Distribution of Drinks Sales over Time')
plt.legend(title='Drink Type', loc='lower right')

plt.gcf().set_size_inches(9,6)
plt.savefig('Results/DrinksDist.png', dpi=300)

#plt.show()





