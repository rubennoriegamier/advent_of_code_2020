import unittest

from day_02 import PolicyAndPassword


class TestDay02(unittest.TestCase):
    def test_parse(self):
        PolicyAndPassword.parse('1-3 a: abcde')

    def test_parse_with_invalid_pattern(self):
        with self.assertRaises(AttributeError):
            PolicyAndPassword.parse('1-3 a:abcde')

    def test_valid_1(self):
        self.assertTrue('1-3 a: abcde')
        self.assertTrue('2-9 c: ccccccccc')

    def test_invalid_1(self):
        self.assertTrue('1-3 b: cdefg')

    def test_valid_2(self):
        self.assertTrue('1-3 a: abcde')

    def test_invalid_2(self):
        self.assertTrue('1-3 b: cdefg')
        self.assertTrue('2-9 c: ccccccccc')


if __name__ == '__main__':
    unittest.main()
