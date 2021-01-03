import unittest

from day_25 import part_1


class TestDay25(unittest.TestCase):
    def setUp(self):
        self._card_public_key = 5_764_801
        self._door_public_key = 17_807_724

    def test_part_1(self):
        self.assertEqual(part_1(self._card_public_key, self._door_public_key), 14_897_079)


if __name__ == '__main__':
    unittest.main()
