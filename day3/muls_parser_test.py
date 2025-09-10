import unittest
from muls_parser import parser


class TestParser(unittest.TestCase):

    def test_parse(self):
        string = "from()why()?mul(603,692)({select()}] )]-(mul(387,685)who()mul(28,717)w"
        res = ['mul(603,692)', 'mul(387,685)', 'mul(28,717)']
        self.assertEqual(parser(string), res)


if __name__ == '__main__':
    unittest.main()
