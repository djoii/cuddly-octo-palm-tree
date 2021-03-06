import csv
import itertools
import matplotlib.pyplot as plt


def csv2list(f):
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
    samples = len(data)
    return samples, data


with open('../csvs/AutoSleep.csv') as f:
    samples, data = csv2list(f)


def declutter(r):
    short_row = list(itertools.islice(r, 2))
    split_row = [x.split() for x in short_row]
    return [split_row[0][1], split_row[1][1]]


sleeps = [declutter(row) for row in data]


def psudotime(t):
    hour, minute, second = t.split(':')
    return int(
        (int(hour) * 3600 + int(minute) * 60 + int(second)) / 86400 * 48)


fractional_sleeps = [[psudotime(time) for time in sleep] for sleep in sleeps]


def binning(dt):
    if dt[0] > dt[1]:
        dt[1] = dt[1] + 48
    return [x % 48 for x in range(dt[0], dt[1] + 1)]


bins_list = [
    binning(fractional_sleep) for fractional_sleep in fractional_sleeps
]

bins = list(itertools.chain(*bins_list))
counts = [sum(x == i for x in bins) for i in range(48)]

norm_counts = list([x / samples for x in counts])
fig1, bar1 = plt.subplots()
bar1.bar(list(range(0, 48)), norm_counts)
plt.show()
fig1.savefig('../figs/SleepDistribution.png', dpi='figure')

