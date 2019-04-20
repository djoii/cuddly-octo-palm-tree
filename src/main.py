import pandas as pd
from datetime import datetime as dt
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

# psudo time conversion
for s, sleep in enumerate(sleeps):
    for t, time in enumerate(sleep):
        hour, minute, second = time.split(':')
        fraction_of_day = (int(hour)*3600 + int(minute)*60 + int(second))/86400 * 48
        sleeps[s][t] = int(fraction_of_day)

# binning logic int(x/24*48)
def chunk(sleep):
    begin, end = sleep
    chunks_asleep = list(range(begin, end+1))
    print(chunks_asleep)
    slots = list(map(lambda x: int(x/24*48), chunks_asleep))
    return slots

# historam counts
hist = [0]*48
for sleep in sleeps:
    for slot in chunk(sleep):
        # hist[slot] += 1
        sleep

# # debug views
# print(data2.head())
# print('\n DataAsleep:')
# print(dataAsleep.head())
# print('\nDataAwake:')
# print(dataAwake.head())
# print('\nSleeps:')
# pprint(sleeps[0:4])
# print('\nHist:')
# print(hist)