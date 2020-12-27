import fileinput
from itertools import islice


def main():
    boarding_passes = list(map(str.rstrip, fileinput.input()))

    print(part_1(boarding_passes))
    print(part_2(boarding_passes))


def part_1(boarding_passes):
    return max(map(seat_id, boarding_passes))


def part_2(boarding_passes):
    seat_ids = sorted(map(seat_id, boarding_passes))

    return next(curr_seat_id + 1 for curr_seat_id, next_seat_id in zip(seat_ids, islice(seat_ids, 1, None))
                if next_seat_id - curr_seat_id == 2)


def seat_id(boarding_pass):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

    for char in boarding_pass:
        if char == 'F':
            max_row -= max_row - min_row + 1 >> 1
        elif char == 'B':
            min_row += max_row - min_row + 1 >> 1
        elif char == 'L':
            max_col -= max_col - min_col + 1 >> 1
        elif char == 'R':
            min_col += max_col - min_col + 1 >> 1

    return min_row * 8 + min_col


if __name__ == '__main__':
    main()
