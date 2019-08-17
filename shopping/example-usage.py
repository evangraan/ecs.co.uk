from basket import *
from catalogue import *
from offers import *

catalogue = Catalogue("../orchestration/fixture/catalogue-full.json")
catalogue.load()
offers = Offers("../orchestration/fixture/offers-full.json")
offers.load()
basket = Basket()

basket.insert("Baked Beans", 5)
basket.remove("Baked Beans", 3)
basket.insert("Sardines", 2)
basket.insert("Shampoo (Large)", 1)

basket.list(catalogue, offers)
