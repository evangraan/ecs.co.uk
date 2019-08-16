Feature: List in a shopping basket

	Scenario: Listing an empty basket
		Given I have a basket
		And the basket is empty
		When I list the items in the basket
		Then I am notified 'No items'

	Scenario: Listing a basket with items in it
		Given I have a basket
		And the basket has 2 items in it
		And I have an item
		When I list the items in the basket
		Then I am notified of the total number of items in the basket
		And I am notified of each item
		And for each item the names are listed uniquely
		And for each item name the quantity of those items in the basket is listed
		And the sub-total for the basket is listed in pounds
		And the discount for the basket is listed in pounds
		And the total for the basket is listed in pounds

