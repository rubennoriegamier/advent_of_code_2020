import fileinput
from collections import deque
from itertools import islice
from operator import mul


def main():
    deck_1, deck_2 = (list(map(int, raw_deck.splitlines()[1:]))
                      for raw_deck in ''.join(fileinput.input()).split('\n\n'))

    print(part_1(deck_1, deck_2))
    print(part_2(deck_1, deck_2)[1])


def part_1(deck_1, deck_2):
    deck_1 = deque(deck_1)
    deck_2 = deque(deck_2)

    while deck_1 and deck_2:
        if deck_1[0] > deck_2[0]:
            deck_1.rotate(-1)
            deck_1.append(deck_2.popleft())
        else:
            deck_2.rotate(-1)
            deck_2.append(deck_1.popleft())

    return sum(map(mul, deck_1 or deck_2, range(len(deck_1) or len(deck_2), 0, -1)))


def part_2(deck_1, deck_2):
    deck_1 = deque(deck_1)
    deck_2 = deque(deck_2)
    prev_rounds = set()

    while deck_1 and deck_2:
        curr_round = tuple(deck_1), tuple(deck_2)

        if curr_round in prev_rounds:
            return 1, sum(map(mul, deck_1, range(len(deck_1), 0, -1)))
        prev_rounds.add(curr_round)

        if deck_1[0] < len(deck_1) and deck_2[0] < len(deck_2):
            if part_2(islice(deck_1, 1, deck_1[0] + 1), islice(deck_2, 1, deck_2[0] + 1))[0] == 1:
                deck_1.rotate(-1)
                deck_1.append(deck_2.popleft())
            else:
                deck_2.rotate(-1)
                deck_2.append(deck_1.popleft())
        elif deck_1[0] > deck_2[0]:
            deck_1.rotate(-1)
            deck_1.append(deck_2.popleft())
        else:
            deck_2.rotate(-1)
            deck_2.append(deck_1.popleft())

    if deck_1:
        return 1, sum(map(mul, deck_1, range(len(deck_1), 0, -1)))
    return 2, sum(map(mul, deck_2, range(len(deck_2), 0, -1)))


if __name__ == '__main__':
    main()
