import csv
import itertools
import matplotlib.pyplot as plt

with open('../csvs/AutoSleep.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
    samples = len(data)

sleeps = []
for row in data:
    new_row = list(itertools.islice(row, 2))
    new_row2 = [x.split() for x in new_row]
    # print(new_row2)
    sleep = [new_row2[0][1], new_row2[1][1]]
    sleeps.append(sleep)

fractional_sleeps = []
for sleep in sleeps:
    fractions_of_day = []
    for time in sleep:
        hour, minute, second = time.split(':')
        fraction_of_day = (int(hour)*3600 + int(minute)
                           * 60 + int(second))/86400*48
        fractions_of_day.append(int(fraction_of_day))
    fractional_sleeps.append(fractions_of_day)

bins_list = []
for fractional_sleep in fractional_sleeps:
    begin = min(fractional_sleep)
    end = max(fractional_sleep)
    bins = list(range(begin, end+1))
    bins_list.append(bins)

counts = [0]*48
for bins in bins_list:
    for bin in bins:
        counts[bin] += 1

norm_counts = list(map(lambda x: x/samples, counts))
plt.bar(list(range(0, 48)), norm_counts)
plt.show()
