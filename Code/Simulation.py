import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os

# Setting up database of times with menu probabilities

food_prob = pd.DataFrame(columns = ['Time', 'Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'])
drinks_prob = pd.DataFrame(columns = ['Time', 'Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'])

timedelta = dt.timedelta(hours = 8)
incr = dt.timedelta(minutes = 1)

ind = 1

while timedelta < dt.timedelta(hours = 18):

    time = (dt.datetime.min + timedelta).time()
    hour = time.hour

    if hour < 11:
        food_i = pd.DataFrame([[time, 0, 0, 0, 0, 1]],
                              columns = ['Time', 'Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index = [ind])
        food_prob = pd.concat([food_prob, food_i])

        drinks_i = pd.DataFrame([[time, 1 / 3, 2 / 15, 2 / 15, 2 / 15, 2 / 15, 2 / 15]],
                                columns=['Time', 'Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index = [ind])
        drinks_prob = pd.concat([drinks_prob, drinks_i])

    elif (hour >= 11) & (hour < 13):
        food_i = pd.DataFrame([[time, 1/8, 1/8, 1/8, 5/8, 0]],
                              columns=['Time', 'Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index = [ind])
        food_prob = pd.concat([food_prob, food_i])

        drinks_i = pd.DataFrame([[time, 1/12, 1/12, 1/12, 7/12, 1/12, 1/12]],
                                columns=['Time', 'Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[ind])
        drinks_prob = pd.concat([drinks_prob, drinks_i])

    else:
        food_i = pd.DataFrame([[time, 4/30, 4/30, 4/30, 0, 3/5]],
                              columns=['Time', 'Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index = [ind])
        food_prob = pd.concat([food_prob, food_i])

        drinks_i = pd.DataFrame([[time, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6]],
                                columns=['Time', 'Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[ind])
        drinks_prob = pd.concat([drinks_prob, drinks_i])

    print(timedelta)
    timedelta = timedelta + incr
    ind = ind + 1

# CSV's to check
food_prob.to_csv('Results/Food_Prob.csv')
drinks_prob.to_csv('Results/Drinks_Prob.csv')



# Prices menus

food_menu = pd.DataFrame( [2, 3, 3, 2, 0], columns = ['Price'], index=['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'])
drinks_menu = pd.DataFrame( [3, 4, 5, 3, 3, 2], columns = ['Price'], index=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'])

elements = ["A", "B"]
probs = [.1,.9]
x = np.random.choice(elements, 1, p = probs)
print(type(x[0]))

df = pd.DataFrame(np.random.randn(26,5), columns=['col'+str(i) for i in range(5)],index=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
df['cat'] = list('aaaabbbccddef' * 2)

idx = pd.period_range('2013-01', periods=len(df), freq='M')
df.index = idx
february_selector = (df.index.month == 2)
february_data = df[february_selector]

q1_data = df[(df.index.month >= 1) & (df.index.month <= 3)] # note: & not "and"
mayornov_data = df[(df.index.month == 5) | (df.index.month == 11)] # note: | not "or"
annual_tot = df.groupby(df.index.year).sum()


print((food_prob[food_prob.index.hour == 8]) # == dt.time(hour = 17, minute = 59))

times_practice = []
for hour in range(8,18):
    for minute in range(0, 60, 1):
        times_practice.append(dt.time(hour = hour, minute=minute))

print(len(times_practice))

df2 = pd.DataFrame(np.random.randn(600), columns=['val'])
df2.index = times_practice

sub1 = (df2.index. == 8)