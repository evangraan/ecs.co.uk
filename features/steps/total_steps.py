@then('the total for the basket is listed in pounds')
def step_impl(context):
    assert context.notifier.contains(u"\xA3") == True

@then('the total is 0.00')
def step_impl(context):
    assert context.basket.getTotal() == 0
    assert context.notifier.contains("total: " + u"\xA3" + "0.00")

@then('the total is the sum of the base prices of both items minus the best discounts for offers that match')
def step_impl(context):
    assert context.basket.getTotal() == context.basket.getSubTotal() - context.basket.getDiscount()
    assert context.notifier.contains("total: " + u"\xA3" + "2.63")

@then('the total is accurate to 2 decimal places')
def step_impl(context):
    assert context.notifier.contains("total: " + u"\xA3" + "2.88")

@then('the total is the sum of the base prices')
def step_impl(context):
    assert context.basket.getTotal() == context.basket.getSubTotal()
    assert context.notifier.contains("total: " + u"\xA3" + "2.88")
