@given('the basket has 2 of the same item in it')
def step_impl(context):
    context.item = "Baked Beans"
    context.basket.insert(context.item, 2)

@given('I have a "buy 2 get 1 free" offer for the item')
def step_impl(context):
    context.orchestrator.seedOffers("full")
    context.offers.load()

@then('the discount is equal to the price of matching item')
def step_impl(context):
    assert context.basket.getDiscount() == 0.99
    assert context.notifier.contains("discount: " + u"\xA3" + "0.99")

@given('the basket has an item in it')
def step_impl(context):
    context.item = "Sardines"
    context.basket.insert(context.item, 1)

@given('I have a "% discount" offer for the item')
def step_impl(context):
    context.orchestrator.seedOffers("full")
    context.offers.load()

@then('the discount is equal to the specified percentage of the price of matching item')
def step_impl(context):
    assert context.basket.getDiscount() == 0.47
    assert context.notifier.contains("discount: " + u"\xA3" + "0.47")
