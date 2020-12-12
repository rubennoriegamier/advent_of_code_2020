import fileinput
from collections import defaultdict
from functools import partial
from itertools import chain, islice
from operator import eq


def main():
    layout = list(map(str.rstrip, fileinput.input()))

    print(part_1(layout))
    print(part_2(layout))


def part_1(layout: list[str]) -> int:
    layout = [list(f'.{row}.') for row in layout]
    layout.append(list('.' * len(layout[0])))
    chaos = True
    counter = [[0] * len(row) for row in layout]

    while chaos:
        chaos = False

        for row_idx, row in enumerate(islice(layout, len(layout) - 1)):
            row_counter = counter[row_idx]
            next_row_counter = counter[row_idx + 1]
            row_layout = layout[row_idx]
            next_row_layout = layout[row_idx + 1]

            for col_idx, tile in enumerate(row):
                if tile == 'L':
                    if row_counter[col_idx] == 0:
                        if (row_layout[col_idx + 1] != '#' and
                                next_row_layout[col_idx - 1] != '#' and
                                next_row_layout[col_idx] != '#' and
                                next_row_layout[col_idx + 1] != '#'):
                            chaos = True
                            row[col_idx] = '#'
                    else:
                        row_counter[col_idx] = 0
                elif tile == '#':
                    row_counter[col_idx + 1] += 1
                    next_row_counter[col_idx - 1] += 1
                    next_row_counter[col_idx] += 1
                    next_row_counter[col_idx + 1] += 1
                    n = row_counter[col_idx] + ((row_layout[col_idx + 1] == '#') +
                                                (next_row_layout[col_idx - 1] == '#') +
                                                (next_row_layout[col_idx] == '#') +
                                                (next_row_layout[col_idx + 1] == '#'))
                    if n >= 4:
                        chaos = True
                        row[col_idx] = 'L'
                    row_counter[col_idx] = 0

    return sum(map(partial(eq, '#'), chain.from_iterable(layout)))


def part_2(layout: list[str]) -> int:
    layout = list(map(list, layout))
    chaos = True
    counter = [[0] * len(row) for row in layout]
    visibility = defaultdict(list)

    for row_idx, row in enumerate(layout):
        for col_idx, tile in enumerate(row):
            if tile != '.':
                for row_step, col_step in (0, 1), (1, -1), (1, 0), (1, 1):
                    visible_row_idx = row_idx + row_step
                    visible_col_idx = col_idx + col_step

                    while visible_row_idx < len(layout) and 0 <= visible_col_idx < len(row):
                        if layout[visible_row_idx][visible_col_idx] != '.':
                            visibility[row_idx, col_idx].append((visible_row_idx, visible_col_idx))
                            break
                        visible_row_idx += row_step
                        visible_col_idx += col_step

    while chaos:
        chaos = False

        for row_idx, row in enumerate(layout):
            row_counter = counter[row_idx]

            for col_idx, tile in enumerate(row):
                if tile == 'L':
                    if row_counter[col_idx] == 0:
                        for visible_row_idx, visible_col_idx in visibility[row_idx, col_idx]:
                            if layout[visible_row_idx][visible_col_idx] == '#':
                                break
                        else:
                            chaos = True
                            row[col_idx] = '#'
                    else:
                        row_counter[col_idx] = 0
                elif tile == '#':
                    n = row_counter[col_idx]

                    for visible_row_idx, visible_col_idx in visibility[row_idx, col_idx]:
                        counter[visible_row_idx][visible_col_idx] += 1
                        n += layout[visible_row_idx][visible_col_idx] == '#'
                    if n >= 5:
                        chaos = True
                        row[col_idx] = 'L'
                    row_counter[col_idx] = 0

    return sum(map(partial(eq, '#'), chain.from_iterable(layout)))


if __name__ == '__main__':
    main()
