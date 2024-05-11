import numpy as np


def function(vals, consecutive_pairs):

    high = consecutive_pairs[-1]
    low = consecutive_pairs[0]
    cnt = 0

    while low[1] <= high[0]:

        cnt += 1
        mid = int((low[1] + high[0]) / 2)

        if low[1] == high[0] or low[1] + 1 == high[0]:

            return consecutive_pairs[mid], cnt

        elif np.floor(vals[consecutive_pairs[mid-1][1]] + vals[consecutive_pairs[mid-1][0]]) == 1:

            high = consecutive_pairs[mid - 1]

        elif np.floor(vals[consecutive_pairs[mid-1][1]] + vals[consecutive_pairs[mid-1][0]]) == 0:

            low = consecutive_pairs[mid]

    return (0, 0), 0


epsilon = 1e-10

size = 100

# create random valures inclusively between epsilon and 1, then sort them

vals = np.sort(np.random.uniform(epsilon, 1, size=(size,)), axis=0)

# from this point onward the only information we recieve about the values in the vals array is from the np.floor evaluations

indices = np.arange(size).astype(int)
pairs = np.column_stack((indices[:-1], indices[1:]))
consecutive_pairs = pairs[np.diff(pairs, axis=1).flatten() == 1]

# call binary search algorithm on consecutive pairs of indices and accompanying values that we have no evaluated yet besides in sort

mid, cnt = function(vals, consecutive_pairs)

print(vals)

print(np.array(
    [(np.floor(vals[x[0]] + vals[x[1]]), tuple(x)) for x in consecutive_pairs]))

print(mid)

# number of evaluations at search time, also binary search in total runs in O(logn) time
print(cnt)
