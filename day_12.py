import fileinput
from collections import deque


def main():
    instructions = list(map(parse_instruction, fileinput.input()))

    print(part_1(instructions))
    print(part_2(instructions))


def parse_instruction(raw_instruction):
    return raw_instruction[0], int(raw_instruction[1:])


def part_1(instructions):
    x = 0
    y = 0
    helm = deque([1, 0, -1, 0])

    for action, value in instructions:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            helm.rotate(value // 90)
        elif action == 'R':
            helm.rotate(value // -90)
        elif action == 'F':
            x += helm[0] * value
            y += helm[1] * value

    return abs(x) + abs(y)


def part_2(instructions):
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1

    for action, value in instructions:
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L':
            for _ in range(value // 90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif action == 'R':
            for _ in range(value // 90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif action == 'F':
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value

    return abs(ship_x) + abs(ship_y)


if __name__ == '__main__':
    main()
