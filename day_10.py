import fileinput
from collections import Counter
from functools import lru_cache
from operator import sub


def main():
    joltages = list(map(int, fileinput.input()))

    print(part_1(joltages))
    print(part_2(joltages))


def part_1(joltages):
    joltages = sorted(joltages)
    differences = Counter(map(sub, joltages[1:], joltages))
    differences[joltages[0]] += 1
    differences[3] += 1

    return differences[1] * differences[3]


def part_2(joltages):
    joltages = sorted(joltages)
    joltages.insert(0, 0)

    @lru_cache(maxsize=None)
    def arrangements(i):
        return sum(arrangements(j) for j in range(i + 1, min(i + 4, len(joltages)))
                   if joltages[j] - joltages[i] <= 3) or 1

    return arrangements(0)


if __name__ == '__main__':
    main()
