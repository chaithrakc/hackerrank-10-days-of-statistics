"""
“Interquartile Range” and that represents the mid-spread or the middle 50% of our data.
This also helps us understand which values can be considered outliers

https://www.hackerrank.com/challenges/s10-interquartile-range/problem
"""
import day1.p01quartiles


def interQuartile(sample: list, freqs: list) -> float:
    dataset = list()
    for index in range(len(freqs)):
        for i in range(freqs[index]):
            dataset.append(sample[index])
    print(dataset)
    q = day1.p01quartiles.quartiles(dataset)
    return q[2] - q[0]


if __name__ == '__main__':
    values = [6, 12, 8, 10, 20, 16]
    freqs = [5, 4, 3, 2, 1, 5]
    print('%.1f' % interQuartile(values, freqs))
