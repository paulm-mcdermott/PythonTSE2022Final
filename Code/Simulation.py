import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os

# Setting up database of times with menu probabilities

food_prob = pd.DataFrame(columns = ['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'])
drinks_prob = pd.DataFrame(columns = ['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'])

timedelta = dt.timedelta(hours = 8)
incr = dt.timedelta(minutes = 1)

while timedelta < dt.timedelta(hours = 18):

    time = (dt.datetime.min + timedelta).time()
    hour = time.hour

    if hour < 11:
        food_i = pd.DataFrame([[0, 0, 0, 0, 1]],
                              columns = ['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'],index=[time])
        food_prob = pd.concat([food_prob, food_i])

        drinks_i = pd.DataFrame([[1 / 3, 2 / 15, 2 / 15, 2 / 15, 2 / 15, 2 / 15]],
                                columns=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[time])
        drinks_prob = pd.concat([drinks_prob, drinks_i])

    elif (hour >= 11) & (hour < 13):
        food_i = pd.DataFrame([[1/8, 1/8, 1/8, 5/8, 0]],
                              columns=['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index=[time])
        food_prob = pd.concat([food_prob, food_i])

        drinks_i = pd.DataFrame([[1/12, 1/12, 1/12, 7/12, 1/12, 1/12]],
                                columns=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[time])
        drinks_prob = pd.concat([drinks_prob, drinks_i])

    else:
        food_i = pd.DataFrame([[4/30, 4/30, 4/30, 0, 3/5]],
                              columns=['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index=[time])
        food_prob = pd.concat([food_prob, food_i])

        drinks_i = pd.DataFrame([[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]],
                                columns=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[time])
        drinks_prob = pd.concat([drinks_prob, drinks_i])

    print(timedelta)
    timedelta = timedelta + incr

# CSV's to check
food_prob.to_csv('Results/Food_Prob.csv')
drinks_prob.to_csv('Results/Drinks_Prob.csv')