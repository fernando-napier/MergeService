# MergeService

This project is meant to REST-fully merge profiles from Bitbucket and Github.

To run the API run the following command at the root of the project
```bash
python api.py
```

Questions about Requirements:
1) How many daily active users do we expect for this kind of service?
2) Are there situations in which profiles submitted would be un-mergeable? specifically if the org/team names are for different orgs
3) Are we also looking to store said merged data in a data store?
4) Since this feels more like a command than not, would it be prudent to consider RPC for this endpoint?

Considerations:
* How would you structure your code?
  * For an MVP I created a single application that takes a GET request and merges team/org names as query params and returns the result of the merged data
  * A mature version of this API would probably include separation of the API into component microservices (the REST API, an Orchestrator, a Bitbucket API Service, a Github API Services) and a load balancer if necessary 
* How efficient is your design?
  * The MVP is not very efficient as all component parts are interdependent
  * The designed version would be easier to scale but more tedious to maintain as there would be 4 component microservices
* How would you handle versions of external APIs; are some versions better suited to solve our problem?
* How would you approach testing this design?
* What are the steps you would take to solve the problem?
* What questions do you have about the requirements?
* Assuming we want to bring this service live to be used by customers, what additional work would you want to do before launch? 
