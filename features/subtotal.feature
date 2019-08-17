Feature: Calculating the subtotal for a shopping basket

	Scenario: Calculating the subtotal for an empty basket
		Given I have a basket
		And the basket is empty
		When I list the items in the basket
		Then the sub-total for the basket is listed in pounds
		And the sub-total is 0.00

	Scenario: Calculating the subtotal for a basket with items in it
		Given I have a loaded catalogue
		And I have a basket
		And the basket has 2 items in it
		When I list the items in the basket
		Then the sub-total for the basket is listed in pounds
		And the sub-total is the sum of the base prices of both items
		And the sub-total is accurate to 2 decimal places

