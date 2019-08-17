@when('I list the items in the basket')
def step_impl(context):
    context.basket.list(context.catalogue, context.offers)

@then('the sub-total for the basket is listed in pounds')
def step_impl(context):
    assert context.notifier.contains(u"\xA3") == True

@then('the sub-total is 0.00')
def step_impl(context):
    assert context.basket.getSubTotal() == 0
    assert context.notifier.contains("sub-total: " + u"\xA3" + "0.00")

@then('the sub-total is the sum of the base prices of both items')
def step_impl(context):
    assert context.basket.getSubTotal() == 2.88
    assert context.notifier.contains("sub-total: " + u"\xA3" + "2.88")

@then('the sub-total is accurate to 2 decimal places')
def step_impl(context):
    assert context.basket.getSubTotal() == 2.88
    assert context.notifier.contains("sub-total: " + u"\xA3" + "2.88")
