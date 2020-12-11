from utils import read_file, flatten

data = [list(row) for row in read_file(11)]


def safe_get(d, i, j):
    if i == -1 or j == -1:
        return None
    try:
        return d[i][j]
    except IndexError:
        return None


def get_immediately_adjacent_els(d, i, j):
    return [safe_get(d, i + x, j + y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)]


# write me
# we can probably cache something here, ie if you're at 0,0 you only need to check the first row once for horizontal
def get_first_seat_in_each_direction(d, i, j):
    pass


def run_model(seat_map, fn, tolerance):
    d = [[0 for x in range(len(seat_map[0]))] for y in range(len(seat_map))]
    for i, row in enumerate(seat_map):
        for j, seat in enumerate(row):
            adjacent_els = fn(seat_map, i, j)
            if seat == 'L' and all([el != '#' for el in adjacent_els]):
                d[i][j] = '#'
            elif seat == '#' and len([el for el in adjacent_els if el == '#']) >= tolerance:
                d[i][j] = 'L'
            else:
                d[i][j] = seat_map[i][j]
    return d


def solve(fn, tolerance=4):
    seat_map = data
    while True:
        model = run_model(seat_map, fn, tolerance)
        if model == seat_map:
            return len([el for el in flatten(model) if el == '#'])
        seat_map = model


print('p1', solve(get_immediately_adjacent_els))
print('p2', solve(get_first_seat_in_each_direction, 5))
