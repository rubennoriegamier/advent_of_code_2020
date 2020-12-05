import unittest

from day_05 import seat_id, part_1, part_2


class TestDay05(unittest.TestCase):
    def test_seat_id(self):
        self.assertEqual(seat_id('FBFBBFFRLR'), 357)
        self.assertEqual(seat_id('BFFFBBFRRR'), 567)
        self.assertEqual(seat_id('FFFBBBFRRR'), 119)
        self.assertEqual(seat_id('BBFFBBFRLL'), 820)

    def test_part_1(self):
        self.assertEqual(part_1(['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']), 820)

    def test_part_2(self):
        self.assertEqual(part_2(['FFFFFFBLLL', 'FFFFFFBLLR', 'FFFFFFBLRL', 'FFFFFFBLRR', 'FFFFFFBRLL',
                                 'FFFFFFBRRL', 'FFFFFFBRRR', 'FFFFFBFLLL', 'FFFFFBFLLR', 'FFFFFBFLRL']), 13)


if __name__ == '__main__':
    unittest.main()
