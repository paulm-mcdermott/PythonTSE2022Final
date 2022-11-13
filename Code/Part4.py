from Simulation import coffee_shop, date_list_2, food_menu, drinks_menu
from Classes.Customer import *
from Classes.Store import *
from Exploratory import *
from Functions import *
import random
import pandas as pd
import matplotlib.pyplot as plt

####################################
# Part 4:
####################################

#############################################################
# Pt4 Q1 Show some histories of returning customers

# pick three random returning customers
sample_returning = random.choices(coffee_shop.viable_ret_cust, k=3)

# print out the histories of the random returning customers
for i in sample_returning:
    print(i.retrieve_purchase_history())

##############################################################
# Part Q2 More analysis of Coffeebar_2016-2020.csv

# We get the number of appearances of each ID
ret_customers = coffeebar_df['CUSTOMER'].value_counts()

# Keep only returning customers, there are 1000 of them
ret_customers = ret_customers[ret_customers > 1]
print(len(ret_customers))

# Now, we add this info to the transaction log
coffeebar_df_ret = coffeebar_df
coffeebar_df_ret['VISITS'] = coffeebar_df.groupby('CUSTOMER')['CUSTOMER'].transform('count')
coffeebar_df_ret['RETURNING'] = coffeebar_df_ret['VISITS'] > 1

# We determine the makeup of the customers at any given time with a graph as above.
ct_time_ret = pd.crosstab(coffeebar_df_ret['TIMESTAMP'], coffeebar_df_ret['RETURNING'], normalize='index') * 100

ct_time_ret.plot(kind="bar", stacked=True, rot=0)

x_ticks = [0, 12, 24, 36, 66, 96, 111, 126, 141, 156, 171]
x_labels = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.ylabel('Proportion of Returning Customers')
plt.xlabel('Time')
plt.title('Distribution of Customer Types over Time')
plt.legend(['One-Time', 'Returning'], title='Customer Type', loc='lower right')
plt.gcf().set_size_inches(9, 6)
plt.savefig(directory + '/Results/Part 4/ReturningDist.png', dpi=300)

# We see returning customers make up:
# 20% of customers in the morning
# 10% of customers around midday
# 30% of customers in the afternoon
# Hence, they show up more in off-peak hours, mornings and afternoons.

# Next, let's look at purchase probabilities for the two groups at different times.
# We just take a single minute in the intervals as distributions are uniform within periods. This is for simplicity

coffeebar_df_ret_morning = coffeebar_df_ret[coffeebar_df_ret['TIMESTAMP'] == dt.time(hour=8)]
coffeebar_df_ret_midday = coffeebar_df_ret[coffeebar_df_ret['TIMESTAMP'] == dt.time(hour=12)]
coffeebar_df_ret_afternoon = coffeebar_df_ret[coffeebar_df_ret['TIMESTAMP'] == dt.time(hour=14)]

# Food
ct_food_ret_morning = pd.crosstab(coffeebar_df_ret_morning['RETURNING'], coffeebar_df_ret_morning['FOOD'],
                                  normalize='index') * 100
ct_food_ret_midday = pd.crosstab(coffeebar_df_ret_midday['RETURNING'], coffeebar_df_ret_midday['FOOD'],
                                 normalize='index') * 100
ct_food_ret_afternoon = pd.crosstab(coffeebar_df_ret_afternoon['RETURNING'], coffeebar_df_ret_afternoon['FOOD'],
                                    normalize='index') * 100

print(ct_food_ret_morning)
# No difference, no food purchased
print(ct_food_ret_midday)
# Returning customers more likely to buy a sandwich, less likely to buy a muffin or pie
print(ct_food_ret_afternoon)
# Returning customers less likely to buy nothing, more likely to have a cookie, muffin or pie

# Drinks
ct_drinks_ret_morning = pd.crosstab(coffeebar_df_ret_morning['RETURNING'], coffeebar_df_ret_morning['DRINKS'],
                                    normalize='index') * 100
ct_drinks_ret_midday = pd.crosstab(coffeebar_df_ret_midday['RETURNING'], coffeebar_df_ret_midday['DRINKS'],
                                   normalize='index') * 100
ct_drinks_ret_afternoon = pd.crosstab(coffeebar_df_ret_afternoon['RETURNING'], coffeebar_df_ret_afternoon['DRINKS'],
                                      normalize='index') * 100

print(ct_drinks_ret_morning)
# Returning customers only drink coffee in the mornings! No other drinks
print(ct_drinks_ret_midday)
# Returning customers more likely to have water or a soda or coffee (marginally),
# less likely to have a frappucino, milkshake or tea
print(ct_drinks_ret_afternoon)
# Returning customers similar but more likely to have soda or frappucino. Similar patterns

# On the whole, patterns are very similar except for the morning drink choices where returning customers
# only drink coffee as opposed to one-time customers who have a range of drinks in the morning. On the whole,
# highly correlated preferences.

