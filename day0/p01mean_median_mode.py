import math
from collections import Counter


def mean(nums: list) -> float:
    return sum(nums) / len(nums)


def median(nums: list) -> float:
    size = len(nums)
    nums_copy = nums.copy()
    nums_copy.sort()
    # even length
    if size % 2 == 0:
        median_index = size // 2
        return (nums_copy[median_index - 1] + nums_copy[median_index]) / 2
    # odd length
    median_index = math.ceil(size / 2)
    return nums_copy[median_index]


def mode(nums: list) -> int:
    value_count = Counter(nums)
    max_freq = value_count.most_common(1)[0][1]
    most_common = list()
    for item, value in value_count.items():
        if value == max_freq:
            most_common.append(item)
    most_common.sort()
    return most_common[0]


if __name__ == '__main__':
    # reading input from stdin
    # size = int(input())
    # data = list(map(int, input().split()))

    data = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
    average = mean(data)
    median_val = median(data)
    mode_val = mode(data)

    print('%.1f' % average)
    print('%.1f' % median_val)
    print(mode_val)
