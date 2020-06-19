# Shopping card prototype

## Running

### Manually

`cd shopping`

`python example-usage.py`

### Unit Tests

`cd tests`

`python test_basket.py`

`python test_discounts.py`

### BDD suite

`behave`

### Continuous Integration

* [Jenkins](jenkins.md)

## Design

* [Design notes](design.md)

## Additional Notes

* I added a buy-N-of-X rule to discounts.py that iterates all items in the basket, count the ones that are in the subset, and if that number is greater than or equal to the desired N, returns the price of the cheapest as discount. This is a generic algorithm, so any number of these rules can be added using the schema below. The indicator to the Offer class that this is a basket-wide offer is the key "basket".

`"basket":[{"rule" : "Buy N of X, get the cheapest one for free", "data" : { "N" : 3, "X" : [ "Shampoo (Medium)", "Shampoo (Large)", "Shampoo (Small)", "Biscuits" ] }}, "rule" : "Some other rule that also applies to the basket", "data": {"other" : "data"}]`

* In the implementation I used 'Item' consistently, and in 'catalogue.feature' indicated that 'Product' is a synonym.

* In the case of data consistency issues in a catalogue, the prototype loads all valid items, but reports an error as well.

## Development approach

This prototype was built test-first, specifically using the 'behave' BDD framework. Tests were written without any implementation code existing, after which the code was implemented using TDD (red-green-refactor).

For core components (basket and discounts) unit tests were also written.

## Dependencies

The only external dependency is the behave BDD library:

`pip install behave`

On my system 'python' is the same as 'python3' Please see the next section for more details.

## Development environment

This prototype was completed on an AWS reserved instance that I own running Ubuntu 18.04 (bionic). If you'd like to setup a similar environment, it is easy to do so:

`sudo apt-get install python3.7`

`sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1`

`git clone https://github.com/evangraan/ecs.co.uk.git`
