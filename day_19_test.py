import unittest

from day_19 import parse_rules, part_1, part_2


class TestDay19(unittest.TestCase):
    def test_part_1(self):
        rules = parse_rules(['0: 4 1 5',
                             '1: 2 3 | 3 2',
                             '2: 4 4 | 5 5',
                             '3: 4 5 | 5 4',
                             '4: "a"',
                             '5: "b"'])
        messages = ['ababbb',
                    'bababa',
                    'abbbab',
                    'aaabbb',
                    'aaaabbb']

        self.assertEqual(part_1(rules, messages), 2)

    def test_part_2(self):
        rules = parse_rules(['42: 9 14 | 10 1',
                             '9: 14 27 | 1 26',
                             '10: 23 14 | 28 1',
                             '1: "a"',
                             '11: 42 31',
                             '5: 1 14 | 15 1',
                             '19: 14 1 | 14 14',
                             '12: 24 14 | 19 1',
                             '16: 15 1 | 14 14',
                             '31: 14 17 | 1 13',
                             '6: 14 14 | 1 14',
                             '2: 1 24 | 14 4',
                             '0: 8 11',
                             '13: 14 3 | 1 12',
                             '15: 1 | 14',
                             '17: 14 2 | 1 7',
                             '23: 25 1 | 22 14',
                             '28: 16 1',
                             '4: 1 1',
                             '20: 14 14 | 1 15',
                             '3: 5 14 | 16 1',
                             '27: 1 6 | 14 18',
                             '14: "b"',
                             '21: 14 1 | 1 14',
                             '25: 1 1 | 1 14',
                             '22: 14 14',
                             '8: 42',
                             '26: 14 22 | 1 20',
                             '18: 15 15',
                             '7: 14 5 | 1 21',
                             '24: 14 1'])
        messages = ['abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
                    'bbabbbbaabaabba',
                    'babbbbaabbbbbabbbbbbaabaaabaaa',
                    'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
                    'bbbbbbbaaaabbbbaaabbabaaa',
                    'bbbababbbbaaaaaaaabbababaaababaabab',
                    'ababaaaaaabaaab',
                    'ababaaaaabbbaba',
                    'baabbaaaabbaaaababbaababb',
                    'abbbbabbbbaaaababbbbbbaaaababb',
                    'aaaaabbaabaaaaababaa',
                    'aaaabbaaaabbaaa',
                    'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
                    'babaaabbbaaabaababbaabababaaab',
                    'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba']

        self.assertEqual(part_2(rules, messages), 12)


if __name__ == '__main__':
    unittest.main()
