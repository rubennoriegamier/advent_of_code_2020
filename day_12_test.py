import unittest

from day_12 import parse_instruction, part_1, part_2


class TestDay12(unittest.TestCase):
    def setUp(self):
        self._instructions = list(map(parse_instruction, ['F10', 'N3', 'F7', 'R90', 'F11']))

    def test_part_1(self):
        self.assertEqual(part_1(self._instructions), 25)

    def test_part_2(self):
        self.assertEqual(part_2(self._instructions), 286)


if __name__ == '__main__':
    unittest.main()
