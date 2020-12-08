from typing import List, Tuple

from utils import read_file

data = read_file(7)


def get_bag_color(bag: str):
    return bag.rsplit(' ', 1)[0]


def parse_bag_str(bag_str: str) -> Tuple[str, List[Tuple[str, int]]]:
    outer, inner = bag_str.split(' contain ')
    outer = get_bag_color(outer)
    contents = []
    for bag in inner.split(', '):
        if bag != 'no other bags.':
            num_bags, bag_type = bag.split(' ', 1)
            bag_type = get_bag_color(bag_type)
            contents.append((bag_type, int(num_bags)))

    return outer, contents


bag_map = dict([parse_bag_str(bag) for bag in data])


def p1():
    def find_gold_bags(bag_name: str):
        res = 0
        for contents in bag_map[bag_name]:
            if not contents:
                return 0
            if contents[0] == 'shiny gold':
                res = 1
            res = res or find_gold_bags(contents[0])
        return res

    return sum(find_gold_bags(b) for b in bag_map)


print(p1())


def p2():
    def get_bag_count(color='shiny gold'):
        if not bag_map.get(color):
            return 0
        total_sub_bags = 0
        for child_color, amt in bag_map[color]:
            total_sub_bags += amt * (get_bag_count(child_color) + 1)

        return total_sub_bags

    return get_bag_count()


print(p2())
