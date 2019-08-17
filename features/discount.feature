Feature: Calculating the discount for a shopping basket

    Scenario: Calculating the discount for an empty basket
        Given I have a basket
        And the basket is empty
        When I list the items in the basket
        Then the discount for the basket is listed in pounds
        And the discount is 0.00

    Scenario: Calculating the discount when no offers match
        Given I have a loaded catalogue
        And I have a basket
        And the basket has 2 items in it
        And no offers match the items
        When I list the items in the basket
        Then the discount for the basket is listed in pounds
        And the discount is 0.00

    Scenario: Calculating the discount when one offer matches
        Given I have a loaded catalogue
        And I have a basket
        And the basket has 2 items in it
        And an offer matches one of the items
        When I list the items in the basket
        Then the discount for the basket is listed in pounds
        And the discount is the correct discount amount for the offer that matches
        And the discount is accurate to 2 decimal places

    Scenario: Calculating the discount when two offers match
        Given I have a loaded catalogue
        And I have a basket
        And the basket has 2 items in it
        And an offer matches one of the items
        And an offer matches the other item
        When I list the items in the basket
        Then the discount for the basket is listed in pounds
        And the discount is the sum of the correct discounts for both offers that match

    Scenario: Calculating the discount when multiple offers match an item
        #Given I have a loaded catalogue
        #And I have a basket
        #And the basket has 2 items in it
        #And an offer matches one of the items
        #And a second offer matches the same item
        #When I list the items in the basket
        #Then the discount for the basket is listed in pounds
        #And the discount is the correct discount amount for the offer that matches with lowest resulting cost for the basket as a whole

    Scenario: Calculating the discount when multiple offers match multiple items
        #Given I have a loaded catalogue
        #And I have a basket
        #And the basket has 2 items in it
        #And an offer matches one of the items
        #And a second offer matches the same item
        #And the second offer also matches the other item
        #And a third offer matches the same item
        #And the third offer also matches the other item
        #When I list the items in the basket
        #Then the discount for the basket is listed in pounds
        #And the discount is the correct discount amount for the offer that matches with lowest resulting cost for the basket as a whole
