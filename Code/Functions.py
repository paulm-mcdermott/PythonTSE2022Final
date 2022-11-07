from Classes.Store import Store
from Classes.Customer import Customer
import pandas as pd
import datetime as dt

# #################################
# NOTES
# #################################

# Using the established class structure, this file defines the workhorse functions for our simulation.
# The premise of this is minute of business which takes in a time and a store object, and then simulates
# what occurs in that minute. So, the type of customer, what is ordered and if there is a tip. It then adds
# to a customer and store ledger and checks the budget of returning customers so that, if necessary, those
# with insufficient funds are removed from the client list
#
# Additionally, we have a day of business function (using the minute base) and two other functions used elsewhere


def minute_of_business(date_time, store):
    hour = date_time.hour
    customer = store.customer_entry()
    if customer is None:
        return
    else:
        # pick food and drink
        food_choice = store.pick_food(hour)
        drink_choice = store.pick_drink(hour)

        # determine prices and total cost of transaction for customer
        food_price = int(store.food_menu.loc[store.food_menu['food_item'] == food_choice, "price"])
        drink_price = int(store.drink_menu.loc[store.drink_menu['drink_item'] == drink_choice, "price"])

        tip = customer.determine_tip()
        total_cost = food_price + drink_price + tip

        # update customer's budget
        customer.update_budget(total_cost)

        # format store ledger entry
        transaction = [date_time.strftime('%d/%m/%Y, %H:%M:%S'), customer.customer_id, food_choice, drink_choice,
                       total_cost, tip]

        # add transaction to store ledger
        store.add_to_ledger(transaction)
        customer.add_to_history(transaction)

        # if customer's updated budget is insufficient, then remove from store ledger
        # don't have to worry about customer type due to size of budget for one time customers
        store.check_returning_viability(customer)


# Use minute of business to simulate a day of business. We input a single date and then minutes from 8h00 to 18h00 are
# run through the simulation
def day_of_business(date, store):
    times_idx = pd.period_range(pd.Timestamp.combine(date=date, time=dt.time(hour=8)), freq="T", periods=600)
    for i in times_idx:
        minute_of_business(i, store)


# Function to convert datetime objects to just the date, used for data analysis and the simulation
def datetime_to_date(i):
    return i.date()


