from collections import defaultdict, deque
from functools import partial
from itertools import count, islice


def main():
    numbers = list(map(int, input().split(',')))

    print(part_1(numbers))
    print(part_2(numbers))


def memory_game(numbers):
    last_number_spoken = numbers[-1]
    last_two_turns = defaultdict(partial(deque, maxlen=2))

    for turn, number in enumerate(numbers, 1):
        yield number

        last_two_turns[number].append(turn)

    ltt = last_two_turns[last_number_spoken]

    for turn in count(len(numbers) + 1):
        if len(ltt) == 1:
            last_number_spoken = 0
        else:
            last_number_spoken = turn - 1 - ltt[0]

        ltt = last_two_turns[last_number_spoken]

        ltt.append(turn)

        yield last_number_spoken


def part_1(numbers):
    return next(islice(memory_game(numbers), 2_020 - 1, None))


def part_2(numbers):
    return next(islice(memory_game(numbers), 30_000_000 - 1, None))


if __name__ == '__main__':
    main()
