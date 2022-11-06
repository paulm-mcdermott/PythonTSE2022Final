import random
import numpy as np
import pandas as pd
from Classes.Customer import OneTimeCustomer, TripAdvisorCustomer

# #################################
# NOTES
# #################################

# This files introduces the store class that we create to make our simulation more efficient.
# Stores are initialised with the relevant menus, customer list and customer probabilities
# We set the probability of a customer entering the store in a given minute as 0.25
# this is based on the coffeebar data which had 171 customers over 600 minutes per day, so we round off to 0.25
#
# Most of the functionality is built into this store class. Including the system to pick type of customer,
# drink choices, budget checking and the maintaining of a ledger of transactions


class Store(object):

    # store constructor, note the fact that the probabilities have default that can be overrided
    def __init__(self, food_menu, drink_menu, ret_cust_list, prob_cust=.25, prob_returning=.2, prob_ta_customer=0.1):
        # TODO: specify types (menus should be dataframes), ret_cust_list is list of ids
        self.food_menu = food_menu
        self.drink_menu = drink_menu
        self.viable_ret_cust = ret_cust_list
        self.ledger = []
        self.walk_ins = []
        self.prob_cust = prob_cust
        self.prob_returning = prob_returning
        self.prob_ta_customer = prob_ta_customer

    # adds transaction, a parameter meant to be a list, onto the ledger
    def add_to_ledger(self, transaction):
        self.ledger.append(transaction)

    # retrieves ledger in dataframe form
    def retrieve_ledger(self):
        return pd.DataFrame.from_records(self.ledger,
                                         columns=['date_time', 'customer_id', 'food_choice', 'drink_choice',
                                                  'transaction_value', 'tip'])

    # removing from returning customer pool
    def remove_returning_customer(self, customer):
        self.viable_ret_cust.remove(customer)

    # takes in returning customer object, observes if that customer can afford to buy both the
    # most expensive drink item AND the most expensive food item on the menu in one transaction
    # if not, this customer is removed from the viable returning customer list
    def check_returning_viability(self, returning_customer):
        if returning_customer.budget < self.food_menu["price"].max() + self.drink_menu["price"].max():
            self.remove_returning_customer(returning_customer)
        else:
            return

    # happens every minute of store open, first determines IF a customer will enter
    # then what type. Returns the corresponding customer object, or nothing in no entry
    def customer_entry(self):
        minute_draw = random.uniform(0, 1)
        if minute_draw < self.prob_cust:
            return self.pick_customer_type()
        else:
            return None

    # if customer_entry determines that a customer will indeed enter, picks which type
    # and returns that corresponding customer object
    def pick_customer_type(self):
        if len(self.viable_ret_cust) == 0:
            type_cust = 1
        else:
            type_cust = random.uniform(0, 1)
        if type_cust < self.prob_returning:
            return self.pick_returning_customer()
        else:
            p_walk_in_type = random.uniform(0, 1)
            if p_walk_in_type <= self.prob_ta_customer:
                wi_customer = TripAdvisorCustomer("TA" + str(len(self.walk_ins) + 1))
            else:
                wi_customer = OneTimeCustomer("OT" + str(len(self.walk_ins) + 1))
            self.walk_ins.append(wi_customer)
            return wi_customer

    # randomly picks from the pool of viable returning customers
    def pick_returning_customer(self):
        return random.choice(self.viable_ret_cust)

    # picks a food item based on the hour of day, according to probabilities in food_menu
    def pick_food(self, hour):
        if hour < 11:
            return np.random.choice(list(self.food_menu["food_item"]), 1, p=list(self.food_menu["breakfast_prob"]))[0]
        elif (hour >= 11) & (hour < 13):
            return np.random.choice(list(self.food_menu["food_item"]), 1, p=list(self.food_menu["lunch_prob"]))[0]
        else:
            return np.random.choice(list(self.food_menu["food_item"]), 1, p=list(self.food_menu["dinner_prob"]))[0]

    # picks a food item based on the hour of day, according to probabilities in drink_menu
    def pick_drink(self, hour):
        if hour < 11:
            return np.random.choice(list(self.drink_menu["drink_item"]), 1, p=list(self.drink_menu["breakfast_prob"]))[
                0]
        elif (hour >= 11) & (hour < 13):
            return np.random.choice(list(self.drink_menu["drink_item"]), 1, p=list(self.drink_menu["lunch_prob"]))[0]
        else:
            return np.random.choice(list(self.drink_menu["drink_item"]), 1, p=list(self.drink_menu["dinner_prob"]))[0]
