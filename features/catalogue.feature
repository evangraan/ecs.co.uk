Feature: Item (product) catalogue

    Scenario: Empty catalogue
        Given I have a catalogue
        And the catalogue is empty
        When I load the catalogue
        Then I have no items
        And I am notified 'empty catalogue'

    Scenario: Catalogue entry schema
        Given I have a catalogue
        And the catalogue has valid items in it
        When I load the catalogue
        Then I have the correct number of items
        And each item has a price
        And I am notified 'catalogue successfully loaded'

        Scenario: Catalogue integrity error - price
        Given I have a catalogue
        And the catalogue has valid items in it
        And an item does not have a valid price
        When I load the catalogue
        Then I have the correct number of items minus one
        And the invalid item is not in the loaded list
        And I am notified 'error loading some items'

