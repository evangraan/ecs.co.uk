import json

class Basket:
    def __init__(self, catalogue, notifier):
        self.catalogue = catalogue
        self.notifier = notifier
        self.items = {}

    def insert(self, item, quantity):
        if item in self.items:
            self.items[item] = self.items[item] + quantity
        else:
            self.items[item] = quantity
        self.notifier.notify("item inserted")

    def remove(self, item, quantity):
        if item in self.items:
            self.items[item] = self.items[item] - quantity
            if self.items[item] <= 0:
                del self.items[item]
            self.notifier.notify("item removed")
        else:
            self.notifier.notify("item not in basket")

    def size(self):
        n = 0
        for item in self.items:
            n = n + int(self.items[item])
        return n

    def lookup(self, item):
        if item in self.items:
            return self.items[item]
        return None

    def clear(self):
        self.items = {}
