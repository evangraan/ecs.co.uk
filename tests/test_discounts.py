import environment
import unittest
from shopping.discounts import *
from shopping.catalogue import *
from shopping.basket import *

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.catalogue = Catalogue("../orchestration/fixture/catalogue-full.json")
        self.catalogue.load()
        self.item = "Baked Beans"

    def test_buy_2_get_1_free(self):
        rule = "buy 2 get 1 free"
        self.assertEqual(self.__test_quantity(rule, 0), 0)
        self.assertEqual(self.__test_quantity(rule, 1), 0)
        self.assertEqual(self.__test_quantity(rule, 2), 0.99)
        self.assertEqual(self.__test_quantity(rule, 10), 4.95)
        self.assertEqual(self.__test_quantity(rule, 9), 3.96)

    def test_25_percent_discount(self):
        rule = "25% discount"
        self.assertEqual(self.__test_quantity(rule, 0), 0)
        self.assertEqual(self.__test_quantity(rule, 4), 0.99)

    def test_buy_3_of_biscuits_shampoo(self):
        rule = "Buy N of X, get the cheapest one for free"
        data = json.loads("{ \"N\" : 3, \"X\" : [ \"Shampoo (Medium)\", \"Shampoo (Large)\", \"Shampoo (Small)\", \"Biscuits\" ] }")
        basket = Basket()
        basket.insert("Baked Beans", 2)
        basket.insert("Biscuits", 2)
        basket.insert("Shampoo (Small)", 2)
        result = rules[rule](self.catalogue, basket, data)
        self.assertEqual(result, 1.2)

    def test_buy_3_of_biscuits_shampoo_multiple(self):
        rule = "Buy N of X, get the cheapest one for free"
        data = json.loads("{ \"N\" : 3, \"X\" : [ \"Shampoo (Medium)\", \"Shampoo (Large)\", \"Shampoo (Small)\", \"Biscuits\" ] }")
        basket = Basket()
        basket.insert("Baked Beans", 3)
        basket.insert("Biscuits", 2)
        basket.insert("Shampoo (Small)", 5)
        result = rules[rule](self.catalogue, basket, data)
        self.assertEqual(result, 2.4)

    def __test_quantity(self, rule, quantity):
        result = rules[rule](self.catalogue, self.item, quantity)
        return result["discount"]
    
if __name__ == '__main__':
    unittest.main()
