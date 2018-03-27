
# x1 is weather type (0 = partly cloudy, 1 = cloudy, 2 = sunny)
# x2 is atmospheric pressure (0 = low, 1 = high)


import numpy as np
x1 = [0, 1, 1, 2, 2, 2]
x2 = [0, 0, 1, 1, 1, 0]
y = np.array([0, 0, 0, 1, 1, 0])

def entropy(s):
    res = 0
    val, counts = np.unique(s, return_counts = True)
    print (counts)
    freqs = counts.astype('float')/len(s)
    for p in freqs:
        if p != 0.0:
            res -= p*np.log2(p)
    return res

def information_gain(y, x):
    res = entropy(y)
    val, counts = np.unique(x, return_counts = True)
    freqs = counts.astype('float')/len(s)
    for p, v in zip(freqs, val):
        res -= p*entropy(y[x == v])
    return res
































