from typing import List

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os
import random
import time

import Functions
from Classes.Customer import HipsterCustomer, ReturningCustomer
from Classes.Store import Store
from Functions import *


os.path.abspath('.')
directory = '/Users/justinstandish-white/PycharmProjects/exam-mcdermott-standish-white'

df_ledger = pd.read_csv(directory + '/Results/SimulationLedger.csv', sep=',')



####### Data ANALYSIS

print(df_ledger.head(7))


df_ledger['DATETIME'] = pd.to_datetime(df_ledger['date_time'])

df_ledger['TIMESTAMP'] = df_ledger['DATETIME'].dt.time
df_ledger['DATE'] = df_ledger['DATETIME'].dt.date

print('done')




