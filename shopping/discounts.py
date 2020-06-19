from utils import*

rules = {}

def buy2get1free(catalogue, item, n):
    return { "item" : item, "discount" : fixDecimal2Places(n // 2 * catalogue.lookup(item)) }

def pc25Discount(catalogue, item, n):
    return { "item" : item, "discount" : fixDecimal2Places(0.25 * catalogue.lookup(item) * n) }

def buyNofX(catalogue, basket, data):
    subset = [item for item in data["X"]]
    # Find all items in the basket that is in the rule item subset
    itemsFound = [item for item in basket.getItems() if item in subset]
    # Sort the found items by lowest price
    itemsFound = sorted(itemsFound, key=lambda item:catalogue.lookup(item))
    # Ask the basket what the total number of the found items in the basket is
    total = sum(basket.lookup(item) for item in itemsFound) 
    discount = 0
    # Give the customer free items, cheapest first, until the rule is satisfied
    freeRemaining = total // data["N"]
    while freeRemaining > 0:
      item = itemsFound.pop(0)
      if basket.lookup(item) >= freeRemaining:
          discount = discount + freeRemaining * catalogue.lookup(item)
          freeRemaining = 0
      else:
          discount = discount + basket.lookup(item) * catalogue.lookup(item)
          freeRemaining = freeRemaining - basket.lookup(item)

    return discount

def notFound():
    return { "item" : None, "discount" : None }

rules["buy 2 get 1 free"] = buy2get1free
rules["25% discount"] = pc25Discount
rules["Buy N of X, get the cheapest one for free"] = buyNofX
rules["not found"] = notFound 
