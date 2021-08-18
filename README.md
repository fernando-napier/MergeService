# MergeService

This project is meant to REST-fully merge profiles from Bitbucket and Github.

To run the API run the following command at the root of the project
```bash
python api.py
```

Merge Profile Diagram

![MergeProfile (1)](https://user-images.githubusercontent.com/11913005/129831557-cea60a16-af64-4f2f-b733-aa13d707e137.png)



ENDPOINTS
```
Must Have
GET /api/v1/profiles/{profileName}

Nice to Have
GET /api/v1/profiles/{profileName}/repos
GET /api/v1/profiles/{profileName}/languages
GET /api/v1/profiles/{profileName}/topics
```

Profile Request
```
HEADERS
Accept:application/json
Authorization: Bearer {apikey}

BODY
no request body
```

Profile Response
```
Response Body
{
 "repos": {
   "original": int,
   "forked": int
   },
   "followers": int,
   "languages: [
   {
   "language":string,
   "count":int
   }],
   "topics: [
   {
   "topic":string,
   "count":int
   }]
}
```

Questions about Requirements:
1) How many daily active users do we expect for this kind of service?
2) Are there situations in which profiles submitted would be un-mergeable? specifically if the org/team names are for different orgs
3) Are we also looking to store said merged data in a data store?
4) Since this feels more like a command than not, would it be prudent to consider RPC for this endpoint?
5) Is this endpoint expected to follow a HATEOAS approach?

Considerations:
* How would you structure your code?
  * For an MVP I created a single application that takes a GET request and merges team/org names as query params and returns the result of the merged data
  * A mature version of this API would probably include separation of the API into component microservices (the REST API, an Orchestrator, a Bitbucket API Service, a Github API Services) and a load balancer if necessary 
* How efficient is your design?
  * The MVP is not very efficient as all component parts are interdependent
  * The designed version would be easier to scale but more tedious to maintain as there would be 4 component microservices
* How would you handle versions of external APIs; are some versions better suited to solve our problem?
  * I am using Github's version 3 of the API though version 4 includes GraphQL which would probably lower the number of API requests needed for the implementation
* How would you approach testing this design?
  * manual testing, unit testing, I'm not sure integration testing is necessary as the API is external and assumed to work virtually 100% of the time
* What are the steps you would take to solve the problem?
  * Ensure project is scoped well (for internal or internal use, any cross team dependencies, technology available to complete project, etc)
  * Define all the data points to be returned in the merged profile
  * Create the API spec for the request and reponse bodies to be returned by API endpoint
  * Create a diagram for the workflow
  * Create an epic and stories for units of work based on system design
  * Talk with stakeholders about when the epic would slate into the initiaves of the tech team
  * Execute stories
  * Profit
* Assuming we want to bring this service live to be used by customers, what additional work would you want to do before launch? 
  *  Finalize deployment strategy, potentially deploying at a time when low volume would occur
  *  Demo for stakeholders
  *  Only release for a small percentage of users based on Oauth scopes potentially
