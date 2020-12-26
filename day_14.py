import fileinput
import re

ASSIGNMENT_RE = re.compile(r'mem\[(\d+)\] = (\d+)')
X_RE = re.compile('X')


def main():
    program = list(map(str.rstrip, fileinput.input()))

    print(part_1(program))
    print(part_2(program))


def parse_mask(mask):
    mask = mask.split()[-1]
    and_mask = int(mask.replace('X', '1'), 2)
    or_mask = int(mask.replace('X', '0'), 2)

    return and_mask, or_mask


def part_1(program):
    and_mask = None
    or_mask = None
    memory = {}

    for instruction in program:
        if instruction.startswith('mask'):
            and_mask, or_mask = parse_mask(instruction)
        else:
            address, value = map(int, ASSIGNMENT_RE.fullmatch(instruction).groups())
            memory[address] = value & and_mask | or_mask

    return sum(memory.values())


def part_2(program):
    or_mask = None
    x_bits = None
    memory = {}

    for instruction in program:
        if instruction.startswith('mask'):
            mask = instruction.split()[-1]
            or_mask = int(mask.replace('X', '0'), 2)
            x_bits = [len(mask) - match.start() - 1 for match in X_RE.finditer(mask)]
        else:
            address, value = map(int, ASSIGNMENT_RE.fullmatch(instruction).groups())
            address |= or_mask

            for n in range(0, 1 << len(x_bits)):
                x_mask = f'{n:0{len(x_bits)}b}'
                address_ = address

                for x_bit, status in zip(x_bits, x_mask):
                    if status == '0':
                        address_ &= ~(1 << x_bit)
                    else:
                        address_ |= 1 << x_bit

                memory[address_] = value

    return sum(memory.values())


if __name__ == '__main__':
    main()
