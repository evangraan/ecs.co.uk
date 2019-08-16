@given('I have a basket')
def step_impl(context):
    assert context.basket != None

@given('the basket is empty')
def step_impl(context):
    assert context.basket.size() == 0

@given('I have an item')
def step_impl(context):
    context.item = "Baked Beans"

@when('I insert the item into the basket')
def step_impl(context):
    context.basket.insert(context.item, 1)

@then('the basket is no longer empty')
def step_impl(context):
    assert context.basket.size() > 0

@then('the basket contains my item')
def step_impl(context):
    assert context.basket.lookup(context.item) != None

@given('the basket already has {number} items in it')
def step_impl(context, number):
    context.basket.insert("Sardines", number)

@then('the basket has {number} items in it')
def step_impl(context, number):
    print(number + "==" + str(context.basket.size()))
    assert context.basket.size() == int(number)
