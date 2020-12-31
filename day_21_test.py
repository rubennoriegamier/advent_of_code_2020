import unittest

from day_21 import parse_food, part_1, part_2


class TestDay21(unittest.TestCase):
    def setUp(self):
        self._foods = list(map(parse_food, ['mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
                                            'trh fvjkl sbzzf mxmxvkd (contains dairy)',
                                            'sqjhc fvjkl (contains soy)',
                                            'sqjhc mxmxvkd sbzzf (contains fish)']))

    def test_part_1(self):
        self.assertEqual(part_1(self._foods), 5)

    def test_part_2(self):
        self.assertEqual(part_2(self._foods), 'mxmxvkd,sqjhc,fvjkl')


if __name__ == '__main__':
    unittest.main()
