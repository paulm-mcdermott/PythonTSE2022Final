import random


class Customer(object):
    def __init__(self, customer_id, budget):
        self.customer_id = customer_id
        self.budget = budget

    # this needs to check budget and block if needed
    # return false if can't, return tip if can (tip can be 0)
    # since we're automatically removing those with insufficient budget
    # we don't have to worry about checking budget
    def update_budget(self, transaction_cost):
        self.budget = self.budget - transaction_cost

    def determine_tip(self):
        tip = 0
        if isinstance(self, TripAdvisorCustomer):
            tip = random.randint(1, 10)
        return tip


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
    def __init__(self, customer_id):
        super().__init__(customer_id)
        self.budget = 500
