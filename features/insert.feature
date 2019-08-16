Feature: Inserting items into a shopping basket

	Scenario: Inserting into an empty basket
		Given I have a basket
		And the basket is empty
		And I have an item
		When I insert the item into the basket
		Then I am notified 'Item inserted'
		And the basket is no longer empty
		And the basket contains my item

	Scenario: Inserting into a basket with items in it
		Given I have a basket
		And the basket already has 2 items in it
		And I have an item
		When I insert the item into the basket
		Then I am notified 'Item inserted'
		And the basket has 3 items in it

