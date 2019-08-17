import environment
import unittest
from shopping.basket import *
from shopping.catalogue import *
from shopping.offers import *

class TestBasket(unittest.TestCase):
    def setUp(self):
        self.iut = Basket()

    def test_empty_basket(self):
        self.__bootstrap("full", "full")
        self.iut.updateTotals(self.catalogue, self.offers)
        self.assertEqual(self.iut.getSubTotal(), 0)
        self.assertEqual(self.iut.getDiscount(), 0)
        self.assertEqual(self.iut.getTotal(), 0)

    def test_no_offers(self):
        self.__bootstrap("full", "none")
        self.iut.insert("Baked Beans", 3)
        self.iut.insert("Sardines", 5)
        self.iut.insert("Shampoo (Large)", 2)
        self.iut.updateTotals(self.catalogue, self.offers)
        self.assertEqual(self.iut.getSubTotal(), 19.42)
        self.assertEqual(self.iut.getDiscount(), 0)
        self.assertEqual(self.iut.getTotal(), 19.42)

    def test_one_offer(self):
        self.__bootstrap("full", "one")
        self.iut.insert("Baked Beans", 3)
        self.iut.insert("Sardines", 5)
        self.iut.insert("Shampoo (Large)", 2)
        self.iut.updateTotals(self.catalogue, self.offers)
        self.assertEqual(self.iut.getSubTotal(), 19.42)
        self.assertEqual(self.iut.getDiscount(), 2.36)
        self.assertEqual(self.iut.getTotal(), 17.06)

    def test_all_offers(self):
        self.__bootstrap("full", "full")
        self.iut.insert("Baked Beans", 7)
        self.iut.insert("Sardines", 5)
        self.iut.insert("Shampoo (Large)", 2)
        self.iut.updateTotals(self.catalogue, self.offers)
        self.assertEqual(self.iut.getSubTotal(), 23.38)
        self.assertEqual(self.iut.getDiscount(), 5.33)
        self.assertEqual(self.iut.getTotal(), 18.05)

    def test_best_offer(self):
        self.__bootstrap("full", "multiple")
        self.iut.insert("Baked Beans", 10)
        self.iut.updateTotals(self.catalogue, self.offers)
        self.assertEqual(self.iut.getSubTotal(), 9.90)
        self.assertEqual(self.iut.getDiscount(), 4.95)
        self.assertEqual(self.iut.getTotal(), 4.95)

    def test_insert(self):
        self.__bootstrap("full", "full")
        self.assertEqual(self.iut.size(), 0)
        self.iut.insert("Baked Beans", 10)
        self.assertEqual(self.iut.size(), 10)
        self.iut.insert("Sardines", 2)
        self.assertEqual(self.iut.size(), 12)

    def test_remove(self):
        self.__bootstrap("full", "full")
        self.iut.insert("Baked Beans", 10)
        self.assertEqual(self.iut.size(), 10)
        self.iut.remove("Baked Beans", 2)
        self.assertEqual(self.iut.size(), 8)
        self.iut.remove("Baked Beans", 8)
        self.assertEqual(self.iut.size(), 0)
        self.iut.remove("Baked Beans", 1)
        self.assertEqual(self.iut.size(), 0)
        self.iut.remove("Baked Beans", -1)
        self.assertEqual(self.iut.size(), 0)

    def test_clear(self):
        self.__bootstrap("full", "full")
        self.iut.insert("Baked Beans", 10)
        self.assertEqual(self.iut.size(), 10)
        self.iut.clear()
        self.assertEqual(self.iut.size(), 0)

    def test_lookup(self):
        self.__bootstrap("full", "full")
        self.iut.insert("Baked Beans", 10)
        self.assertEqual(self.iut.lookup("Sardines"), None)
        self.assertEqual(self.iut.lookup("Baked Beans"), 10)

    def __bootstrap(self, catalogueLabel, offersLabel):
        self.catalogue = Catalogue("../orchestration/fixture/catalogue-" + catalogueLabel + ".json")
        self.catalogue.load()
        self.offers = Offers("../orchestration/fixture/offers-" + offersLabel + ".json")
        self.offers.load()

if __name__ == '__main__':
    unittest.main()
