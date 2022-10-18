class Customer(object):
    def __init__(self, customer_id, budget):
        self.customer_id = customer_id
        self.budget = budget

    # this needs to check budget and block if needed
    # return false if can't, return tip if can (tip can be 0)
    def add_transaction(self, cost):
        if self.budget < cost:
            return False
        # TODO: add rest of logic (else)


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
