import fileinput
from functools import partial, reduce
from itertools import chain
from operator import mul


def main():
    raw_rules, raw_my_ticket, raw_nearby_tickets = ''.join(fileinput.input()).split('\n\n')
    rules = list(map(Rule.parse, raw_rules.splitlines()))
    my_ticket = parse_ticket(raw_my_ticket.splitlines()[-1])
    nearby_tickets = list(map(parse_ticket, raw_nearby_tickets.splitlines()[1:]))

    print(part_1(rules, nearby_tickets))
    print(part_2(rules, my_ticket, nearby_tickets))


class Rule:
    def __init__(self, name, range_1, range_2):
        self._name = name
        self._range_1 = range_1
        self._range_2 = range_2

    @classmethod
    def parse(cls, raw_rule):
        name, ranges = raw_rule.split(':')
        raw_range_1, raw_range_2 = ranges.split(' or ')
        raw_range_start_1, raw_range_stop_1 = raw_range_1.split('-')
        raw_range_start_2, raw_range_stop_2 = raw_range_2.split('-')
        range_1 = range(int(raw_range_start_1), int(raw_range_stop_1) + 1)
        range_2 = range(int(raw_range_start_2), int(raw_range_stop_2) + 1)

        return cls(name, range_1, range_2)

    @property
    def name(self):
        return self._name

    def is_valid(self, value):
        return value in self._range_1 or value in self._range_2


def parse_ticket(raw_ticket):
    return list(map(int, raw_ticket.split(',')))


def invalid_values(rules, ticket):
    for value in ticket:
        for rule in rules:
            if rule.is_valid(value):
                break
        else:
            yield value


def part_1(rules, nearby_tickets):
    return sum(chain.from_iterable(map(partial(invalid_values, rules), nearby_tickets)))


def candidate_rules(rules, values):
    for rule in rules:
        for value in values:
            if not rule.is_valid(value):
                break
        else:
            yield rule.name


def part_2(rules, my_ticket, nearby_tickets):
    tickets = [ticket for ticket in [my_ticket] + nearby_tickets if next(invalid_values(rules, ticket), None) is None]
    candidates = list(map(set, map(partial(candidate_rules, rules), zip(*tickets))))
    indices = set(range(len(rules)))

    while indices:
        for i in indices:
            if len(candidates[i]) == 1:
                candidates[i] = candidates[i].pop()
                indices.remove(i)
                for j in indices:
                    candidates[j].discard(candidates[i])
                break

    return reduce(mul, (value for value, field in zip(my_ticket, candidates) if field.startswith('departure')))


if __name__ == '__main__':
    main()
