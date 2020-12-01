import unittest

from day_01 import part_1, part_2


class TestDay01(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1([1_721, 979, 366, 299, 675, 1_456]), 514_579)

    def test_part_2(self):
        self.assertEqual(part_2([1_721, 979, 366, 299, 675, 1_456]), 241_861_950)


if __name__ == '__main__':
    unittest.main()
