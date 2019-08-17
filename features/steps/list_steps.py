@then('I am notified of the total number of items in the basket')
def step_impl(context):
    assert context.notifier.wasNotified("number of items: 2") == True

@then('I am notified of each item')
def step_impl(context):
    assert context.notifier.contains("Baked Beans") == True
    assert context.notifier.contains("Sardines") == True

@then('for each item name the quantity of those items in the basket is listed')
def step_impl(context):
    assert context.notifier.contains("Baked Beans : 1") == True
    assert context.notifier.contains("Sardines : 1") == True

@then('for each item the base price is listed')
def step_impl(context):
    assert context.notifier.contains("Baked Beans : 1 @ 0.99") == True
    assert context.notifier.contains("Sardines : 1 @ 1.89") == True
