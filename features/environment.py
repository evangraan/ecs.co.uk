import sys
import json
sys.path.append("shopping")
sys.path.append("orchestration")

from behave import *
from shopping.catalogue import *
from shopping.offers import *
from shopping.basket import *
from orchestration.orchestrator import *
from orchestration.notifier import *

@fixture
def bootstrap(context):
    context.notifier = TestNotifier()
    context.orchestrator = Orchestrator()
    context.catalogue = Catalogue(context.orchestrator.cataloguePath(), context.notifier)
    context.offers = Offers(context.orchestrator.offersPath(), context.notifier)
    context.offers.load()
    context.basket = Basket(context.notifier)

def before_all(context):
    use_fixture(bootstrap, context)

def before_scenario(context, scenario):
    context.notifier.clear()
    context.basket.clear()
