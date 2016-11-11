import numpy as np

c ,v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)

vwap = np.average(c, weights = v)

t = np.arange(len(c))
# print "twap = ", np.average(c, weights=t)

h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)

# print "highest = ", np.max(h)
# print "lowest = ", np.min(l)

print "Spread high price", np.ptp(h)
print "Spread low price" , np.ptp(l)
