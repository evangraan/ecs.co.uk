from utils import*

rules = {}

def buy2get1free(catalogue, item, n):
    return { "item" : item, "discount" : fixDecimal2Places(n // 2 * catalogue.lookup(item)) }

def pc25Discount(catalogue, item, n):
    return { "item" : item, "discount" : fixDecimal2Places(0.25 * catalogue.lookup(item) * n) }

def notFound():
    return { "item" : None, "discount" : None }

rules["buy 2 get 1 free"] = buy2get1free
rules["25% discount"] = pc25Discount
rules["not found"] = notFound

