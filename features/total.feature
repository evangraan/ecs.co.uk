Feature: Calculating the total for a shopping basket

	Scenario: Calculating the total for an empty basket
		Given I have a basket
		And the basket is empty
		When I list the items in the basket
		Then the total for the basket is listed in pounds
		And the total is 0 

	Scenario: Calculating the total for a basket with matching offers
		Given I have a basket
		And the basket has 2 items in it
		And an offer matches one of the items
		And a second offer matches the same item
		When I list the items in the basket
		Then the total for the basket is listed in pounds
		And the total is the sum of the base prices of both items minus all discouts for offers that match
		And the total is accurate to 2 decimal places

	Scenario: Calculating the total for a basket with items in it but no matching offers
		Given I have a basket
		And the basket has 2 items in it
		And no offers match
		When I list the items in the basket
		Then the total for the basket is listed in pounds
		And the total is the sum of the base prices
		And the total is accurate to 2 decimal places
