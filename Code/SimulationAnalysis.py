from typing import List

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os
import random
import time

import Functions
from Classes.Customer import HipsterCustomer, ReturningCustomer
from Classes.Store import Store
from Functions import *

# Load your own directory to prevent issues
os.path.abspath('.')
directory = '/Users/justinstandish-white/PycharmProjects/exam-mcdermott-standish-white'
# directory = '/Users/paulmcdermott/PycharmProjects/exam-mcdermott-standish-white'

df_ledger = pd.read_csv(directory + '/Results/Part 3/SimulationLedger.csv', sep=',')

# TODO note the number of returning customers at the end of the simulation

######################################
# Analysing Simulation Data          #
######################################

print(df_ledger.head(7))


df_ledger['DATETIME'] = pd.to_datetime(df_ledger['date_time'])

df_ledger['TIMESTAMP'] = df_ledger['DATETIME'].dt.time
df_ledger['YrMonth'] = df_ledger['DATETIME'].dt.strftime('%Y-%m')
df_ledger['YEAR'] = df_ledger['DATETIME'].dt.year

# Monthly Income

monthly_agg_tv = df_ledger.groupby(by='YrMonth')[['transaction_value']].agg('sum')

monthly_agg_tv.plot(kind="bar",  rot=0, legend = None)

x_ticks = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
x_labels = ['Jan-\'16', 'Jul-\'16', 'Jan-\'17', 'Jul-\'17', 'Jan-\'18', 'Jul-\'18', 'Jan-\'19', 'Jul-\'19', 'Jan-\'20', 'Jul-\'20']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Monthly Total Income')
plt.xlabel('Month')
plt.title('Total Monthly Income, 2016-2020')

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 3/MonthlyIncome.png', dpi=300)

# We see a constant trend over time here which makes sense in our model, as the probabilities of different spending
# behaviour does not change over time. All parameters are constant and all types of customers have the same spending
# behaviour aside from tips. As we have a large body of returning customers (1000), we don't 'run out' of such customers
# and thereby, the probability of a TripAdvisor customer coming doesn't change. Hence, the average tip amount will be
# constant in it's expected value.
# over the period, we note that the average monthly income is just over €20 000.

# tips over time

monthly_agg_tip = df_ledger.groupby(by='YrMonth')[['tip']].agg('sum')

monthly_agg_tip.plot(kind="bar", rot=0, legend=None)

x_ticks = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
x_labels = ['Jan-\'16', 'Jul-\'16', 'Jan-\'17', 'Jul-\'17', 'Jan-\'18', 'Jul-\'18', 'Jan-\'19', 'Jul-\'19', 'Jan-\'20', 'Jul-\'20']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Monthly Tip Total')
plt.xlabel('Month')
plt.title('Total Monthly Tips, 2016-2020')

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 3/MonthlyTips.png', dpi=300)

# As discussed above, the probability of trip advisor customers doesn't change over time. Hence, we see a constant
# trend in tip levels. Total amount of tips comes to around €2 000 per month on average, therefore making up around
# 10% of total income for the store.

# tips and income

monthly_agg = df_ledger.groupby(by='YrMonth').agg('sum')
monthly_agg.pop('YEAR')

monthly_agg.plot(kind="bar",  rot=0)

x_ticks = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
x_labels = ['Jan-\'16', 'Jul-\'16', 'Jan-\'17', 'Jul-\'17', 'Jan-\'18', 'Jul-\'18', 'Jan-\'19', 'Jul-\'19', 'Jan-\'20', 'Jul-\'20']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Monthly Tip Total')
plt.xlabel('Month')
plt.title('Total Monthly Income Including Tips, 2016-2020')
plt.legend(title='Category', loc='right',labels =['Total Income', 'Total Tips'])

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 3/MonthlyIncTips.png', dpi=300)

# This simply combines the two previous plots.


# Income by times

time_agg = df_ledger.groupby(by='TIMESTAMP').agg('mean')
time_agg.pop('YEAR')

time_agg.plot(kind="bar",  rot=0, linewidth=.5)

x_ticks = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]
x_labels = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Average Value')
plt.xlabel('Time')
plt.title('Average Transaction and Tip by Time of Day, 2016-2020')
plt.legend(title='Category', loc='upper right',labels =['Transactions', 'Tips'])

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 3/IncomeByTimes.png', dpi=300)

# The three time segments are made clear in this plot.
# The morning slot has the lowest average value (just under €4) due to no one buying food at this time.
# The lunch slot has the highest average (just under 6) due to everyone buying a food then.
# The afternoon slot is in the middle with an average of just under €5, as the prob. of buying a food item is 40%.
# There is a constant trend for tips, as tip amounts are independent of time of day.


# Food Distribution in Simulation

df_ledger['food_choice'] = df_ledger['food_choice'].replace('None',np.nan)

ct_food = pd.crosstab(df_ledger['food_choice'], df_ledger['YEAR'])

ct_food.plot(kind="bar", stacked=True, rot=0)
plt.ylabel('Quantity Sold')
plt.xlabel('Food')
plt.title('Quantity of Food Sold, 2016-2020')
plt.legend(title = 'Year', loc='upper left')

plt.gcf().set_size_inches(9,7)
plt.savefig(directory + '/Results/Part 3/FoodFreqSim.png', dpi=300)
# plt.show()

# This is a replication of a similar plot in the given coffee_bar data. We see similar trends in that consumption across
# years is roughly equal and sandwiches are clearly more popular. However, in the previous case, sandwiches were
# twice as popular whilst here it is more 1.3x. This is because we have a constant probability of customers entering the
# store in a given minute, across the day. The given data had variations with the most customer density being in the
# lunch slot, when sandwiches are most popular. This is a simplification in our model and we see the results here.


