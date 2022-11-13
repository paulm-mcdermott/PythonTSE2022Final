import random

import pandas as pd


# #################################
# NOTES
# #################################

# This files introduces the classes for the different types of customers, defines the initialization, and adds the
# necessary methods to manage purchase history and determine tip. Of importance, customer type determines budget.

class Customer(object):
    def __init__(self, customer_id, budget):
        self.customer_id = customer_id
        self.budget = budget
        self.purchase_history = []

    # updates a customer's budget
    # since we're automatically removing those with insufficient budget we don't have to worry about checking budget
    def update_budget(self, transaction_cost):
        self.budget = self.budget - transaction_cost

    # determines tip
    def determine_tip(self):
        tip = 0
        if isinstance(self, TripAdvisorCustomer):
            tip = random.randint(1, 10)
        return float(tip)

    # adds to purchase history upon transaction
    def add_to_history(self, transaction):
        self.purchase_history.append(transaction)

    # retrieves this customer's purchase history as a dataframe
    def retrieve_purchase_history(self):
        return pd.DataFrame.from_records(self.purchase_history,
                                         columns=['date_time', 'customer_id', 'food_choice', 'drink_choice',
                                                  'transaction_value', 'tip'])


class OneTimeCustomer(Customer):
    def __init__(self, customer_id):
        super().__init__(customer_id, 100)


class TripAdvisorCustomer(OneTimeCustomer):
    def __init__(self, customer_id):
        super().__init__(customer_id)


class ReturningCustomer(Customer):
    def __init__(self, customer_id):
        super().__init__(customer_id, 250)


class HipsterCustomer(ReturningCustomer):
    def __init__(self, customer_id, budget=None):
        super().__init__(customer_id)
        self.budget = budget if budget is not None else 500
