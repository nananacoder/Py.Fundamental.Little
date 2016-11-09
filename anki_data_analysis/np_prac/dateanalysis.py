import numpy as np
from datetime import datetime

def datestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()

dates, open, high, low, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), converters={1: datestr2num}, unpack=True)
print "Date:", dates
# print "Date = ", dates
# averages = np.zeros(5)

# for i in range(5):
#     indices = np.where(dates == i)
#
#     prices = np.take(close, indices)
#     avg = np.mean(prices)
#     print "Day", i, "prices", prices, "Average", avg
#     averages[i] = avg
#
# top = np.max(averages)
# print "Highest average", top
# print "Top day of the week", np.argmax(averages)
# bottom = np.min(averages)
# print "Lowest average", bottom
# print "Bottom day of the week", np.argmin(averages)

close = close[:16]
dates = dates[:16]


first_monday = np.ravel(np.where(dates == 0))[0]
#print "The first Monday index is", first_monday
last_friday = np.ravel(np.where(dates == 4))[-1]
#print "The last Friday index is", last_friday

weeks_indics = np.arange(first_monday, last_friday+1)
print weeks_indics
weeks_indics = np.split(weeks_indics, 3)
print "Weeks indices after split", weeks_indics

def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]

    return("APPL", monday_open, week_high, week_low, friday_close)

weeksummary = np.apply_along_axis(summarize, 1, weeks_indics, open, high, low, close)
print "Week summary", weeksummary

np.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")

