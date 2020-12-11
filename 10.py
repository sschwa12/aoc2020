from collections import Counter
from functools import reduce, lru_cache
from operator import mul

from utils import read_file

data = [int(d) for d in read_file(10)]

d = sorted(data)
d.append(d[-1] + 3)
d.insert(0, 0)


def get_jolt_differences() -> int:
    diffs = []

    for i in range(1, len(d)):
        num = d[i]
        prev_num = d[i - 1]
        diffs.append(num - prev_num)

    return reduce(mul, Counter(diffs).values())


print('p1', get_jolt_differences())


def get_paths(joltages, cache={}):
    key = ','.join([str(j) for j in joltages])
    if key in cache:
        return cache[key]
    cnt = 1
    for i in range(1, len(joltages) - 1):
        if joltages[i + 1] - joltages[i - 1] <= 3:
            new_joltages = [joltages[i - 1]] + joltages[i + 1:]
            cnt += get_paths(new_joltages, cache)

    cache[key] = cnt
    return cnt


print(d)
print(get_paths(d))

lru_cache