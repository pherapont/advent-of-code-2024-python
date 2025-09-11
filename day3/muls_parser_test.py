import unittest
from muls_parser import parser, extract_nums_from, calc_prod, get_chanks


class TestParser(unittest.TestCase):

    def test_parse(self):
        string = "from()why()?mul(603,692)({select()}] )]-(mul(387,685)who()mul(28,717)w"
        res = ['mul(603,692)', 'mul(387,685)', 'mul(28,717)']
        self.assertEqual(parser(string), res)

    def test_extract_2digit_nums(self):
        data = "mul(22,43)"
        res = [22, 43]
        self.assertEqual(extract_nums_from(data), res)

    def test_extract_1and3_digit_nums(self):
        data = "mul(5,294)"
        res = [5, 294]
        self.assertEqual(extract_nums_from(data), res)

    def test_calc_simple_prod(self):
        data = [[1, 2], [3, 4], [10, 5]]
        sum_prod = 64
        self.assertEqual(calc_prod(data), sum_prod)

    def test_calc_large_numbers_prod(self):
        data = [[234569, 85432], [222222, 444444], [10000000, 55858585]]
        sum_prod = 558704654933376
        self.assertEqual(calc_prod(data), sum_prod)

    def test_get_chanks(self):
        data = "[?mul(813,364)?whydon't()<,'mul(942, 587){howdo()mul(704,164)#$select"
        res = "[?mul(813,364)?whymul(704,164)#$select"
        self.assertEqual(get_chanks(data), res)


if __name__ == '__main__':
    unittest.main()
