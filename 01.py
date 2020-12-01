from typing import List, Tuple

from utils import read_file

data = [int(n) for n in read_file('01')]


# part 1
def find_addends(nums: List[int], tgt: int) -> Tuple[int, int]:
    num_map = {}
    for i, num in enumerate(nums):
        diff = tgt - num
        if num_map.get(diff):
            return nums[num_map[diff]], nums[i]
        num_map[num] = i
    return 'not found'


x, y = find_addends(data, 2020)

print('part 1', x * y)


# part 2
def find_three_addends(nums: List[int], tgt: int) -> Tuple[int, int]:
    for num in nums:
        new_tgt = tgt - num
        addends = find_addends(nums, new_tgt)
        if addends != 'not found':
            add1, add2 = addends
            return 2020 - new_tgt, add1, add2


a1, a2, a3 = find_three_addends(data, 2020)

print('part 2', a1 * a2 * a3)
