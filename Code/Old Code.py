
# #################################
# NOTES
# #################################

# This file can be ignored. We wrote some code that we ended up not using, but wished to have on hand in case.
# One example was a table of individual minutes with the probabilities of different food and drinks. This would have
# made our model more flexible (i.e. not relying on 3 distinct time windows).
# However, it was an unnecessary complication.

# drinks_prob.index = times_idx
#
# food_prob = pd.DataFrame(columns = ['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'])
# drinks_prob = pd.DataFrame(columns = ['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'])
#
# timedelta = dt.timedelta(hours = 8)
# incr = dt.timedelta(minutes = 1)
#
#
# while timedelta < dt.timedelta(hours = 18):
#
#     time = (dt.datetime.min + timedelta).time()
#     hour = time.hour
#
#     if hour < 11:
#         food_i = pd.DataFrame([[0, 0, 0, 0, 1]],
#                               columns = ['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index = [time])
#         food_prob = pd.concat([food_prob, food_i])
#
#         drinks_i = pd.DataFrame([[1/3, 2/15, 2/15, 2/15, 2/15, 2/15]],
#                                 columns=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index = [time])
#         drinks_prob = pd.concat([drinks_prob, drinks_i])
#
#     elif (hour >= 11) & (hour < 13):
#         food_i = pd.DataFrame([[1/8, 1/8, 1/8, 5/8, 0]],
#                               columns=['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index = [time])
#         food_prob = pd.concat([food_prob, food_i])
#
#         drinks_i = pd.DataFrame([[1/12, 1/12, 1/12, 7/12, 1/12, 1/12]],
#                                 columns=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[time])
#         drinks_prob = pd.concat([drinks_prob, drinks_i])
#
#     else:
#         food_i = pd.DataFrame([[4/30, 4/30, 4/30, 0, 3/5]],
#                               columns=['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'], index = [time])
#         food_prob = pd.concat([food_prob, food_i])
#
#         drinks_i = pd.DataFrame([[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]],
#                                 columns=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'], index=[time])
#         drinks_prob = pd.concat([drinks_prob, drinks_i])
#
#     print(timedelta)
#     timedelta = timedelta + incr
#
# # CSVs to check
# food_prob.to_csv('Results/Food_Prob.csv')
# drinks_prob.to_csv('Results/Drinks_Prob.csv')
#
#
# # Adapting indexes to easy access later on
# times_idx = pd.period_range("2000-01-01 8:00", freq="T", periods = 600)
# food_prob.index = times_idx
#
#
#
# # allows us to easily select specific rows
# # for example, for food
#
# test_time = dt.time(hour=16, minute=14)
#
# row_ind = ((food_prob.index.minute == test_time.minute) & (food_prob.index.hour == test_time.hour))
# probs_row = food_prob[row_ind]
#
# options = list(probs_row.columns)
# probs = probs_row.values.tolist()[0]
#
# food = np.random.choice(options, 1, p = probs)
# print(food)
#
# # Prices menus
#
# food_menu = pd.DataFrame( [2, 3, 3, 2, 0], columns = ['Price'], index=['Cookie', 'Muffin', 'Pie', 'Sandwich', 'None'])
# drinks_menu = pd.DataFrame( [3, 4, 5, 3, 3, 2],
# columns = ['Price'], index=['Coffee', 'Frappucino', 'Milkshake', 'Soda', 'Tea', 'Water'])
#
#
#
