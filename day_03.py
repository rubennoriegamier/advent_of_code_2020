import fileinput
from functools import partial, reduce
from itertools import count, islice
from operator import mul


def main():
    grid = list(map(str.strip, fileinput.input()))

    print(part_1(grid))
    print(part_2(grid))


def part_1(grid: list[str]) -> int:
    return trees_on_the_slope(grid, 3, 1)


def part_2(grid: list[str]) -> int:
    # noinspection PyTypeChecker
    return reduce(mul, map(partial(trees_on_the_slope, grid), (1, 3, 5, 7, 1), (1, 1, 1, 1, 2)))


def trees_on_the_slope(grid: list[str], right: int, down: int) -> int:
    return sum(1 for row, col_idx in zip(islice(grid, 0, None, down), count(0, right))
               if row[col_idx % len(row)] == '#')


if __name__ == '__main__':
    main()
