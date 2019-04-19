import pandas as pd

# set display preferences to max
pd.set_option('display.max_columns', None, 'display.max_rows', None)

# read csv and remove empty columns and extra whitespace
data = pd.read_csv("../csvs/AutoSleep.csv")
data.columns = data.columns.str.strip()

# make working datafram with start/end times
data2 = data[['In bed at', 'Until']]
print(data2.head())

# split dates from times
dataAwake = data2['In bed at'].apply(lambda x: pd.Series(x.split()))
print(dataAwake.head())
