import fileinput
from collections.abc import Iterable


def main():
    entries = list(map(int, fileinput.input()))

    print(part_1(entries))
    print(part_2(entries))


def part_1(entries: Iterable[int]) -> int:
    entries = sorted(entries)

    while entries[0] + entries[-1] != 2_020:
        while entries[0] + entries[-1] < 2_020:
            del entries[0]
        while entries[0] + entries[-1] > 2_020:
            del entries[-1]

    return entries[0] * entries[-1]


def part_2(entries: Iterable[int]) -> int:
    entries = sorted(entries)

    while entries[0] + entries[1] + entries[-1] > 2020:
        del entries[-1]

    return next(entries[a] * entries[b] * entries[c]
                for a in range(0, len(entries) - 2)
                for b in range(a + 1, len(entries) - 1)
                for c in range(b + 1, len(entries))
                if entries[a] + entries[b] + entries[c] == 2_020)


if __name__ == '__main__':
    main()
