from itertools import chain


def main():
    cups = list(map(int, input()))

    print(part_1(cups, 100))
    print(part_2(cups, 10_000_000))


def game(cups, moves):
    right = []
    indexes = [0] * (len(cups) + 1)

    for idx, cup in enumerate(cups):
        right.append((idx + 1) % len(cups))
        indexes[cup] = idx

    idx = 0

    for _ in range(moves):
        pick_up_a_idx = right[idx]
        pick_up_b_idx = right[pick_up_a_idx]
        pick_up_c_idx = right[pick_up_b_idx]

        right[idx] = right[pick_up_c_idx]

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

        right[pick_up_c_idx] = right[destination_idx]
        right[destination_idx] = pick_up_a_idx

        idx = right[idx]

    idx = indexes[1]

    for _ in range(len(cups) - 1):
        idx = right[idx]

        yield cups[idx]


def part_1(cups, moves):
    return ''.join(map(str, game(cups, moves)))


def part_2(cups, moves):
    g = game(list(chain(cups, range(max(cups) + 1, 1_000_001))), moves)

    return next(g) * next(g)


if __name__ == '__main__':
    main()
