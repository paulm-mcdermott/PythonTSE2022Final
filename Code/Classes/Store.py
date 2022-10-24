
from Customer import ReturningCustomer, OneTimeCustomer, TripAdvisorCustomer, HipsterCustomer
import random


# store needs a ledger for part 3, so
# transactions need to be in store, then store will
# have items (in the same way customers have budget)

class Store(object):
    def __init__(self, food_menu, drink_menu, ret_cust_list):
        # TODO: specify type dictionary
        self.food_menu = food_menu
        self.drink_menu = drink_menu
        self.viable_ret_cust = ret_cust_list # I think this way will be extremely inefficient
        self.ledger = []

    def remove_customer(self,cust_id):
        self.viable_ret_cust.remove(cust_id)

    def add_to_ledger(self, transaction):
        self.ledger.append(transaction)

    # TODO: find a way to pull out all of these probabilities
    # Note: maybe this should actually be a function outside of Class
    def minute_of_business(self, cust_list):
        minute_draw = random.uniform(0, 1)
        p_cust = 0.7
        if minute_draw < p_cust:
            p_returning = 0.2
            type_cust = random.uniform(0, 1)
            if type_cust < p_returning:
                r_customer = random.choice(cust_list)
                # r_customer.do_transaction() TODO: Implement in customer class
            else:
                p_ta_customer = 0.1
                p_wi_type = random.uniform(0, 1)
                if p_wi_type <= p_ta_customer:
                    wi_customer = TripAdvisorCustomer()
                else:
                    wi_customer = OneTimeCustomer()
        else:
            return

    # check budget, narrow options, choose selection, subtract from budget, check if tip
    # def transaction(self):
