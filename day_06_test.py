import unittest

from day_06 import parse_groups, part_1, part_2


class TestDay06(unittest.TestCase):
    def setUp(self):
        self._raw_groups = '''
abc

a
b
c

ab
ac

a
a
a
a

b'''.lstrip()

    def test_part_1(self):
        self.assertEqual(part_1(parse_groups(self._raw_groups)), 11)

    def test_part_2(self):
        self.assertEqual(part_2(parse_groups(self._raw_groups)), 6)


if __name__ == '__main__':
    unittest.main()
