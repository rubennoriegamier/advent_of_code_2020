import fileinput
from itertools import islice


def main():
    data = list(map(int, fileinput.input()))

    n = part_1(data, 25)
    print(n)
    print(part_2(data, n))


def part_1(data, preamble_len):
    for i, n in enumerate(islice(data, preamble_len, None), preamble_len):
        preamble = data[i - preamble_len:i]
        preamble.sort()

        while len(preamble) >= 2 and preamble[0] + preamble[-1] != n:
            while len(preamble) >= 2 and preamble[0] + preamble[-1] < n:
                del preamble[0]
            while len(preamble) >= 2 and preamble[0] + preamble[-1] > n:
                del preamble[-1]

        if len(preamble) == 1:
            return n


def part_2(data, n):
    i = 0
    j = 1
    s = data[i] + data[j]

    while s != n:
        while s < n:
            j += 1
            s += data[j]
        while s > n:
            s -= data[i]
            i += 1

    return min(islice(data, i, j + 1)) + max(islice(data, i, j + 1))


if __name__ == '__main__':
    main()
