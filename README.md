# ECS shopping card excercise

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


## Comment on the examples provided

My assumption is that these examples are not based on the offers specified as current, but from a previous set of offers no longer valid. The question does specify that offers change.

The "Basket 1" example indicates a discount not achievable with the rules specified. The buy 2 get 1 free offer would suggest that 2 items should be given free, but the question sets the expectation at only one free item. The actual discount would be 1.89

The "Basket 2" example indicates a discount not achievable with the rules specified. The actual discount would be 1.89 (0.99 from the 'buy 2 get 1 free' offer for the 2 tins of baked beans, 0 for biscuits as there are no offers specified for biscuits and 0.99 from the 25% discount on sardines.)

## Bonus questions

### question 1
I added an example rule to discounts.py that iterates all items in the basket, count the ones that are in the subset, and if that number is greater than or equal to the desired N, returns the price of the cheapest as discount.

### question 2
I simply split the rules into two lists, those that apply to 1 item only and those that apply to subsets. Rules that apply to subsets are processed in offer.py after rules that apply to individual items. The desired behaviour is achieved.

### question 3
I fixed a few issue in the question and made a pull request for them

## Design

* [Design notes](design.md)

## Additional Notes

* I would recommend to the retailer that they standardize on one term for items (either product or item.) In my implementation I used item consistently, and in 'catalogue.feature' indicated that Product is a synonym.

* In the case of data itegrity issues in the catalogue, I made the decision to load all valid items, but to report an error as well.

* I was not sure if you intended the *** pre- and post-fixes to the item name to be included. I apologize if it was intended as part of the name, usually I'd ask the client. In my data set I did not include the ***s.

## Development approach

This excercise was built test-first, specifically using the 'behave' BDD framework. Tests were written without any implementation code existing, after which the code was implemented using TDD (red-green-refactor).

For core components (basket and discounts) unit tests were also written.

## Dependencies

The only external dependency is the behave BDD library:

`pip install behave`

On my system 'python' is the same as 'python3' Please see the next section for more details.

## Development environment

This excercise was completed on an AWS reserved instance that I own running Ubuntu 18.04 (bionic). If you'd like to setup a similar environment, it is easy to do so:

`sudo apt-get install python3.7`

`sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1`

`git clone https://github.com/evangraan/ecs.co.uk.git`

# Todo

- convert tabs to 4 spaces in all files
- visually inspect should be automated
