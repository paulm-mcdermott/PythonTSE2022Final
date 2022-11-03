import Simulation
import random

sample_returning = random.choices(Simulation.coffee_shop.viable_ret_cust,k=3)
print(type(sample_returning[0]))
sample_returning[0].retrieve_purchase_history()
for i in sample_returning:
    print(i.retrieve_purchase_history())