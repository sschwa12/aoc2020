from collections import Counter
from typing import Tuple, List

from utils import read_file

data = read_file('02')


def split_pass(password: str) -> Tuple[int, int, str, str]:
    policy, char, pw = password.split(' ')
    policy_range = policy.split('-')
    sanitized_char = char[0]
    start, end = [int(p) for p in policy_range]
    return start, end, sanitized_char, pw


def is_valid(password: str) -> bool:
    start, end, char, pw = split_pass(password)
    char_count = Counter(pw)
    if start <= char_count[char] <= end:
        return True
    return False


def is_valid2(password: str) -> bool:
    i, j, char, pw = split_pass(password)
    first = pw[i - 1]
    second = pw[j - 1]
    return len([c for c in [first, second] if c == char]) == 1


print('part 1', Counter((is_valid(pw) for pw in data))[True])
print('part 2', Counter((is_valid2(pw) for pw in data))[True])
