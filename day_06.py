from os import linesep
from sys import stdin
from functools import reduce


def main():
    groups = parse_groups(stdin.read().rstrip())

    print(part_1(groups))
    print(part_2(groups))


def parse_groups(raw_groups: str) -> list[list[str]]:
    return list(map(str.split, raw_groups.split(linesep * 2)))


def anyone_answered_yes_count(group: list[str]) -> int:
    return len(set(''.join(group)))


def everyone_answered_yes_count(group: list[str]) -> int:
    # noinspection PyTypeChecker
    return len(reduce(set.intersection, map(set, group)))


def part_1(groups: list[list[str]]) -> int:
    return sum(map(anyone_answered_yes_count, groups))


def part_2(groups: list[list[str]]) -> int:
    return sum(map(everyone_answered_yes_count, groups))


if __name__ == '__main__':
    main()
