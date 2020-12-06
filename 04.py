from collections import Counter
from typing import List

from utils import read_file

data = read_file('04', do_strip=False)

REQUIRED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def split_passports(passport: str) -> List[str]:
    split_by_newline = passport.split('\n')
    split_by_spaces = ' '.join(split_by_newline).split(' ')
    return [s[:3] for s in split_by_spaces]


def is_valid(passport: List[str]):
    return all(field in passport for field in REQUIRED_FIELDS)


def part_1():
    passports = [split_passports(p) for p in ''.join(data).split('\n\n')]
    return Counter(is_valid(p) for p in passports)[True]


print('p1', part_1())
