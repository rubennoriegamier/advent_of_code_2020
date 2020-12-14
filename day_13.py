from functools import partial
from itertools import count, islice
from operator import ne


def main():
    ts = int(input())
    ids = input().rstrip().split(',')

    print(part_1(ts, ids))
    print(part_2(ids))


def wait_time(ts, id_):
    return id_ - ts % id_


# noinspection PyTypeChecker
def part_1(ts, ids):
    ids = map(int, filter(partial(ne, 'x'), ids))
    id_ = min(ids, key=partial(wait_time, ts))

    return wait_time(ts, id_) * id_


def part_2(ids):
    gen = count(1)

    for idx, id_ in enumerate(ids):
        if id_ != 'x':
            a, b = islice((n for n in gen if (n + idx) % int(id_) == 0), 2)
            gen = count(a, b - a)

    return next(gen)


if __name__ == '__main__':
    main()
