import unittest
import pandas as pd
from Classes.Store import Store
from Classes.Customer import *
from Functions import *


class store_tests(unittest.TestCase):
    returning_budget = 250
    hipster_budget = 500

    def test_returning_removal(self):
        food_menu = pd.DataFrame([['Cookie', self.returning_budget/2 - 1, 1, 1, 1]],
                                 columns=['food_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                                 )

        drink_menu = pd.DataFrame([['Coffee', self.returning_budget/2 - 1, 1, 1, 1]],
                                 columns=['drink_item', 'price', 'breakfast_prob', 'lunch_prob', 'dinner_prob'],
                                 )
        R1 = ReturningCustomer('R1')
        customer_list = [R1]
        store1 = Store(food_menu, drink_menu, customer_list,1,1,1)
        times_idx = pd.period_range("2000-01-01 8:00", freq="T", periods=600)
        minute_of_business(times_idx[0], store1)
        self.assertTrue(len(store1.viable_ret_cust) == 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
