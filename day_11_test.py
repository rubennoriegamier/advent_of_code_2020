import unittest

from day_11 import part_1, part_2


class TestDay11(unittest.TestCase):
    def setUp(self):
        self._layout = ['#.##.##.##',
                        '#######.##',
                        '#.#.#..#..',
                        '####.##.##',
                        '#.##.##.##',
                        '#.#####.##',
                        '..#.#.....',
                        '##########',
                        '#.######.#',
                        '#.#####.##']

    def test_part_1(self):
        self.assertEqual(part_1(self._layout), 37)

    def test_part_2(self):
        self.assertEqual(part_2(self._layout), 26)


if __name__ == '__main__':
    unittest.main()
