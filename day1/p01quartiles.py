# Q2: find median for entire sample
# Q1: find median for first half of the sample
# Q3: find median for second half of the sample

"""

https://towardsdatascience.com/what-are-quartiles-c3e117114cf1

Quartiles are position indicators that divide a sequence of numbers into 4 equal parts.

Quartiles analysis is part of descriptive statistics and consequently, helps us better understand
the data at hand. With these, specifically, we will understand what is called central tendency or :

“A measure of central tendency is a single value that attempts to describe a set of data by identifying
the central position within that set of data”

1) Before doing any calculation of Quartiles we need to order the sequence from lowest to highest

"""

import numpy as np


def median(sample: list) -> float:
    size = len(sample)
    mid_index = size // 2
    # sample with odd length
    if size % 2:
        return sorted(sample)[mid_index]

    # sample with even length
    return sum(sorted(sample)[mid_index - 1: mid_index + 1]) / 2


def quartiles(sample: list) -> list:
    sample.sort()
    size = len(sample)
    mid_index = size // 2
    if size % 2:
        q3 = median(sample[mid_index + 1:])
    else:
        q3 = median(sample[mid_index:])
    return [median(sample[:mid_index]), median(sample), q3]


if __name__ == '__main__':
    data = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
    result = quartiles(data)
    print(result)

    # using numpy
    print('%d' % np.quantile(np.array(data), 0.25))
    print('%d' % np.quantile(np.array(data), 0.5))
    print('%d' % np.quantile(np.array(data), 0.75, interpolation='midpoint'))
