from Customer import OneTimeCustomer, TripAdvisorCustomer
import random
import numpy as np
import pandas as pd
from Customer import Customer, OneTimeCustomer, TripAdvisorCustomer


# store needs a ledger for part 3, so
# transactions need to be in store, then store will
# have items (in the same way customers have budget)

class Store(object):
    def __init__(self, food_menu, drink_menu, ret_cust_list):
        # TODO: specify types (menus should be dataframes), ret_cust_list is list of ids
        self.food_menu = food_menu
        self.drink_menu = drink_menu
        self.viable_ret_cust = ret_cust_list
        self.ledger = []

    def add_to_ledger(self, transaction):
        self.ledger.append(transaction)

    def retrieve_ledger(self):
        return pd.DataFrame.from_records(self.ledger,columns=['date_time','customer_id','food_choice','drink_choice','transaction_value','tip'])

    def remove_returning_customer(self, customer_id):
        self.viable_ret_cust.remove(customer_id)

    # takes in returning customer object, observes if that customer can afford to buy both the
    # most expensive drink item AND the most expensive food item on the menu in one transaction
    # if not, this customer is removed from the viable returning customer list
    def check_returning_viability(self, returning_customer):
        if returning_customer.budget() < self.food_menu["price"].max() + self.drink_menu["price"].max():
            self.remove_returning_customer(returning_customer.customer_id)
        else:
            return

    # happens every minute of store open, first determines IF a customer will enter
    # then what type. Returns the corresponding customer object, or nothing in no entry
    def customer_entry(self):
        minute_draw = random.uniform(0, 1)
        p_cust = 0.7
        if minute_draw < p_cust:
            return self.pick_customer_type()
        else:
            return

    # if customer_entry determines that a customer will indeed enter, picks which type
    # and returns that corresponding customer object
    def pick_customer_type(self):
        p_returning = 0.2
        type_cust = random.uniform(0, 1)
        if type_cust < p_returning:
            return self.pick_returning_customer()
        else:
            p_ta_customer = 0.1
            p_walk_in_type = random.uniform(0, 1)
            if p_walk_in_type <= p_ta_customer:
                wi_customer = TripAdvisorCustomer()
            else:
                wi_customer = OneTimeCustomer()
            return wi_customer

    # randomly picks from the pool of viable returning customers
    def pick_returning_customer(self):
        random.choice(self.viable_ret_cust)

    # picks a food item based on the hour of day, according to probabilities in food_menu
    def pick_food(self, hour):
        if hour < 11:
            np.random.choice(self.food_menu["food_item"], 1, self.food_menu["breakfast_prob"])
        elif (hour >= 11) & (hour < 13):
            np.random.choice(self.food_menu["food_item"], 1, self.food_menu["lunch_prob"])
        else:
            np.random.choice(self.food_menu["food_item"], 1, self.food_menu["dinner_prob"])

    def pick_drink(self, hour):
        if hour < 11:
            np.random.choice(self.food_menu["food_item"], 1, self.food_menu["breakfast_prob"])
        elif (hour >= 11) & (hour < 13):
            np.random.choice(self.food_menu["food_item"], 1, self.food_menu["lunch_prob"])
        else:
            np.random.choice(self.food_menu["food_item"], 1, self.food_menu["dinner_prob"])


