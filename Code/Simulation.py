from typing import List

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os
import random
from Classes.Customer import HipsterCustomer, ReturningCustomer
from Classes.Store import Store
from Functions import *

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

print(drinks_menu)
# create hipster and returning customers
hipster_list = [HipsterCustomer("H" + str(i)) for i in range(1, 334)]
returning_list = [ReturningCustomer("R" + str(i)) for i in range(334, 1001)]
all_returning_list = returning_list + hipster_list

print(random.choice(all_returning_list))
print(all_returning_list)
# instantiate store
coffee_shop = Store(food_menu, drinks_menu, all_returning_list)
times_idx = pd.period_range("2000-01-01 8:00", freq="T", periods=600)
for i in times_idx[:9]:
    minute_of_business(i, coffee_shop)
print(coffee_shop.retrieve_ledger().loc[:, 'customer_id':'tip'])
