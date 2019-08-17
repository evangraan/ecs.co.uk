# Design

## Association (Aggregation) over Containment (Ownership)

The basket class does not contain a catalogue or offers, rather these are provided to it across its public API

## Data source

I selected JSON for the data store (a simple file)). JSON is often a great choice, and as data can be sourced from databases (which in a microservices world often sit behind APIs) or diretly from APIs, JSON is a safe, flexible choice.

## Discount rules

I made the decision to separate the specification of the discount rules from the offer class. These rules are small and singly responsible. I think it would be over-design to put them each in their own class at this stage. Later that might become preferable.

## Singly responsible classes

I created classed for Catalogue, Offers, Basket and a file for Discounts. I think this the minimal set of responsibilities to cater for in the system. Each of these offers a clear API and all functionality of their APIs are directly relevant to their domain.

## Sparse design

To avoid over- and under-design I would normally ask the client what success from their perspective looks like and try and elicit some non functional requirements to guide the selection of design components. From the test instructions I extracted the NFR 'focus on a solid core algorithm' and so I made the rest really simple, but I did sketch out some basic design components so that it would be easy to grow and maintain the system without too much refactor.

## Dry

The code for the most part is pretty dry. Catalogue and Offers where tempting to derive from a base class, but in the end I did not think the small shared footprint large enough to warrant a base class. BDD features and step definitions by nature also makes the testing code more DRY, as step fulfillment is re-used through-out.

## Clean code

I try and keep functions meaningul, singly responsible and named for what the function aims to accomplish. I limit the number of parameters per function to 4 max.

## Demeter

I also try and avoid violating the Demeter principle where-ever I can, favouring passing dependencies as parameters as opposed to making then variables in the class. Where the class should own the data (e.g. the items in a basket) I did use member fields.

## Liskov Substitusion

I made dependencies substitutable, but it is not formalized using abstract classes at this stage. I think that would be over-design now. Duck typing is enough at this stage I think. Catalgue, Offers and Notifiers are the main classes that one would want to formalize later if it becomes valuable to the project to do so.

## Test design

I try to treat test code and production code as equally important (I think test code is in fact more important) and so try and keey it DRY as well and to not take shortcuts.

## Mocking

This project was small enough, and as I starte with BDD specs I did not have a big need for mocking. I prefer the real thing instead of mocks (which later become expensive to maintain I find). Fixtures in this project are simple data files that are swapped out by the unit and BDD suites as needed.
