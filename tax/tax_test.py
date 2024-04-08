import unittest
from tax import Tax

class TestTax(unittest.TestCase):

    def test_0(self):
        t = Tax()
        income = 0; expectedTax = 0;
        self.assertEqual(t.tax(income), expectedTax)

    def test_50000(self):
        t = Tax()
        income = 50000; expectedTax = 0
        self.assertEqual(t.tax(income), expectedTax)

    def test_150000(self):
        t = Tax()
        income = 150000; expectedTax = 2500
        self.assertEqual(t.tax(income), expectedTax)

    def test_250000(self):
        t = Tax()
        income = 250000; expectedTax = 7500
        self.assertEqual(t.tax(income), expectedTax)

    def test_250001(self):
        t = Tax()
        income = 250001; expectedTax = 7500.10
        self.assertEqual(t.tax(income), expectedTax)

    def test_500000(self):
        t = Tax()
        income = 500000; expectedTax = 32500
        self.assertEqual(t.tax(income), expectedTax)

    def test_1000000(self):
        t = Tax()
        income = 1000000; expectedTax = 82500
        self.assertEqual(t.tax(income), expectedTax)

    def test_1000001(self):
        t = Tax()
        income = 1000001; expectedTax = 82500.20
        self.assertEqual(t.tax(income), expectedTax)

    def test_2000000(self):
        t = Tax()
        income = 2000000; expectedTax = 282500
        self.assertEqual(t.tax(income), expectedTax)

    def test_neg1(self):
        t = Tax()
        self.assertRaises(ValueError, t.tax, -1)

    def test_string(self):
        t = Tax()
        self.assertRaises(TypeError, t.tax, '12000')

    def test_complex(self):
        t = Tax()
        self.assertRaises(TypeError, t.tax, (12+2j))
