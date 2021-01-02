import fileinput
from collections import Counter
from operator import add

import regex as re

INSTRUCTIONS_RE = re.compile(r'(e|se|sw|w|nw|ne)+')
DIRECTIONS = {'e': (0, 2),
              'se': (-1, 1),
              'sw': (-1, -1),
              'w': (0, -2),
              'nw': (1, -1),
              'ne': (1, 1)}


def main():
    instruction_list = list(map(parse_instructions, map(str.rstrip, fileinput.input())))

    print(part_1(instruction_list))
    print(part_2(instruction_list, 100))


def parse_instructions(raw_instructions):
    return INSTRUCTIONS_RE.fullmatch(raw_instructions).captures(1)


def get_flips_counter(instruction_list):
    flips_counter = Counter()

    for instructions in instruction_list:
        y = 0
        x = 0

        for instruction in instructions:
            y, x = map(add, (y, x), DIRECTIONS[instruction])

        flips_counter[y, x] += 1

    return flips_counter


def part_1(instruction_list):
    flips_counter = get_flips_counter(instruction_list)

    return sum(1 for flips in flips_counter.values() if flips % 2 == 1)


def part_2(instruction_list, days):
    flips_counter = get_flips_counter(instruction_list)
    black_tiles = {tile for tile, flips in flips_counter.items() if flips % 2 == 1}

    for _ in range(days):
        new_black_tiles = set()
        adj_black_tiles_counter = Counter()

        for y, x in black_tiles:
            adj_black_tiles = 0

            for y_inc, x_inc in DIRECTIONS.values():
                adj_tile = y + y_inc, x + x_inc

                if adj_tile in black_tiles:
                    adj_black_tiles += 1
                else:
                    adj_black_tiles_counter[adj_tile] += 1

            if adj_black_tiles == 1 or adj_black_tiles == 2:
                new_black_tiles.add((y, x))

        for tile, adj_black_tiles in adj_black_tiles_counter.items():
            if adj_black_tiles == 2:
                new_black_tiles.add(tile)

        black_tiles = new_black_tiles

    return len(black_tiles)


if __name__ == '__main__':
    main()
