import fileinput
from bisect import bisect_left


def main():
    entries = list(map(int, fileinput.input()))

    print(part_1(entries))
    print(part_2(entries))


def part_1(entries: list[int]) -> int:
    entries = sorted(entries)
    a = 0
    b = len(entries) - 1

    while entries[a] + entries[b] != 2_020:
        while entries[a] + entries[b] < 2_020:
            a += 1
        while entries[a] + entries[b] > 2_020:
            b -= 1

    return entries[a] * entries[b]


def part_2(entries: list[int]) -> int:
    entries = sorted(entries)

    while entries[0] + entries[1] + entries[-1] > 2020:
        del entries[-1]

    for a in range(0, len(entries) - 2):
        for b in range(a + 1, len(entries) - 1):
            c = bisect_left(entries, 2_020 - entries[a] - entries[b], b + 1, len(entries) - 1)

            if entries[a] + entries[b] + entries[c] == 2_020:
                return entries[a] * entries[b] * entries[c]


if __name__ == '__main__':
    main()
