@when('I try and remove an item')
def step_impl(context):
    context.item = "Baked Beans"
    context.basket.remove(context.item, 1)

@then('the basket remains empty')
def step_impl(context):
    assert context.basket.size() == 0

@given('the basket has 1 items in it')
def step_impl(context):
    context.item = "Baked Beans"
    context.basket.insert(context.item, 1)

@then('the basket is empty')
def step_impl(context):
    assert context.basket.size() == 0

@given('the basket has 2 items in it')
def step_impl(context):
    context.item = "Baked Beans"
    context.basket.insert(context.item, 1)
    context.item = "Sardines"
    context.basket.insert(context.item, 1)

@then('the basket still has 1 item in it')
def step_impl(context):
    assert context.basket.size() == 1

@then('the basket does not have the removed item in it')
def step_impl(context):
    assert context.basket.lookup(context.item) == None