#############################################################
# Pt 4 Q3 Lower returning to 50 customers, then run same simulation

# make the new viable returning customer list
hipster_list_p4 = [HipsterCustomer("H" + str(i)) for i in range(1, 20)]
returning_list_p4 = [ReturningCustomer("R" + str(i)) for i in range(20, 51)]
all_returning_list_p4 = returning_list_p4 + hipster_list_p4
coffee_shop_p4 = Store(food_menu, drinks_menu, all_returning_list_p4)

# for each day, run day of business function.
for i in date_list_2:
    day_of_business(i, coffee_shop_p4)
df_ledger_p4 = coffee_shop_p4.retrieve_ledger()
print(df_ledger_p4)

# see all the regular returning customer transactions, of interest: when the last returning customer arrived (one
# simulation: 14/04/2016, of course this will change in another simulation)
print(df_ledger_p4[df_ledger_p4['customer_id'].str.contains('R')])

# see all the hipster returning customer transactions, of interest: when the last hipster arrived (one simulation:
# 10/05/2016, about a month after the last regular returning customer, which makes sense due to higher budget)
print(df_ledger_p4[df_ledger_p4['customer_id'].str.contains('H')])

#############################################################
# Pt 4 Q4 The prices change from the beginning of 2018 and go up by 20%

# make two time lists instead of just one
date_list_pt4q4_1 = pd.date_range(start="2016-01-01", end="2017-12-31")
date_list_pt4q4_2 = pd.date_range(start="2018-01-01", end="2020-12-31")

# convert datetime objects to date objects
dates_pt4q4_1 = list(map(datetime_to_date, date_list_pt4q4_1))
dates_pt4q4_2 = list(map(datetime_to_date, date_list_pt4q4_2))

# create hipster and returning customers
hipster_list_pt4q4 = [HipsterCustomer("H" + str(i)) for i in range(1, 334)]
returning_list_pt4q4 = [ReturningCustomer("R" + str(i)) for i in range(334, 1001)]
all_returning_list_pt4q4 = returning_list_pt4q4 + hipster_list_pt4q4

# instantiate store
coffee_shop_pt4q4 = Store(food_menu, drinks_menu, all_returning_list_pt4q4)

# run 2016, 2017 simulation
for i in dates_pt4q4_1:
    day_of_business(i, coffee_shop_pt4q4)

# update menus
new_food_prices = coffee_shop_pt4q4.food_menu['price'] * 1.2
coffee_shop_pt4q4.food_menu['price'] = new_food_prices

new_drink_prices = coffee_shop_pt4q4.drink_menu['price'] * 1.2
coffee_shop_pt4q4.drink_menu['price'] = new_drink_prices

# run 2018, 2019, 2020 simulation
for i in dates_pt4q4_2:
    day_of_business(i, coffee_shop_pt4q4)

# retrieve and print ledger, notice that some transactions now have decimals
df_ledger_pt4q4 = coffee_shop_pt4q4.retrieve_ledger()
print(df_ledger_pt4q4)

# we would expect more returning customers to be removed from the list than the baseline simulation case due to higher
# average prices. Indeed, our test results in 367 remaining, compared to baseline test of 672
print(len(coffee_shop_pt4q4.viable_ret_cust))

#############################################################
# Pt 4 Q5 Hipster budget reduces to 40

# new list of 1000 viable customers, this time with all hipsters having a budget of 40
hipster_list_pt4q5 = [HipsterCustomer("H" + str(i), budget=40) for i in range(1, 334)]
returning_list_pt4q5 = [ReturningCustomer("R" + str(i)) for i in range(334, 1001)]
all_returning_list_pt4q5 = returning_list_pt4q5 + hipster_list_pt4q5

# instantiate a store
coffee_shop_pt4q5 = Store(food_menu, drinks_menu, all_returning_list_pt4q5)

# run simulation, same as before
for i in date_list_2:
    day_of_business(i, coffee_shop_pt4q5)

# retrieve and print ledger
df_ledger_pt4q5 = coffee_shop_pt4q5.retrieve_ledger()
print(df_ledger_pt4q5)

# we suspect that the last date a hipster customer will visit the store will be much earlier than in
# the original case. A test simulation: last hipster on 11/05/2017. There will be variance across tests.
print(df_ledger_pt4q5[df_ledger_pt4q5['customer_id'].str.contains('H')])

#############################################################
# Pt 4 Q6 Build your own TODO pt 4 q6
# Randomize the budgets of returning and hipster

# new list of 1000 viable customers, using random integers for the budgets
hipster_list_pt4q6 = [HipsterCustomer("H" + str(i), budget=random.randint(100, 500)) for i in range(1, 334)]
returning_list_pt4q6 = [ReturningCustomer("R" + str(i), budget=random.randint(100, 250)) for i in range(334, 1001)]
all_returning_list_pt4q6 = returning_list_pt4q6 + hipster_list_pt4q6
