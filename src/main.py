import pandas as pd
import datetime as dt
from pprint import pprint

# set display preferences to max
pd.set_option('display.max_columns', None, 'display.max_rows', None)

# read csv and remove empty columns and extra whitespace
data = pd.read_csv("../csvs/AutoSleep.csv")
data.columns = data.columns.str.strip()

# make working datafram with start/end times
data2 = data[['In bed at', 'Until']]

# split dates from times
dataAsleep = data2['In bed at'].apply(lambda x: pd.Series(x.split()))
dataAwake = data2['Until'].apply(lambda x: pd.Series(x.split()))

# merge pertinent data
sleeps = pd.concat([dataAsleep[1], dataAwake[1]], axis=1, keys=['Asleep', 'Awake'])

# convert to list 
sleeps = sleeps.values.tolist()

# binning logic int(x/24*48)




# debug views
print(data2.head())
print('\n DataAsleep:')
print(dataAsleep.head())
print('\nDataAwake:')
print(dataAwake.head())
print('\nSleeps:')
pprint(sleeps[0:4])