import math

from utils import read_file

data = read_file('05')


def get_middle(num1: int, num2: int, round='up') -> int:
    if round == 'down':
        return (num1 + num2) // 2
    return math.ceil((num1 + num2) / 2)


def get_seat_id(boarding_pass: str) -> int:
    lower_row = 0
    upper_row = 127
    lower_col = 0
    upper_col = 7
    for pos in boarding_pass:
        if pos == 'F':
            upper_row = get_middle(lower_row, upper_row, 'down')
        if pos == 'B':
            lower_row = get_middle(lower_row, upper_row)
        if pos == 'R':
            lower_col = get_middle(lower_col, upper_col)
        if pos == 'L':
            upper_col = get_middle(lower_col, upper_col, 'down')

    return lower_row * 8 + lower_col


seat_ids = [get_seat_id(bp) for bp in data]

print('p1', max(seat_ids))

sorted_seat_ids = sorted(seat_ids)
for i, sid in enumerate(sorted_seat_ids):
    if sorted_seat_ids[i + 1] != sid + 1:
        print('p2', sid + 1)
        break
