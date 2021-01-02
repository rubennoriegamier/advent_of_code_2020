import unittest

from day_23 import part_1, part_2


class TestDay23(unittest.TestCase):
    def setUp(self):
        self._cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]

    def test_part_1(self):
        self.assertEqual(part_1(self._cups, 100), '67384529')

    def test_part_2(self):
        self.assertEqual(part_2(self._cups, 10_000_000), 149_245_887_792)


if __name__ == '__main__':
    unittest.main()
