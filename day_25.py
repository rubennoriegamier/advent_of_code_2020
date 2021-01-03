def main():
    card_public_key = int(input())
    door_public_key = int(input())

    print(part_1(card_public_key, door_public_key))


def get_loop_size(key, subject):
    loop_size = 0
    value = 1

    while value != key:
        value = value * subject % 20_201_227
        loop_size += 1

    return loop_size


def get_encryption_key(subject, loop_size):
    value = 1

    for _ in range(loop_size):
        value = value * subject % 20_201_227

    return value


def part_1(card_public_key, door_public_key):
    card_loop_size = get_loop_size(card_public_key, 7)

    return get_encryption_key(door_public_key, card_loop_size)


if __name__ == '__main__':
    main()
