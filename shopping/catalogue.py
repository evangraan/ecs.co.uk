import json

class Catalogue:
    def __init__(self, path, notifier):
        self.path = path
        self.notifier = notifier
        self.load

    def isEmpty(self):
        return len(self.items) == 0

    def load(self):
        self.items = {}
        with open(self.path, 'r') as f:
            loaded = json.load(f)

        for item in loaded:
            price = loaded[item]
            try:
                float(price)
                self.items[item] = price
            except ValueError:
                self.notifier.notify("error loading some items")

        if self.isEmpty():
            self.notifier.notify("empty catalogue")
        else:
            self.notifier.notify("catalogue successfully loaded")

    def size(self):
        return len(self.items)

    def getItems(self):
        return self.items

    def lookup(self, name):
        if name in self.items:
            return self.items[name]
        return None
