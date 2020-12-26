import unittest

from day_14 import part_1, part_2


class TestDay14(unittest.TestCase):
    def test_part_1(self):
        program = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
                   'mem[8] = 11',
                   'mem[7] = 101',
                   'mem[8] = 0']

        self.assertEqual(part_1(program), 165)

    def test_part_2(self):
        program = ['mask = 000000000000000000000000000000X1001X',
                   'mem[42] = 100',
                   'mask = 00000000000000000000000000000000X0XX',
                   'mem[26] = 1']

        self.assertEqual(part_2(program), 208)


if __name__ == '__main__':
    unittest.main()
