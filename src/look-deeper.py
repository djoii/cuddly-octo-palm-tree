import csv
import pprint

with open('../csvs/AutoSleep.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    data = [[x.strip() for x in inner] for inner in data]

print(data[0:4])