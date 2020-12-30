import fileinput
from collections import defaultdict
from itertools import chain, islice
from operator import itemgetter, methodcaller


def main():
    tiles = list(map(Tile.parse, ''.join(fileinput.input()).split('\n\n')))
    puzzle = assemble_puzzle(tiles)

    print(part_1(puzzle))
    print(part_2(puzzle))


def part_1(puzzle):
    return puzzle[0][0].id_ * puzzle[0][-1].id_ * puzzle[-1][0].id_ * puzzle[-1][-1].id_


def part_2(puzzle):
    image = tuple(chain.from_iterable(map(''.join, zip(*map(Tile.image_without_borders, row))) for row in puzzle))
    tile = Tile(0, image)

    #                   #
    # #    ##    ##    ###
    #  #  #  #  #  #  #
    for tile in tile.all_variations():
        monsters = sum(1 for i, row in enumerate(islice(tile.image, 1, len(tile.image) - 1), 1)
                       for j in range(len(row) - 19)
                       if row[j] == '1' and row[j + 5] == '1' and row[j + 6] == '1' and row[j + 11] == '1' and
                       row[j + 12] == '1' and row[j + 17] == '1' and row[j + 18] == '1' and row[j + 19] == '1' and
                       tile.image[i - 1][j + 18] == '1' and
                       tile.image[i + 1][j + 1] == '1' and tile.image[i + 1][j + 4] == '1' and
                       tile.image[i + 1][j + 7] == '1' and tile.image[i + 1][j + 10] == '1' and
                       tile.image[i + 1][j + 13] == '1' and tile.image[i + 1][j + 16] == '1')

        if monsters > 0:
            return sum(1 for row in tile.image for x in row if x == '1') - monsters * 15


def assemble_puzzle(tiles):
    puzzle_side_size = round(len(tiles) ** 0.5) * 2 + 1
    initial_tile, *tiles = tiles
    tiles = list(chain.from_iterable(map(Tile.all_variations, tiles)))
    puzzle = [[None] * puzzle_side_size for _ in range(puzzle_side_size)]

    y_center = puzzle_side_size // 2
    x_center = y_center
    puzzle[y_center][x_center] = initial_tile

    top = defaultdict(list)
    bottom = defaultdict(list)
    left = defaultdict(list)
    right = defaultdict(list)

    for tile in tiles:
        top[tile.top].append(tile)
        bottom[tile.bottom].append(tile)
        left[tile.left].append(tile)
        right[tile.right].append(tile)

    # noinspection PyShadowingNames,PyUnresolvedReferences
    def go_up(y, x):
        if puzzle[y - 1][x] is None:
            tile = next((tile for tile in bottom[puzzle[y][x].top] if tile.id_ != puzzle[y][x].id_), None)

            if tile:
                puzzle[y - 1][x] = tile

                go_up(y - 1, x)
                go_left(y - 1, x)
                go_right(y - 1, x)

    # noinspection PyShadowingNames,PyUnresolvedReferences
    def go_down(y, x):
        if puzzle[y + 1][x] is None:
            tile = next((tile for tile in top[puzzle[y][x].bottom] if tile.id_ != puzzle[y][x].id_), None)

            if tile:
                puzzle[y + 1][x] = tile

                go_down(y + 1, x)
                go_left(y + 1, x)
                go_right(y + 1, x)

    # noinspection PyShadowingNames,PyUnresolvedReferences
    def go_left(y, x):
        if puzzle[y][x - 1] is None:
            tile = next((tile for tile in right[puzzle[y][x].left] if tile.id_ != puzzle[y][x].id_), None)

            if tile:
                puzzle[y][x - 1] = tile

                go_up(y, x - 1)
                go_down(y, x - 1)
                go_left(y, x - 1)

    # noinspection PyShadowingNames,PyUnresolvedReferences
    def go_right(y, x):
        if puzzle[y][x + 1] is None:
            tile = next((tile for tile in left[puzzle[y][x].right] if tile.id_ != puzzle[y][x].id_), None)

            if tile:
                puzzle[y][x + 1] = tile

                go_up(y, x + 1)
                go_down(y, x + 1)
                go_right(y, x + 1)

    go_up(y_center, x_center)
    go_down(y_center, x_center)
    go_left(y_center, x_center)
    go_right(y_center, x_center)

    return tuple(tuple(filter(None, row)) for row in puzzle if any(row))


class Tile:
    _TRANSLATE_TO_BINARY = methodcaller('translate', str.maketrans('.#', '01'))
    _FIRST_ITEM = itemgetter(0)
    _LAST_ITEM = itemgetter(-1)

    __slots__ = 'id_', 'image', 'top', 'bottom', 'left', 'right'

    def __init__(self, id_, image):
        self.id_ = id_
        self.image = image
        self.top = int(image[0], 2)
        self.bottom = int(image[-1], 2)
        # noinspection PyTypeChecker
        self.left = int(''.join(map(self._FIRST_ITEM, image)), 2)
        # noinspection PyTypeChecker
        self.right = int(''.join(map(self._LAST_ITEM, image)), 2)

    def clockwise_rotation(self):
        return self.__class__(self.id_, tuple(map(''.join, zip(*self.image[::-1]))))

    def vertical_flip(self):
        return self.__class__(self.id_, self.image[::-1])

    def all_variations(self):
        a = self
        b = self.vertical_flip()

        yield a
        yield b

        for _ in range(3):
            a = a.clockwise_rotation()
            b = b.clockwise_rotation()

            yield a
            yield b

    def image_without_borders(self):
        return tuple(row[1:-1] for row in self.image[1:-1])

    @classmethod
    def parse(cls, raw_tile):
        raw_id, *raw_image = raw_tile.splitlines()
        id_ = int(raw_id.split()[1][:-1])
        image = tuple(map(cls._TRANSLATE_TO_BINARY, raw_image))

        return cls(id_, image)


if __name__ == '__main__':
    main()
