import unittest
from random import randint
from secrets import token_hex

from day_04 import HEIGHT_RE, HAIR_COLOR_RE, EYE_COLOR_RE, PASSPORT_ID_RE, parse_passports, part_1, part_2


class TestDay04(unittest.TestCase):
    def test_height_re(self):
        for cm in range(150, 194):
            self.assertIsNotNone(HEIGHT_RE.fullmatch(f'{cm}cm'))
        for inches in range(59, 77):
            self.assertIsNotNone(HEIGHT_RE.fullmatch(f'{inches}in'))

    def test_invalid_height_re(self):
        self.assertIsNone(HEIGHT_RE.fullmatch('149cm'))
        self.assertIsNone(HEIGHT_RE.fullmatch('194cm'))
        self.assertIsNone(HEIGHT_RE.fullmatch('170'))
        self.assertIsNone(HEIGHT_RE.fullmatch('58in'))
        self.assertIsNone(HEIGHT_RE.fullmatch('77in'))
        self.assertIsNone(HEIGHT_RE.fullmatch('65'))

    def test_hair_color_re(self):
        for _ in range(100):
            self.assertIsNotNone(HAIR_COLOR_RE.fullmatch(f'#{token_hex(3)}'))

    def test_invalid_hair_color_re(self):
        self.assertIsNone(HAIR_COLOR_RE.fullmatch('#123abz'))
        self.assertIsNone(HAIR_COLOR_RE.fullmatch('123abc'))
        self.assertIsNone(HAIR_COLOR_RE.fullmatch(f'#{token_hex(4)}'))

    def test_eye_color_re(self):
        for eye_color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            self.assertIsNotNone(EYE_COLOR_RE.fullmatch(eye_color))

    def test_invalid_eye_color_re(self):
        self.assertIsNone(EYE_COLOR_RE.fullmatch('wat'))
        self.assertIsNone(EYE_COLOR_RE.fullmatch('zzz'))

    def test_passport_id_re(self):
        for _ in range(100):
            self.assertIsNotNone(PASSPORT_ID_RE.fullmatch(f'{randint(0, 999_999_999):09}'))

    def test_invalid_passport_id_re(self):
        self.assertIsNone(PASSPORT_ID_RE.fullmatch('186cm'))
        self.assertIsNone(PASSPORT_ID_RE.fullmatch('0123456789'))
        self.assertIsNone(PASSPORT_ID_RE.fullmatch('3556412378'))

    def test_part_1(self):
        passports = parse_passports('''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''.lstrip())

        self.assertEqual(part_1(passports), 2)

    def test_part_2(self):
        passports = parse_passports('''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''.lstrip())

        self.assertEqual(part_2(passports), 4)


if __name__ == '__main__':
    unittest.main()
