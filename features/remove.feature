Feature: Removing items from a shopping basket

    Scenario: Removing from an empty basket
        Given I have a basket
        And the basket is empty
        When I try and remove an item
        Then I am notified 'item not in basket'
        And the basket remains empty

    Scenario: Removing from an almost empty basket
        Given I have a basket
        And the basket has 1 items in it
        When I try and remove an item
        Then I am notified 'item removed'
        And the basket is empty

    Scenario: Removing from a filled basket
        Given I have a basket
        And the basket has 2 items in it
        When I try and remove an item
        Then I am notified 'item removed'
        And the basket still has 1 item in it
        And the basket does not have the removed item in it
