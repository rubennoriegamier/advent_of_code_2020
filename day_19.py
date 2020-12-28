import fileinput
from functools import lru_cache, partial
from itertools import chain

import regex as re


def main():
    # noinspection PyTypeChecker
    raw_rules, messages = map(str.splitlines, ''.join(fileinput.input()).split('\n\n'))
    rules = parse_rules(raw_rules)

    print(part_1(rules, messages))
    print(part_2(rules, messages))


def parse_rules(raw_rules):
    rules = {}

    for raw_rule in raw_rules:
        n, rule = raw_rule.split(': ')

        if rule.startswith('"'):
            rules[int(n)] = rule[1]
        else:
            rules[int(n)] = tuple(map(tuple, map(partial(map, int), map(str.split, rule.split(' | ')))))

    return rules


def get_zero_re(rules):
    @lru_cache(maxsize=None)
    def get_pattern(n):
        rule = rules[n]

        if isinstance(rule, str):
            return rule
        if len(rule) == 1:
            return ''.join(map(get_pattern, rule[0]))
        if n in set(chain.from_iterable(rule)):
            group_name = f'_{n}'
            ors = '|'.join(''.join(f'(?P&{group_name})' if sub_rule == n else get_pattern(sub_rule)
                                   for sub_rule in sub_rules) for sub_rules in rule)

            return f"(?<{group_name}>{ors})"
        return f"(?:{'|'.join(''.join(map(get_pattern, sub_rules)) for sub_rules in rule)})"

    return re.compile(get_pattern(0))


def part_1(rules, messages):
    return sum(1 for _ in filter(get_zero_re(rules).fullmatch, messages))


def part_2(rules, messages):
    rules = rules.copy()
    rules[8] = ((42,), (42, 8))
    rules[11] = ((42, 31), (42, 11, 31))

    return sum(1 for _ in filter(get_zero_re(rules).fullmatch, messages))


if __name__ == '__main__':
    main()
