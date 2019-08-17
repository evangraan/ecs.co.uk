import json
from notifier import *
from utils import *

class Basket:
    def __init__(self, notifier = DefaultNotifier()):
        self.notifier = notifier
        self.items = {}

    def updateTotals(self, catalogue, offers):
        self.subTotal = self.__calculateSubTotal(catalogue)
        self.discount = self.__calculateDiscount(catalogue, offers)
        self.total = self.subTotal - self.discount

    def getSubTotal(self):
        return fixDecimal2Places(self.subTotal)

    def getDiscount(self):
        return fixDecimal2Places(self.discount)

    def getTotal(self):
        return fixDecimal2Places(self.total)

    def list(self, catalogue, offers):
        self.updateTotals(catalogue, offers)
        self.__listContents(catalogue)
        self.__listTotals()

    def lookup(self, item):
        if item in self.items:
            return int(self.items[item])
        return None

    def size(self):
        return sum(self.lookup(item) for item in self.items)

    def getItems(self):
        return self.items

    def clear(self):
        self.items = {}

    def insert(self, item, quantity = 1):
        self.items[item] = self.items[item] + quantity if item in self.items else quantity
        self.notifier.notify("item inserted")

    def remove(self, item, quantity = 1):
        if item in self.items:
            self.__removeItem(item, quantity)
            self.notifier.notify("item removed")
        else:
            self.notifier.notify("item not in basket")

    def __calculateDiscount(self, catalogue, offers):
        discounts = offers.calculateBestDiscount(catalogue, self)
        return sum(discounts[discount]['discount'] for discount in discounts)

    def __calculateSubTotal(self, catalogue):
        return sum(self.items[item] * catalogue.lookup(item) for item in self.items)

    def __listContents(self, catalogue):
        self.notifier.notify("number of items: " + str(self.size()))
        for item in self.items:
            self.notifier.notify(item + " : " + str(self.items[item]) + " @ " + str(catalogue.lookup(item)))
        if self.size() == 0:
            self.notifier.notify("No items")

    def __listTotals(self):
        self.notifier.notify("sub-total: " + u"\xA3" + f'{self.subTotal:.2f}')
        self.notifier.notify("discount: " + u"\xA3" + f'{self.discount:.2f}')
        self.notifier.notify("total: " + u"\xA3" + f'{self.total:.2f}')

    def __removeItem(self, item, quantity):
        self.items[item] = self.items[item] - quantity
        if self.items[item] <= 0:
            del self.items[item]
        self.notifier.notify("item removed")


