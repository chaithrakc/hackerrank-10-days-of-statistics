# weighted mean tutorial - real time example
# https://www.hackerrank.com/challenges/s10-weighted-mean/tutorial

import numpy as np


def weighted_mean(values: list, costs: list) -> float:
    total_weight = sum([val * cost for val, cost in zip(values, costs)])
    weighted_avg = total_weight / sum(costs)
    return '%.1f' % weighted_avg


if __name__ == '__main__':
    data = [10, 40, 30, 50, 20]
    weights = [1, 2, 3, 4, 5]
    print(weighted_mean(data, weights))

    # using numpy
    avg = np.average(np.array(data), weights=np.array(weights))
    print(avg)

