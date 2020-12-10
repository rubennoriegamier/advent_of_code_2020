import unittest

from day_10 import part_1, part_2


class TestDay10(unittest.TestCase):
    def setUp(self):
        self._sample_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self._sample_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                          38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

    def test_part_1(self):
        self.assertEqual(part_1(self._sample_1), 7 * 5)
        self.assertEqual(part_1(self._sample_2), 22 * 10)

    def test_part_2(self):
        self.assertEqual(part_2(self._sample_1), 8)
        self.assertEqual(part_2(self._sample_2), 19_208)


if __name__ == '__main__':
    unittest.main()
