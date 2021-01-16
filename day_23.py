import numba as nb
import numpy as np


def main():
    cups = np.fromiter(map(int, input()), dtype=np.int64)

    print(part_1(cups, 100))
    print(part_2(cups, 1_000_000, 10_000_000))


def part_1(cups, moves):
    next_cup_idx = list(range(1, len(cups) + 1))
    next_cup_idx[-1] = 0

    indexes = [0] * (len(cups) + 1)
    for idx, cup in enumerate(cups):
        indexes[cup] = idx

    idx = 0

    for _ in range(moves):
        pick_up_a_idx = next_cup_idx[idx]
        pick_up_b_idx = next_cup_idx[pick_up_a_idx]
        pick_up_c_idx = next_cup_idx[pick_up_b_idx]

        next_cup_idx[idx] = next_cup_idx[pick_up_c_idx]

        destination = cups[idx] - 1

        while (destination == cups[pick_up_a_idx] or
               destination == cups[pick_up_b_idx] or
               destination == cups[pick_up_c_idx]):
            destination -= 1

        if destination == 0:
            destination = len(cups)

            while (destination == cups[pick_up_a_idx] or
                   destination == cups[pick_up_b_idx] or
                   destination == cups[pick_up_c_idx]):
                destination -= 1

        destination_idx = indexes[destination]

        next_cup_idx[pick_up_c_idx] = next_cup_idx[destination_idx]
        next_cup_idx[destination_idx] = pick_up_a_idx

        idx = next_cup_idx[idx]

    idx = indexes[1]
    result = ''

    for _ in range(len(cups) - 1):
        idx = next_cup_idx[idx]

        result += str(cups[idx])

    return result


@nb.njit(nb.int64(nb.int64[:], nb.int64, nb.int64))
def part_2(initial_cups, size, moves):
    cups = np.arange(1, size + 1, dtype=np.int64)
    cups[0:len(initial_cups)] = initial_cups

    next_cup_idx = np.arange(1, size + 1, dtype=np.int64)
    next_cup_idx[-1] = 0

    indexes = np.arange(-1, size, dtype=np.int64)
    for idx, cup in enumerate(initial_cups):
        indexes[cup] = idx

    idx = 0

    for _ in range(moves):
        pick_up_a_idx = next_cup_idx[idx]
        pick_up_b_idx = next_cup_idx[pick_up_a_idx]
        pick_up_c_idx = next_cup_idx[pick_up_b_idx]

        next_cup_idx[idx] = next_cup_idx[pick_up_c_idx]

        destination = cups[idx] - 1

        while (destination == cups[pick_up_a_idx] or
               destination == cups[pick_up_b_idx] or
               destination == cups[pick_up_c_idx]):
            destination -= 1

        if destination == 0:
            destination = len(cups)

            while (destination == cups[pick_up_a_idx] or
                   destination == cups[pick_up_b_idx] or
                   destination == cups[pick_up_c_idx]):
                destination -= 1

        destination_idx = indexes[destination]

        next_cup_idx[pick_up_c_idx] = next_cup_idx[destination_idx]
        next_cup_idx[destination_idx] = pick_up_a_idx

        idx = next_cup_idx[idx]

    idx_a = next_cup_idx[indexes[1]]
    idx_b = next_cup_idx[idx_a]

    return cups[idx_a] * cups[idx_b]


if __name__ == '__main__':
    main()
