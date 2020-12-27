from functools import reduce
from sys import stdin


def main():
    groups = parse_groups(stdin.read().rstrip())

    print(part_1(groups))
    print(part_2(groups))


def parse_groups(raw_groups):
    return list(map(str.split, raw_groups.split('\n\n')))


def anyone_answered_yes_count(group):
    return len(set(''.join(group)))


def everyone_answered_yes_count(group):
    # noinspection PyTypeChecker
    return len(reduce(set.intersection, map(set, group)))


def part_1(groups):
    return sum(map(anyone_answered_yes_count, groups))


def part_2(groups):
    return sum(map(everyone_answered_yes_count, groups))


if __name__ == '__main__':
    main()
