import fileinput
import re
from functools import lru_cache

CONTENT_RE = re.compile('(\\d+) ([a-z]+ [a-z]+)')


def main():
    rules = dict(map(parse_rule, fileinput.input()))

    print(part_1(rules))
    print(part_2(rules))


def parse_rule(raw_rule: str) -> tuple[str, dict[str, int]]:
    container = ' '.join(raw_rule.split(maxsplit=2)[:2])
    content = {}

    # noinspection PyTypeChecker
    for content_count, content_color in map(re.Match.groups, CONTENT_RE.finditer(raw_rule)):
        content[content_color] = int(content_count)

    return container, content


def part_1(rules: dict[str, dict[str, int]]) -> int:
    @lru_cache(maxsize=None)
    def contains_shiny(container_color: str) -> bool:
        return any(True for content_color in rules[container_color]
                   if content_color == 'shiny gold' or contains_shiny(content_color))

    return sum(map(contains_shiny, rules))


def part_2(rules: dict[str, dict[str, int]]) -> int:
    def count_bags(container_color: str) -> int:
        return sum(content_count + content_count * count_bags(content_color)
                   for content_color, content_count in rules[container_color].items())

    return count_bags('shiny gold')


if __name__ == '__main__':
    main()
