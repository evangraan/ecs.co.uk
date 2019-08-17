import json
from discounts import rules
from notifier import *

class Offers:
    def __init__(self, path, notifier = DefaultNotifier()):
        self.path = path
        self.notifier = notifier
        self.load

    def calculateBestDiscount(self, catalogue, basket):
        discounts = {}
        for offer in self.offers:
            discounts = self.__mergeBestDiscountForThisOffer(catalogue, offer, basket, discounts)
        return discounts

    def load(self):
        with open(self.path, 'r') as f:
            self.offers = json.load(f)
        self.__notifyLoaded()

    def size(self):
        return len(self.offers)

    def getOffers(self):
        return self.offers

    def isEmpty(self):
        return len(self.offers) == 0

    def __mergeBestDiscountForThisOffer(self, catalogue, offer, basket, discounts):
        discount = self.__calculateDiscount(catalogue, offer, self.offers[offer], basket)
        if discount["item"] != None:
            discounts = self.__mergeDiscountIfBetterOrMissing(discount, discounts)
        return discounts

    def __mergeDiscountIfBetterOrMissing(self, discount, discounts):
        if discount["item"] in discounts:
            discounts = __mergeDiscountIfBetter(discounts, discount)
        else:
            discounts[discount["item"]] = discount
        return discounts

    def __mergeDiscountIfBetter(self, discounts, discount):
        if discount["discount"] > discounts[discount["item"]]:
            discounts[discount["item"]] = discount["discount"]
        return discounts

    def __calculateDiscount(self, catalogue, offer, rule, basket):
        for item in basket.getItems():
            if item == offer and rule in rules:
                return rules[rule](catalogue, item, basket.getItems()[item])

        return rules["not found"]()

    def __notifyLoaded(self):
        if self.isEmpty():
            self.notifier.notify("no offers")
        else:
            self.notifier.notify("offers successfully loaded")
