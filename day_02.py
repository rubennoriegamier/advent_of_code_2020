import fileinput
import re
from collections import Counter


class PolicyAndPassword:
    _PARSE_RE = re.compile('(\\d+)-(\\d+) ([a-z]): ([a-z]+)')

    __slots__ = '_n_1', '_n_2', '_char', '_password'

    def __init__(self, n_1, n_2, char, password):
        self._n_1 = n_1
        self._n_2 = n_2
        self._char = char
        self._password = password

    @classmethod
    def parse(cls, raw_policy_with_password):
        (n_1, n_2, char, password) = cls._PARSE_RE.fullmatch(raw_policy_with_password).groups()

        return cls(int(n_1), int(n_2), char, password)

    def is_valid_1(self):
        char_counter = Counter(self._password)

        return self._n_1 <= char_counter[self._char] <= self._n_2

    def is_valid_2(self):
        return (self._password[self._n_1 - 1] == self._char) != (self._password[self._n_2 - 1] == self._char)


def main():
    policies_with_passwords = list(map(PolicyAndPassword.parse, map(str.rstrip, fileinput.input())))

    print(sum(map(PolicyAndPassword.is_valid_1, policies_with_passwords)))
    print(sum(map(PolicyAndPassword.is_valid_2, policies_with_passwords)))


if __name__ == '__main__':
    main()
