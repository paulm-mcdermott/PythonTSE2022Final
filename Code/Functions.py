from Classes.Store import Store
from Classes.Customer import Customer
import pandas as pd


def minute_of_business(date_time, store):
    hour = get_hour(date_time)
    customer = store.customer_entry()
    if customer is None:
        return
    else:
        # pick food and drink
        food_choice = store.pick_food(hour)
        drink_choice = store.pick_drink(hour)

        # determine prices and total cost of transaction for customer
        food_price = store.food_menu.loc[store.food_menu['food_item'] == food_choice, "price"]
        drink_price = store.drink_menu.loc[store.drink_menu['drink_item'] == drink_choice, "price"]
        tip = customer.determine_tip()
        total_cost = food_price + drink_price + tip

        # update customer's budget
        customer.update_budget(total_cost)

        # format store ledger entry
        transaction = [date_time, customer.customer_id, food_choice, drink_choice, total_cost, tip]

        # add transaction to store ledger
        store.add_to_ledger(transaction)

        # if customer's updated budget is insufficient, then remove from store ledger
        # don't have to worry about customer type due to size of budget for one time customers
        store.check_returning_viability(customer.customer_id)


def day_of_business(date, store):
    times_idx = pd.period_range(date + " 8:00", freq="T", periods=600)
    for i in times_idx:
        minute_of_business(i, store)


def get_hour(time):
    return int(time[0:2])
