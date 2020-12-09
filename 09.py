from typing import List

from utils import read_file

data = [int(line) for line in read_file(9)]


def is_sum_of_addends(num: int, addends: List[int]) -> bool:
    sums = set()
    for i, n1 in enumerate(addends):
        for n2 in addends[i + 1:]:
            sums.add(n1 + n2)
    return num in sums


def first_sum(min_i, max_i):
    cur = max_i

    while cur < len(data):
        num = data[cur]
        addends = data[min_i:max_i]
        if not is_sum_of_addends(num, addends):
            return num
        min_i += 1
        max_i += 1
        cur += 1


p1 = first_sum(0, 25)
print('p1', p1)


def get_all_subarrays(arr):
    for i in range(1, len(arr) + 1):
        for j in range(len(arr) - i + 1):
            yield arr[j:j + i]


def get_sum_range(tgt, nums):
    for subarray in get_all_subarrays(nums):
        subarray_sum = sum(subarray)
        if subarray_sum == tgt and len(subarray) > 1:
            return min(subarray) + max(subarray)


print('p2', get_sum_range(p1, data))
