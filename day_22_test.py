import unittest

from day_22 import part_1, part_2


class TestDay22(unittest.TestCase):
    def setUp(self):
        self._deck_1 = [9, 2, 6, 3, 1]
        self._deck_2 = [5, 8, 4, 7, 10]

    def test_part_1(self):
        self.assertEqual(part_1(self._deck_1, self._deck_2), 306)

    def test_part_2(self):
        self.assertEqual(part_2(self._deck_1, self._deck_2)[1], 291)


if __name__ == '__main__':
    unittest.main()
