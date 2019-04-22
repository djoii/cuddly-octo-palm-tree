import csv
import itertools
import matplotlib.pyplot as plt


def csv2list(f):
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
    samples = len(data)
    return samples, data


with open('AutoSleep.csv') as f:
    samples, data = csv2list(f)


def declutter(r, l):
    short_row = list(itertools.islice(r, 2))
    split_row = [x.split() for x in short_row]
    joind_row = [split_row[0][1], split_row[1][1]]
    l.append(joind_row)


sleeps = []
for row in data:
    declutter(row, sleeps)


def psudotime(t, l):
    hour, minute, second = t.split(':')
    fraction_of_day = (
        int(hour) * 3600 + int(minute) * 60 + int(second)) / 86400 * 48
    l.append(int(fraction_of_day))


fractional_sleeps = []
for sleep in sleeps:
    fractions_of_day = []
    for time in sleep:
        fraction_of_day = psudotime(time, fractions_of_day)
    fractional_sleeps.append(fractions_of_day)


def binning(dt, l):
    start = min(dt)
    end = max(dt)
    bins = list(range(start, end + 1))
    l.append(bins)


bins_list = []
for fractional_sleep in fractional_sleeps:
    binning(fractional_sleep, bins_list)

counts = [0] * 48
for bins in bins_list:
    for bin in bins:
        counts[bin] += 1

norm_counts = list(map(lambda x: x / samples, counts))
plt.bar(list(range(0, 48)), norm_counts)
plt.show()