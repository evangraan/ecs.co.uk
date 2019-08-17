# Design

Aggregation over containment. The basket class does not contain a catalogue or offers, rather these are provided to it across its public API
After I had specced the system using the BDD suite (usually this would be limited to the highest value feature, which I'd then implement, and so iterate, but this project is small enough to spec in one go), I decided on the following architecture for the system:

- json for the data store (a simple file)). json is often a great choice, and as data can be sourced from databases (which in a microservices world often sit behind APIs) or diretly from APIs, json is a safe, flexible choice.
- given the test direction to focus on the calculation core rather, I included a simple configuration for specifying the catalogue data source fule in the project. I did how-ever include a check whether a .reload file is present, which would load a new catalogue if present and then delete the .reload signal. This is to allow for change of catalogue without restarting the system.
- Using MVC is always a good idea for systems that have output and models (the rules in this case) and so I implemented a very simple command line controller and stdout view.
- To avoid over- and under-design I would normally ask the client what success from their perspective looks like and try and elicit some non functional requirements to guide the selection of design components. From the test instructions I extracted the NFR 'focus on a solid core algorithm' and so I made the rest really simple, but I did sketch out some basic design components as indicated above so that it is easy to grow and maintain the system without too much refactor.
- shopping carts are usually related to sessions (which can live long)- as such I made the call to construct a basket with the offers and catalogue to use. This could easily be refactored at the API level though if this call was not appropriate for the use case.
