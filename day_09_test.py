import unittest

from day_09 import part_1, part_2


class TestDay09(unittest.TestCase):
    def setUp(self):
        self._data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

    def test_part_1(self):
        self.assertEqual(part_1(self._data, 5), 127)

    def test_part_2(self):
        self.assertEqual(part_2(self._data, 5), 62)


if __name__ == '__main__':
    unittest.main()
