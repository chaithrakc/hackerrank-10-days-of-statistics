import math
from collections import Counter


# central measures/central tendency of the data - mean, median, and mode

def mean(sample: list) -> float:
    return sum(sample) / len(sample)


def median(sample: list) -> float:
    size = len(sample)
    mid_index = size // 2
    # sample with odd length
    if size % 2:
        return sorted(sample)[mid_index]

    # sample with even length
    return sum(sorted(sample)[mid_index - 1: mid_index + 1]) / 2


def mode(sample: list) -> int:
    ctr = Counter(sample)
    max_freq = ctr.most_common(1)[0][1]
    max_freq_num = [key for key, val in ctr.items() if val == max_freq]
    # if multiple values have max freq, selecting the smallest one
    return sorted(max_freq_num)[0]


if __name__ == '__main__':
    # reading input from stdin
    # size = int(input())
    # data = list(map(int, input().split()))

    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    average = mean(data)
    median_val = median(data)
    mode_val = mode(data)

    print('%.1f' % average)
    print('%.1f' % median_val)
    print(mode_val)
