# store needs a ledger for part 3, so
# transactions need to be in store, then store will
# have items (in the same way customers have budget)

class Store(object):
    def __init__(self, food_items, drink_items):
        # TODO: specify type dictionary
        self.food_items = food_items
        self.drink_items = drink_items

    # check budget, narrow options, choose selection, subtract from budget, check if tip
    # def transaction(self):
