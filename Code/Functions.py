from Classes.Store import Store
from Classes.Customer import Customer


def minute_of_business(time, store):
    hour = get_hour(time)
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
        transaction = [customer.customer_id, food_choice, drink_choice, tip, total_cost]

        # add transaction to store ledger
        store.add_to_ledger(transaction)

        # if customer's updated budget is insufficient, then remove from store ledger
        # don't have to worry about customer type due to size of budget for one time customers
        store.check_returning_viability(customer.customer_id)


def get_hour(time):
    return int(time[0:2])
