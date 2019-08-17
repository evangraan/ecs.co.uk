import environment
import unittest
from shopping.discounts import *
from shopping.catalogue import *

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.catalogue = Catalogue("../orchestration/fixture/catalogue-full.json")
        self.catalogue.load()
        self.item = "Baked Beans"

    def test_buy_2_get_1_free(self):
        rule = "buy 2 get 1 free"
        self.assertEquals(self.__test_quantity(rule, 0), 0)
        self.assertEquals(self.__test_quantity(rule, 1), 0)
        self.assertEquals(self.__test_quantity(rule, 2), 0.99)
        self.assertEquals(self.__test_quantity(rule, 10), 4.95)
        self.assertEquals(self.__test_quantity(rule, 9), 3.96)

    def test_25_percent_discount(self):
        rule = "25% discount"
        self.assertEquals(self.__test_quantity(rule, 0), 0)
        self.assertEquals(self.__test_quantity(rule, 4), 0.99)

    def __test_quantity(self, rule, quantity):
        result = rules[rule](self.catalogue, self.item, quantity)
        return result["discount"]
if __name__ == '__main__':
    unittest.main()
