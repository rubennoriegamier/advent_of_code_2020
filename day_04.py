import re
from functools import partial
from sys import stdin

HEIGHT_RE = re.compile('1(?:[5-8]\\d|9[0-3])cm|(?:59|6\\d|7[0-6])in')
HAIR_COLOR_RE = re.compile('#[0-9a-f]{6}')
EYE_COLOR_RE = re.compile('amb|blu|brn|gry|grn|hzl|oth')
PASSPORT_ID_RE = re.compile('\\d{9}')


def main():
    passports = parse_passports(stdin.read().rstrip())

    print(part_1(passports))
    print(part_2(passports))


def part_1(passports):
    return sum(1 for passport in passports if len(passport) == 8 or len(passport) == 7 and 'cid' not in passport)


def part_2(passports):
    return sum(1 for passport in passports if
               (len(passport) == 8 or len(passport) == 7 and 'cid' not in passport) and
               1920 <= int(passport['byr']) <= 2002 and
               2010 <= int(passport['iyr']) <= 2020 <= int(passport['eyr']) <= 2030 and
               HEIGHT_RE.fullmatch(passport['hgt']) and
               HAIR_COLOR_RE.fullmatch(passport['hcl']) and
               EYE_COLOR_RE.fullmatch(passport['ecl']) and
               PASSPORT_ID_RE.fullmatch(passport['pid']))


def parse_passports(raw_passports):
    # 'ecl:amb byr:1943 iyr:2014 eyr:2028\npid:333051831'
    passports = raw_passports.split('\n\n')

    # ['ecl:amb', 'byr:1943', 'iyr:2014', 'eyr:2028', 'pid:333051831']
    passports = map(re.compile('\\s').split, passports)

    # {'ecl': 'amb', 'byr': '1943', 'iyr': '2014', 'eyr': '2028', 'pid': '333051831'}
    # noinspection PyTypeChecker
    return list(map(dict, map(partial(map, partial(str.split, sep=':')), passports)))


if __name__ == '__main__':
    main()
