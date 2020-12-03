import unittest

from day_03 import part_1, part_2


class TestDay03(unittest.TestCase):
    def setUp(self):
        self._grid = ['..##.......',
                      '#...#...#..',
                      '.#....#..#.',
                      '..#.#...#.#',
                      '.#...##..#.',
                      '..#.##.....',
                      '.#.#.#....#',
                      '.#........#',
                      '#.##...#...',
                      '#...##....#',
                      '.#..#...#.#']

    def test_part_1(self):
        self.assertEqual(part_1(self._grid), 7)

    def test_part_2(self):
        self.assertEqual(part_2(self._grid), 336)


if __name__ == '__main__':
    unittest.main()
