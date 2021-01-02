import unittest

from day_24 import parse_instructions, part_1, part_2


class TestDay24(unittest.TestCase):
    def setUp(self):
        self._instruction_list = list(map(parse_instructions, ['sesenwnenenewseeswwswswwnenewsewsw',
                                                               'neeenesenwnwwswnenewnwwsewnenwseswesw',
                                                               'seswneswswsenwwnwse',
                                                               'nwnwneseeswswnenewneswwnewseswneseene',
                                                               'swweswneswnenwsewnwneneseenw',
                                                               'eesenwseswswnenwswnwnwsewwnwsene',
                                                               'sewnenenenesenwsewnenwwwse',
                                                               'wenwwweseeeweswwwnwwe',
                                                               'wsweesenenewnwwnwsenewsenwwsesesenwne',
                                                               'neeswseenwwswnwswswnw',
                                                               'nenwswwsewswnenenewsenwsenwnesesenew',
                                                               'enewnwewneswsewnwswenweswnenwsenwsw',
                                                               'sweneswneswneneenwnewenewwneswswnese',
                                                               'swwesenesewenwneswnwwneseswwne',
                                                               'enesenwswwswneneswsenwnewswseenwsese',
                                                               'wnwnesenesenenwwnenwsewesewsesesew',
                                                               'nenewswnwewswnenesenwnesewesw',
                                                               'eneswnwswnwsenenwnwnwwseeswneewsenese',
                                                               'neswnwewnwnwseenwseesewsenwsweewe',
                                                               'wseweeenwnesenwwwswnew']))

    def test_part_1(self):
        self.assertEqual(part_1(self._instruction_list), 10)

    def test_part_2(self):
        self.assertEqual(part_2(self._instruction_list, 100), 2_208)


if __name__ == '__main__':
    unittest.main()
