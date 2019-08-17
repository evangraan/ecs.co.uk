import json
from notifier import *

class Catalogue:
    def __init__(self, path, notifier = DefaultNotifier()):
        self.path = path
        self.notifier = notifier
        self.load

    def isEmpty(self):
        return len(self.items) == 0

    def load(self):
        self.items = {}
        self.__addValidItems(self.__loadItems())
        self.__notifyLoaded()

    def lookup(self, item):
        if item in self.items:
            return self.items[item]
        return None

    def size(self):
        return len(self.items)

    def getItems(self):
        return self.items

    def __loadItems(self):
        with open(self.path, 'r') as f:
            loaded = json.load(f)
        return loaded

    def __addValidItems(self, loaded):
        for item in loaded:
            price = loaded[item]
            try:
                float(price)
                self.items[item] = price
            except ValueError:
                self.notifier.notify("error loading some items")

    def __notifyLoaded(self):
        if self.isEmpty():
            self.notifier.notify("empty catalogue")
        else:
            self.notifier.notify("catalogue successfully loaded")

