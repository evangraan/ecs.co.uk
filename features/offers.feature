Feature: Offers discount items

	Scenario: Buy 2 get 1 free
		Given I have a loaded catalogue
		And I have a basket
		And the basket has 2 of the same item in it
		And I have a "buy 2 get 1 free" offer for the item
		When I list the items in the basket
		Then the discount is equal to the price of matching item

	Scenario: Percentage discount
		Given I have a loaded catalogue
		And I have a basket
		And the basket has an item in it
		And I have a "% discount" offer for the item
		When I list the items in the basket
		Then the discount is equal to the specified percentage of the price of matching item

	Scenario: Buy N of X, get the cheapest one for free
		#Given I have a basket
		#And the basket has an item in it
		#And the basket has another item in it
		#And I have a "buy N of X, get the cheapest one for free" offer
		#And the offer specifies X as the two items
		#And the offer specifies N as 2
		#When I list the items in the basket
		#Then the discount is equal to the price of the cheapest of the two items

	Scenario: Buy N of X, multiple matches
		#Given I have a basket
		#And the basket has an item in it
		#And the basket has another item in it
		#And the basket has a third item in it
		#And I have a "buy N of X, get the cheapest one for free" offer
		#And the offer specifies X as the first two items
		#And the offer specifies N as 2
		#And I have another "buy N of X, get the cheapest one for free" offer
		#And the additional offer specifies X as the second two items
		#And the additional offer specifies N as 2
		#When I list the items in the basket
		#Then the discount is equal to the price of the cheapest of the two items for which the 'buy N of X' yielded the biggest discount
