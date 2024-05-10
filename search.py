import numpy as np


def function(vals, consecutive_pairs):

    high = consecutive_pairs[-1]
    low = consecutive_pairs[0]
    cnt = 0

    while low[1] <= high[0]:

        cnt += 1
        mid = int((low[1] + high[0]) / 2)

        if low[1] == high[0] or low[1] + 1 == high[0]:

            return consecutive_pairs[mid-1], cnt

        elif np.floor(vals[consecutive_pairs[mid-1][1]] + vals[consecutive_pairs[mid-1][0]]) == 1:

            high = consecutive_pairs[mid - 1]

        elif np.floor(vals[consecutive_pairs[mid-1][1]] + vals[consecutive_pairs[mid-1][0]]) == 0:

            low = consecutive_pairs[mid]

    return (0, 0), 0


epsilon = 1e-10

size = 100

size = 100
vals = np.sort(np.random.uniform(epsilon, 1, size=(size,)), axis=0)
indices = np.arange(size).astype(int)

# touples = np.dstack((indices, vals)).astype(object)[0]


pairs = np.column_stack((indices[:-1], indices[1:]))

consecutive_pairs = pairs[np.diff(pairs, axis=1).flatten() == 1]

print(vals)

high = consecutive_pairs[-1]
low = consecutive_pairs[0]


mid, cnt = function(vals, consecutive_pairs)

print(np.array(
    [(np.floor(vals[x[0]] + vals[x[1]]), tuple(x)) for x in consecutive_pairs]))

print(mid)
print(cnt)
