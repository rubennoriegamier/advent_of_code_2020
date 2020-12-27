import unittest

from day_17 import parse_grid, part_1, part_2


class TestDay17(unittest.TestCase):
    def setUp(self):
        self._raw_grid = ['.#.', '..#', '###']

    def test_part_1(self):
        active_cubes_3d = parse_grid(self._raw_grid, 3)

        self.assertEqual(part_1(active_cubes_3d), 112)

    def test_part_2(self):
        active_cubes_4d = parse_grid(self._raw_grid, 4)

        self.assertEqual(part_2(active_cubes_4d), 848)


if __name__ == '__main__':
    unittest.main()
