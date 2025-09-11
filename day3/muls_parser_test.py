import unittest
from muls_parser import parser, extract_nums_from


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

    def test_calc_prod(self):
        ...


if __name__ == '__main__':
    unittest.main()
