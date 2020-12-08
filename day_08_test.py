import unittest

from day_08 import parse_instruction, part_1, part_2


class TestDay08(unittest.TestCase):
    def setUp(self):
        self._instructions = list(map(parse_instruction, ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3',
                                                          'acc -99', 'acc +1', 'jmp -4', 'acc +6']))

    def test_part_1(self):
        self.assertEqual(part_1(self._instructions), 5)

    def test_part_2(self):
        self.assertEqual(part_2(self._instructions), 8)


if __name__ == '__main__':
    unittest.main()
