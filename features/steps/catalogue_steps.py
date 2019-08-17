from shopping.catalogue import *
from shopping.basket import *
from environment import *

@given('I have a catalogue')
def step_impl(context):
    assert context.catalogue != None

@given('the catalogue is empty')
def step_impl(context):
    context.orchestrator.seedCatalogue("empty")

@when('I load the catalogue')
def step_impl(context):
    context.catalogue.load()

@then('I have no items')
def step_impl(context):
    assert context.catalogue.size() == 0

@given('the catalogue has valid items in it')
def step_impl(context):
    context.orchestrator.seedCatalogue("full")

@then('I have the correct number of items')
def step_impl(context):
    assert context.catalogue.size() == 6

@then('each item has a price')
def step_impl(context):
    for item in context.catalogue.getItems():
        price = context.catalogue.lookup(item)
        assert price != None
        isAFloat = True
        try:
            float(price)
        except ValueError:
            isAFloat = False
        assert isAFloat == True

@given('an item does not have a valid name')
def step_impl(context):
    context.orchestrator.seedCatalogue("invalid-name")

@then('I have the correct number of items minus one')
def step_impl(context):
    assert context.catalogue.size() == 5

@then('the invalid item is not in the loaded list')
def step_impl(context):
    assert context.catalogue.lookup("Baked Beans") == None

@given('an item does not have a valid price')
def step_impl(context):
    context.orchestrator.seedCatalogue("invalid-price")

@given('I have a loaded catalogue')
def step_impl(context):
    assert context.catalogue != None
    context.orchestrator.seedCatalogue("full")
    context.catalogue.load()
