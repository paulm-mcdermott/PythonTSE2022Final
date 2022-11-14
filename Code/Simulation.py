import pandas as pd
import datetime as dt
import os
import random

from Classes.Customer import HipsterCustomer, ReturningCustomer
from Classes.Store import Store
from Functions import *

# #################################
# NOTES
# #################################

# This file runs the simulation for Part 3. We run it over the 5-year period.
# The analysis is completed in 'SimulationAnalysis.py'
#
# For running the simulation, we state the menus (based on given prices and probabilities from 'Exploratory.py')
# We then create a returning customer list (1/3 hipsters). We set a random seed and then simulate the 5 years of
# data. This takes under 3 minutes. We store the ledger in a csv file so that it can be easily accessed later on.


# Please run the below line and amend as necessary to set the directory for your computer
os.path.abspath('.')

# directory = '/Users/justinstandish-white/PycharmProjects/exam-mcdermott-standish-white'
directory = '/Users/paulmcdermott/PycharmProjects/exam-mcdermott-standish-white'

# Setting up database of times with menu probabilities

food_menu = pd.DataFrame([['Cookie', 2, 0, 1 / 8, 4 / 30],
                          ['Muffin', 3, 0, 1 / 8, 4 / 30],
                          ['Pie', 3, 0, 1 / 8, 4 / 30],
                          ['Sandwich', 2, 0, 5 / 8, 0],
                          ['None', 0, 1, 0, 3 / 5]],
                         columns=['food_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                         )
print(food_menu)
drinks_menu = pd.DataFrame([['Coffee', 3, 1 / 3, 1 / 12, 1 / 6],
                            ['Frappucino', 4, 2 / 15, 1 / 12, 1 / 6],
                            ['Milkshake', 5, 2 / 15, 1 / 12, 1 / 6],
                            ['Soda', 3, 2 / 15, 7 / 12, 1 / 6],
                            ['Tea', 3, 2 / 15, 1 / 12, 1 / 6],
                            ['Water', 2, 2 / 15, 1 / 12, 1 / 6]],
                           columns=['drink_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                           )

# create hipster and returning customers
hipster_list = [HipsterCustomer("H" + str(i)) for i in range(1, 334)]
returning_list = [ReturningCustomer("R" + str(i)) for i in range(334, 1001)]
all_returning_list = returning_list + hipster_list

# instantiate store
coffee_shop = Store(food_menu, drinks_menu, all_returning_list)

# set seed
random.seed(7)

# make a list of 5-years worth of days
date_list = pd.date_range(start="2016-01-01", end="2020-12-31")
date_list_2 = list(map(datetime_to_date, date_list))

# for each day, run day of business function
for i in date_list_2:
    day_of_business(i, coffee_shop)

# retrieve full 5-year ledger
df_ledger = coffee_shop.retrieve_ledger()
print(df_ledger)
df_ledger.to_csv(directory + '/Results/Part 3/SimulationLedger.csv', sep=",", index=False)
df_ledger = pd.read_csv(directory + '/Results/Part 3/SimulationLedger.csv', sep=',')

# Brief analysis: here we answer the question of how many returning customers are left.
print(len(coffee_shop.viable_ret_cust))
# 672 returning customers left, number may change with random variation but set.seed should prevent that.
# This means that 328 customers were removed for insufficient funds.

# Reminder: you will find analysis of this simulation, including graphs, in the SimulationAnalysis.py file






