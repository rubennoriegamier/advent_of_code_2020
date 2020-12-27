import fileinput
from collections import Counter


def main():
    raw_grid = list(fileinput.input())
    active_cubes_3d = parse_grid(raw_grid, 3)
    active_cubes_4d = parse_grid(raw_grid, 4)

    print(part_1(active_cubes_3d))
    print(part_2(active_cubes_4d))


def parse_grid(raw_grid, dimensions):
    return {(x, y) + (0,) * (dimensions - 2)
            for y, row in enumerate(raw_grid)
            for x, cube in enumerate(row)
            if cube == '#'}


def next_cycle_3d(active_cubes):
    next_active_cubes = set()
    inactive_cubes = Counter()

    for x, y, z in active_cubes:
        active_neighbor_count = 0

        for new_x in range(x - 1, x + 2):
            for new_y in range(y - 1, y + 2):
                for new_z in range(z - 1, z + 2):
                    if new_x != x or new_y != y or new_z != z:
                        neighbor = new_x, new_y, new_z

                        if neighbor in active_cubes:
                            active_neighbor_count += 1
                        else:
                            inactive_cubes[neighbor] += 1

        if active_neighbor_count == 2 or active_neighbor_count == 3:
            next_active_cubes.add((x, y, z))

    for inactive_cube, active_neighbor_count in inactive_cubes.items():
        if active_neighbor_count == 3:
            next_active_cubes.add(inactive_cube)

    return next_active_cubes


def next_cycle_4d(active_cubes):
    next_active_cubes = set()
    inactive_cubes = Counter()

    for x, y, z, w in active_cubes:
        active_neighbor_count = 0

        for new_x in range(x - 1, x + 2):
            for new_y in range(y - 1, y + 2):
                for new_z in range(z - 1, z + 2):
                    for new_w in range(w - 1, w + 2):
                        if new_x != x or new_y != y or new_z != z or new_w != w:
                            neighbor = new_x, new_y, new_z, new_w

                            if neighbor in active_cubes:
                                active_neighbor_count += 1
                            else:
                                inactive_cubes[neighbor] += 1

        if active_neighbor_count == 2 or active_neighbor_count == 3:
            next_active_cubes.add((x, y, z, w))

    for inactive_cube, active_neighbor_count in inactive_cubes.items():
        if active_neighbor_count == 3:
            next_active_cubes.add(inactive_cube)

    return next_active_cubes


def part_1(active_cubes):
    for _ in range(6):
        active_cubes = next_cycle_3d(active_cubes)

    return len(active_cubes)


def part_2(active_cubes):
    for _ in range(6):
        active_cubes = next_cycle_4d(active_cubes)

    return len(active_cubes)


if __name__ == '__main__':
    main()
