import unittest

from day_13 import part_1, part_2


class TestDay13(unittest.TestCase):
    def test_part_1(self):
        ids = ['7', '13', 'x', 'x', '59', 'x', '31', '19']
        self.assertEqual(part_1(939, ids), 295)

    def test_part_2_without_gaps(self):
        self.assertEqual(part_2(['67', '7', '59', '61']), 754_018)
        self.assertEqual(part_2(['1789', '37', '47', '1889']), 1_202_161_486)

    def test_part_2_with_gaps(self):
        self.assertEqual(part_2(['17', 'x', '13', '19']), 3_417)
        self.assertEqual(part_2(['67', 'x', '7', '59', '61']), 779_210)
        self.assertEqual(part_2(['67', '7', 'x', '59', '61']), 1_261_476)


if __name__ == '__main__':
    unittest.main()
