import pandas as pd

# set display preferences to max
pd.set_option('display.max_columns', None, 'display.max_rows', None)

# read csv and remove empty columns and extra whitespace
df = pd.read_csv("../csvs/AutoSleep.csv")
df.drop(['Fell asleep in', 'Tags', 'Notes'], axis=1, inplace=True)
df.columns = df.columns.str.strip()

# debug info
print(list(df.columns))
print(df)

# convert datatypes to datetime and timedelta
# df["In bed at"] = pd.to_datetime(df["In bed at"])
df[['In bed at', 'Until']] = df[['In bed at', 'Until']].apply(pd.to_datetime)

# Debug output
print('\n' + "DataTypes:")
print(df.dtypes)
