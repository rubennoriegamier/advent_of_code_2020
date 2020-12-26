import unittest

from day_16 import Rule, parse_ticket, part_1, part_2


class TestDay16(unittest.TestCase):
    def test_part_1(self):
        raw_rules, _, raw_nearby_tickets = '''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.lstrip().split('\n\n')
        rules = list(map(Rule.parse, raw_rules.splitlines()))
        nearby_tickets = list(map(parse_ticket, raw_nearby_tickets.splitlines()[1:]))

        self.assertEqual(part_1(rules, nearby_tickets), 71)

    def test_part_2(self):
        raw_rules, raw_my_ticket, raw_nearby_tickets = '''
departure class: 0-1 or 4-19
departure row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''.lstrip().split('\n\n')
        rules = list(map(Rule.parse, raw_rules.splitlines()))
        my_ticket = parse_ticket(raw_my_ticket.splitlines()[-1])
        nearby_tickets = list(map(parse_ticket, raw_nearby_tickets.splitlines()[1:]))

        self.assertEqual(part_2(rules, my_ticket, nearby_tickets), 11 * 12 * 13)


if __name__ == '__main__':
    unittest.main()
