import unittest

from day_07 import parse_rule, part_1, part_2


class TestDay07(unittest.TestCase):
    def setUp(self):
        self._rules_1 = '''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.splitlines()
        self._rules_2 = '''
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.splitlines()

    def test_part_1(self):
        self.assertEqual(part_1(dict(map(parse_rule, self._rules_1))), 4)

    def test_part_2(self):
        self.assertEqual(part_2(dict(map(parse_rule, self._rules_1))), 32)
        self.assertEqual(part_2(dict(map(parse_rule, self._rules_2))), 126)


if __name__ == '__main__':
    unittest.main()
