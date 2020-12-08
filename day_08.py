import fileinput
from collections import namedtuple
from collections.abc import Sequence

Instruction = namedtuple('Instruction', ('operation', 'argument'))


def main():
    instructions = list(map(parse_instruction, fileinput.input()))

    print(part_1(instructions))
    print(part_2(instructions))


def parse_instruction(raw_instruction: str) -> Instruction:
    operation, raw_argument = raw_instruction.split()

    return Instruction(operation, int(raw_argument))


def part_1(instructions: Sequence[Instruction]) -> int:
    acc = 0
    pos = 0
    exe_ins = set()

    while pos not in exe_ins:
        ins = instructions[pos]

        exe_ins.add(pos)
        if ins.operation == 'acc':
            acc += ins.argument
            pos += 1
        elif ins.operation == 'jmp':
            pos += ins.argument
        elif ins.operation == 'nop':
            pos += 1

    return acc


def part_2(instructions: Sequence[Instruction]) -> int:
    acc = [0, None]
    pos = [0]
    exe_ins = [set()]

    while pos[0] < len(instructions):
        ins = instructions[pos[0]]

        exe_ins[0].add(pos[0])
        if ins.operation == 'acc':
            acc[0] += ins.argument
            pos[0] += 1
        elif ins.operation == 'jmp':
            if acc[1] is None:
                acc = [acc[0], acc[0]]
                pos = [pos[0] + 1, pos[0] + ins.argument]
                exe_ins = [exe_ins[0].copy(), exe_ins[0]]
            else:
                pos[0] += ins.argument
        elif ins.operation == 'nop':
            if acc[1] is None and ins.argument > 0:
                acc = [acc[0], acc[0]]
                pos = [pos[0] + ins.argument, pos[0] + 1]
                exe_ins = [exe_ins[0].copy(), exe_ins[0]]
            else:
                pos[0] += 1

        if pos[0] in exe_ins[0]:
            acc = [acc[1], None]
            pos = [pos[1]]
            exe_ins = [exe_ins[1]]

    return acc[0]


if __name__ == '__main__':
    main()
