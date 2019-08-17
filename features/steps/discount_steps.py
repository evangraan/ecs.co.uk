@then('the discount for the basket is listed in pounds')
def step_impl(context):
    assert context.notifier.contains(u"\xA3") == True

@then('the discount is 0.00')
def step_impl(context):
    assert context.basket.getDiscount() == 0
    assert context.notifier.contains("discount: " + u"\xA3" + "0.00")

@given('no offers match the items')
def step_impl(context):
    context.orchestrator.seedOffers("none")
    context.offers.load()

@then('the discount is the correct discount amount for the offer that matches')
def step_impl(context):
    assert context.basket.getDiscount() == 0.47
    assert context.notifier.contains("discount: " + u"\xA3" + "0.47")

@given('an offer matches the other item')
def step_impl(context):
    context.orchestrator.seedOffers("full")
    context.offers.load()

@then('the discount is the sum of the correct discounts for both offers that match')
def step_impl(context):
    assert context.basket.getDiscount() == 0.47
    assert context.notifier.contains("discount: " + u"\xA3" + "0.47")

@given('a third offer matches the same item')
def step_impl(context):
    context.orchestrator.seedOffers("multiple")
    context.offers.load()

@then('the discount is the correct discount amount for the offer that matches with lowest resulting cost for the basket as a whole')
def step_impl(context):
    assert context.basket.getDiscount() == -1
    assert context.notifier.contains("discount: " + u"\xA3" + "-1")

@given('the second offer also matches the other item')
def step_impl(context):
    context.orchestrator.secondOffers()
    context.offers.load()

@given('the third offer also matches the other item')
def step_impl(context):
    context.orchestrator.thirdOffers()
    context.offers.load()

@then('the discount is accurate to 2 decimal places')
def step_impl(context):
    assert context.basket.getSubTotal() == 2.88
    assert context.notifier.contains("sub-total: " + u"\xA3" + "2.88")

@given('an offer matches one of the items')
def step_impl(context):
    context.orchestrator.seedOffers("one")
    context.offers.load()

@given('a second offer matches the same item')
def step_impl(context):
    context.orchestrator.seedOffers("multiple")
    context.offers.load()
