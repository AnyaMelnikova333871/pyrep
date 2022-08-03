from unittest import TestCase
from calculater import calc_plus, calc_minus, calc_del, calc_mnozh, calc_get, calc_square, calc_sqrt, calc_sin, calc_cos, calc_tg, calc_ctg

class CalcTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc_plus(2, 3), 5)

    def test_minus(self):
        self.assertEqual(calc_minus(3, 2), 1)

    def test_del(self):
        self.assertEqual(calc_del(4, 2), 2)

    def test_mnozh(self):
        self.assertEqual(calc_mnozh(3, 2), 6)

    def test_get(self):
        self.assertEqual(calc_get(3, 2), 9)

    def test_square(self):
        self.assertEqual(calc_square(4), 16)

    def test_sqrt(self):
        self.assertEqual(calc_sqrt(4), 2)

    def test_sin(self):
        self.assertEqual(calc_sin(30), 0.5)

    def test_cos(self):
        self.assertEqual(calc_cos(60), 0.5)

    def test_tg(self):
        self.assertEqual(calc_tg(45), 1)

    def test_ctg(self):
        self.assertEqual(calc_ctg(45), 1)

CalcTest()