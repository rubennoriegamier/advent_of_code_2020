import unittest

from day_02 import PolicyAndPassword


class TestDay02(unittest.TestCase):
    def test_parse(self):
        PolicyAndPassword.parse('1-3 a: abcde')

    def test_parse_with_invalid_pattern(self):
        with self.assertRaises(AttributeError):
            PolicyAndPassword.parse('1-3 a:abcde')

    def test_valid_1(self):
        self.assertTrue(PolicyAndPassword.parse('1-3 a: abcde').is_valid_1())
        self.assertTrue(PolicyAndPassword.parse('2-9 c: ccccccccc').is_valid_1())

    def test_invalid_1(self):
        self.assertFalse(PolicyAndPassword.parse('1-3 b: cdefg').is_valid_1())

    def test_valid_2(self):
        self.assertTrue(PolicyAndPassword.parse('1-3 a: abcde').is_valid_2())

    def test_invalid_2(self):
        self.assertFalse(PolicyAndPassword.parse('1-3 b: cdefg').is_valid_2())
        self.assertFalse(PolicyAndPassword.parse('2-9 c: ccccccccc').is_valid_2())


if __name__ == '__main__':
    unittest.main()
