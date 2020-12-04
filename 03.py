from functools import reduce
from typing import List, Tuple

from utils import read_file

data = [list(r) for r in read_file('03')]


def count_trees(tree_map: List[str], slope: Tuple[int, int]) -> int:
    right, down = slope
    count = 0
    idx = right
    for i in range(down, len(tree_map), down):
        row = tree_map[i]
        row_length = len(row)
        if idx >= row_length:
            idx -= row_length
        if row[idx] == '#':
            count += 1
        idx += right
    return count


print('p1', count_trees(data, (3, 1)))

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def mult_slopes(slopes: Tuple[int, int]) -> int:
    counts = [count_trees(data, slope) for slope in slopes]
    return reduce((lambda x, y: x * y), counts)


print('p2', mult_slopes(SLOPES))
