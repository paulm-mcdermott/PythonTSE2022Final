
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

# This file is in two parts. First, we run the simulation over 5 years. Second, we compute some additional
# analysis for part 4. The analysis of the simulation data itself is completed in a separate file.
#
# For running the simulation, we state the menus (based on given prices and probabilities from 'Exploratory.py')
# We then create a returning customer list (1/3 hipsters). We set a random seed and then simulate the 5 years of
# data. This takes under 3 minutes. We store the ledger in a csv file so that it can be easily accessed later on.


# Please run the below line and amend as necessary to set the directory for your computer
os.path.abspath('.')

directory = '/Users/justinstandish-white/PycharmProjects/exam-mcdermott-standish-white'
# directory = '/Users/paulmcdermott/PycharmProjects/exam-mcdermott-standish-white'

# Setting up database of times with menu probabilities

food_menu = pd.DataFrame([['Cookie',   2, 0, 1 / 8, 4 / 30],
                          ['Muffin',   3, 0, 1 / 8, 4 / 30],
                          ['Pie',      3, 0, 1 / 8, 4 / 30],
                          ['Sandwich', 2, 0, 5 / 8, 0],
                          ['None',     0, 1, 0,     3 / 5]],
                         columns=['food_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                         )
print(food_menu)
drinks_menu = pd.DataFrame([['Coffee',     3, 1 / 3,  1 / 12, 1 / 6],
                            ['Frappucino', 4, 2 / 15, 1 / 12, 1 / 6],
                            ['Milkshake',  5, 2 / 15, 1 / 12, 1 / 6],
                            ['Soda',       3, 2 / 15, 7 / 12, 1 / 6],
                            ['Tea',        3, 2 / 15, 1 / 12, 1 / 6],
                            ['Water',      2, 2 / 15, 1 / 12, 1 / 6]],
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
df_ledger.to_csv(directory + '/Results/Part 3/SimulationLedger.csv', sep=",", index=False)
df_ledger = pd.read_csv(directory + '/Results/Part 3/SimulationLedger.csv', sep=',')
print(df_ledger)

# Brief analysis: here we answer the question of how many returning customers are left.
print(len(all_returning_list))
# 672 returning customers left, number may change with random variation but set.seed should prevent that.
# This means that 128 customers were removed for insufficient funds.

####################
# Part 4:          #
####################

# show some histories of returning customers
# pick three random returning customers
sample_returning = random.choices(coffee_shop.viable_ret_cust, k=3)

# print out the histories of the random returning customers
for i in sample_returning:
    print(i.retrieve_purchase_history())

# Lower returning to 50 customers, then run same simulation
hipster_list_p4 = [HipsterCustomer("H" + str(i)) for i in range(1, 20)]
returning_list_p4 = [ReturningCustomer("R" + str(i)) for i in range(20, 51)]
all_returning_list_p4 = returning_list_p4 + hipster_list_p4
coffee_shop_p4 = Store(food_menu, drinks_menu, all_returning_list_p4)

# for each day, run day of business function
for i in date_list_2:
    day_of_business(i, coffee_shop_p4)
df_ledger_p4 = coffee_shop_p4.retrieve_ledger()
print(df_ledger_p4)
