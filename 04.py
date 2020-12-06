import re
from typing import List

from utils import read_file

data = read_file('04', do_strip=False)

REQUIRED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
EYE_COLORS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


class PassportValidator:
    def __init__(self, passports):
        self.passports = passports

    def byr(self, year):
        return 1920 <= int(year) <= 2002

    def iyr(self, year):
        return 2010 <= int(year) <= 2020

    def eyr(self, year):
        return 2020 <= int(year) <= 2030

    def hgt(self, height):
        value = height[:-2]
        unit_of_measurement = height[-2:]
        if unit_of_measurement == 'cm':
            return 150 <= int(value) <= 193
        elif unit_of_measurement == 'in':
            return 59 <= int(value) <= 76
        return False

    def hcl(self, hair_color):
        if hair_color[0] != '#':
            return False
        hex = hair_color[1:]
        if len(hex) != 6:
            return False
        return bool(re.match('^[a-f0-9]*$', hex))

    def ecl(self, eye_color):
        return eye_color in EYE_COLORS

    def pid(self, passport_id):
        # this could definitely break in some edge cases but let's see what happens
        return len(passport_id) == 9

    def validate_field(self, field):
        f_name, f_val = field.split(':')
        return getattr(self, f_name)(f_val)

    def cid(self, _):
        return True

    def run(self):
        return [all([self.validate_field(field) for field in passport]) for passport in self.passports]


def split_passports(passport: str) -> List[str]:
    split_by_newline = passport.split('\n')
    split_by_spaces = ' '.join(split_by_newline).split(' ')
    return [s for s in split_by_spaces]


passports = [split_passports(p) for p in ''.join(data).split('\n\n')]


def is_valid(passport: List[str]) -> bool:
    field_names_only = [f[:3] for f in passport]
    return all(field in field_names_only for field in REQUIRED_FIELDS)


def get_passports_with_reqd_fields() -> List[str]:
    return [p for p in passports if is_valid(p)]


passports_with_reqd_fields = get_passports_with_reqd_fields()

print('p1', len(passports_with_reqd_fields))

v = PassportValidator(passports_with_reqd_fields)
print('p2', len([res for res in v.run() if res]))
