# weighted mean tutorial - real time example
# https://www.hackerrank.com/challenges/s10-weighted-mean/tutorial

def weighted_mean(values: list, costs: list) -> float:
    total_weight = 0
    for val, cost in zip(values, costs):
        total_weight = total_weight + (val * cost)
    return '%.1f' % (total_weight / sum(costs))


if __name__ == '__main__':
    data = [10, 40, 30, 50, 20]
    weights = [1, 2, 3, 4, 5]
    print(weighted_mean(data, weights))
