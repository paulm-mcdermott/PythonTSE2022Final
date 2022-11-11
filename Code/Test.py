import unittest
import pandas as pd
from Classes.Store import Store
from Classes.Customer import *
from Functions import *

# experimenting with the test filetype built into PyCharm
class store_tests(unittest.TestCase):
    returning_budget = 250
    hipster_budget = 500

    # testing if the removal of returning customers from customer pool works
    def test_returning_removal(self):
        # defining menus for this test with one item each at probability one ensuring they will be bought
        food_menu = pd.DataFrame([['Cookie', self.returning_budget/2 - 1, 1, 1, 1]],
                                 columns=['food_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                                 )

        drink_menu = pd.DataFrame([['Coffee', self.returning_budget/2 - 1, 1, 1, 1]],
                                 columns=['drink_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                                 )

        # instantiate returning customer and store
        R1 = ReturningCustomer('R1')
        customer_list = [R1]

        # instantiate store with 100% probability of entry and 100% probability of returning customer
        store1 = Store(food_menu, drink_menu, customer_list, prob_cust=1, prob_returning=1, prob_ta_customer=1)

        # grab a single time from times_idx and run minute of business
        times_idx = pd.period_range("2000-01-01 8:00", freq="T", periods=600)
        minute_of_business(times_idx[0], store1)

        # since probability of customer entry and returning customer are 1, and menu prices as defined, then the viable
        # list should now be empty. if empty, removal was successful
        self.assertTrue(len(store1.viable_ret_cust) == 0)


if __name__ == '__main__':
    unittest.main()
