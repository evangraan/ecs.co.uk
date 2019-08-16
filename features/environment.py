import sys
import json
sys.path.append("shopping")
sys.path.append("test")

from behave import *
from shopping.catalogue import *
from shopping.basket import *
from test.orchestrator import *
from test.notifier import *

@fixture
def bootstrap(context):
    context.notifier = TestNotifier()
    context.orchestrator = Orchestrator()
    context.catalogue = Catalogue(context.orchestrator.cataloguePath(), context.notifier)
    context.basket = Basket(context.catalogue, context.notifier)

def before_all(context):
    use_fixture(bootstrap, context)

def before_each(context):
    context.notifier.clear()
