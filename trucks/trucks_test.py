import unittest
from trucks import Trucks

class TestTax(unittest.TestCase):
    t = Trucks()

    def test_40(self):
        orders = 40
        self.assertListEqual(self.t.spread(orders), [40])

    def test_41(self):
        orders = 41
        self.assertListEqual(self.t.spread(orders), [21, 20])

    def test_63(self):
        orders = 63
        self.assertListEqual(self.t.spread(orders), [32, 31])

    def test_80(self):
        orders = 80
        self.assertListEqual(self.t.spread(orders), [40, 40])

    def test_82(self):
        orders = 82
        self.assertListEqual(self.t.spread(orders), [28, 27, 27])

    def test_100(self):
        orders = 100
        self.assertListEqual(self.t.spread(orders), [34, 33, 33])

    def test_119(self):
        orders = 119
        self.assertListEqual(self.t.spread(orders), [40, 40, 39])

    def test_120(self):
        orders = 120
        self.assertListEqual(self.t.spread(orders), [40, 40, 40])

    def test_121(self):
        orders = 121
        self.assertListEqual(self.t.spread(orders), [31, 30, 30, 30])

    def test_250(self):
        orders = 250
        self.assertListEqual(self.t.spread(orders), [36, 36, 36, 36, 36, 35, 35])

    def test_253(self):
        orders = 253
        self.assertListEqual(self.t.spread(orders), [37, 36, 36, 36, 36, 36, 36])

    def test_280(self):
        orders = 280
        self.assertListEqual(self.t.spread(orders), [40, 40, 40, 40, 40, 40, 40])

    def test_281(self):
        orders = 281
        self.assertListEqual(self.t.spread(orders), [36, 35, 35, 35, 35, 35, 35, 35])

    def test_500(self):
        orders = 500
        self.assertListEqual(self.t.spread(orders), [39, 39, 39, 39, 39, 39, 38, 38, 38, 38, 38, 38, 38])

    def test_800(self):
        orders = 800
        self.assertListEqual(self.t.spread(orders), [40] * 20)

    def test_1000(self):
        orders = 1000
        self.assertListEqual(self.t.spread(orders), [40] * 25)