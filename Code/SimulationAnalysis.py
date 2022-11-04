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


os.path.abspath('.')
# directory = '/Users/justinstandish-white/PycharmProjects/exam-mcdermott-standish-white'
directory = '/Users/paulmcdermott/PycharmProjects/exam-mcdermott-standish-white'

df_ledger = pd.read_csv(directory + '/Results/SimulationLedger.csv', sep=',')



####### Data ANALYSIS

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
plt.savefig(directory + '/Results/MonthlyIncome.png', dpi=300)

# No clear trends, makes sense given the model

# tips over time

monthly_agg_tip = df_ledger.groupby(by='YrMonth')[['tip']].agg('sum')

monthly_agg_tip.plot(kind="bar", rot=0, legend = None)

x_ticks = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
x_labels = ['Jan-\'16', 'Jul-\'16', 'Jan-\'17', 'Jul-\'17', 'Jan-\'18', 'Jul-\'18', 'Jan-\'19', 'Jul-\'19', 'Jan-\'20', 'Jul-\'20']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Monthly Tip Total')
plt.xlabel('Month')
plt.title('Total Monthly Tips, 2016-2020')

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/MonthlyTips.png', dpi=300)

# No trends either, trip advisor customers remain equally likely over time

# tips and income

monthly_agg = df_ledger.groupby(by='YrMonth').agg('sum')

monthly_agg.plot(kind="bar",  rot=0)

x_ticks = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
x_labels = ['Jan-\'16', 'Jul-\'16', 'Jan-\'17', 'Jul-\'17', 'Jan-\'18', 'Jul-\'18', 'Jan-\'19', 'Jul-\'19', 'Jan-\'20', 'Jul-\'20']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Monthly Tip Total')
plt.xlabel('Month')
plt.title('Total Monthly Income Including Tips, 2016-2020')
plt.legend(title='Category', loc='right',labels =['Total Income', 'Total Tips'])

plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/MonthlyIncTips.png', dpi=300)

# combined plot


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
plt.savefig(directory + '/Results/IncomeByTimes.png', dpi=300)

# time segments are clear, more expensive combinations are most likely at midday. Morning session has the
# lowest average transaction as people don't buy food
# tips are constant, tripadvisor prob. is constant over time and so is EV of tip generator


# food dist in simulation

df_ledger['food_choice'] = df_ledger['food_choice'].replace('None',np.nan)

ct_food = pd.crosstab(df_ledger['food_choice'], df_ledger['YEAR'])

ct_food.plot(kind="bar", stacked=True, rot=0)
plt.ylabel('Quantity Sold')
plt.xlabel('Food')
plt.title('Quantity of Food Sold, 2016-2020')
plt.legend(title = 'Year', loc='upper left')

plt.gcf().set_size_inches(9,7)
plt.savefig(directory + '/Results/FoodFreqSim.png', dpi=300)
# plt.show()

# some variation but ratios are there.

