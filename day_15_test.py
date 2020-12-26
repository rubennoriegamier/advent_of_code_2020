import unittest

from day_15 import part_1, part_2


class TestDay15(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1([0, 3, 6]), 436)
        self.assertEqual(part_1([1, 3, 2]), 1)
        self.assertEqual(part_1([2, 1, 3]), 10)
        self.assertEqual(part_1([1, 2, 3]), 27)
        self.assertEqual(part_1([2, 3, 1]), 78)
        self.assertEqual(part_1([3, 2, 1]), 438)
        self.assertEqual(part_1([3, 1, 2]), 1_836)

    def test_part_2(self):
        self.assertEqual(part_2([0, 3, 6]), 175_594)
        self.assertEqual(part_2([1, 3, 2]), 2_578)
        self.assertEqual(part_2([2, 1, 3]), 3_544_142)
        self.assertEqual(part_2([1, 2, 3]), 261_214)
        self.assertEqual(part_2([2, 3, 1]), 6_895_259)
        self.assertEqual(part_2([3, 2, 1]), 18)
        self.assertEqual(part_2([3, 1, 2]), 362)


if __name__ == '__main__':
    unittest.main()
