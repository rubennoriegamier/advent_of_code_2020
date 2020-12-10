import fileinput
from collections import Counter
from collections.abc import Iterable
from functools import lru_cache
from operator import sub


def main():
    output_joltages = list(map(int, fileinput.input()))

    print(part_1(output_joltages))
    print(part_2(output_joltages))


def part_1(output_joltages: Iterable[int]) -> int:
    output_joltages = sorted(output_joltages)
    differences = Counter(map(sub, output_joltages[1:], output_joltages))
    differences[output_joltages[0]] += 1
    differences[3] += 1

    return differences[1] * differences[3]


def part_2(output_joltages: Iterable[int]) -> int:
    output_joltages = sorted(output_joltages)
    output_joltages.insert(0, 0)

    @lru_cache(maxsize=None)
    def distinct_arrangements(i: int) -> int:
        return sum(distinct_arrangements(i + step) for step in (1, 2, 3)
                   if i + step < len(output_joltages) and output_joltages[i + step] - output_joltages[i] <= 3) or 1

    return distinct_arrangements(0)


if __name__ == '__main__':
    main()
