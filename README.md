# Github_Access


### Description:
Using the Github API (in Python) and d3.js, to retrieve and display data regarding developers in the organization (set to 'HubSpot').

Note: Change ORGANIZATION_NAME to choose organization in question (refer to limitations at the end of the file)


### Tools used:
1. PyGithub.
   Install: pip install PyGithub

2. Pytest.
   Install: pip install -U pytest*


### Testing:
Testing is done using "dummy classes" in 'Test_Classes.py', which is used to create objects similar to github objects, such as NamedUser, Repository, etc, with similar attributes and functions as the Github objects.


### Idea behind Project:
Who are the employees in the organization that work together on outside projects or help each other with personal projects?
Representing connections between employees of any organization who have worked together on personal or non-organization-owned repositories


### Data Gathering (Plan for now):
All the members who work at the organization, and recorded on github.com, are gathered as github users.

Data, about them as well as their repositories, are gathered.


### Visualization (Plan for now):
1. Nodes are employees of the organization.

2. Color-coded nodes, based on popularity (attribute based on number of followers).

3. Links between nodes who have worked on the same repositories

4. Clicking on the node displays employee's information


### Limitations:
'HubSpot' is an organization which is not as "big" on github, as compared to others. Other organizations which are small or have "light" repositories with not too many contributors can be analyzed as well, by changing ORGANIZATION_NAME

Analyzing a "big" organization (i.e. an organization with lots of members on github) could cause issues. For example, organizations like 'Google' and 'Github', on github, have so much data about the connections between it's employees that it causes this program to reach an API rate limit due to amount of data being pulled (which tends to be more than the maximum allowable limit per second). Also, for 'Bloomberg', a repository exists with such a large number of contributors, that github takes it as infinite, and such a large amount of data is impossible to process. To tackle this, a few things have been added, that could help to limit the quantity of repositories, number of contributors or the amount of data being pulled per second: (the most useful to tackle the API rate limit being point 3)

1. A constant 'REPO_LIMIT' (at the top of 'Github_Access.py') can been used to limit the number of repositories being checked per member of the organization, so as to limit the amount of data being pulled. This must be set to -1 if you intend for the program to check all repositories of each member of the organization on github.

2. Another constant CONTRIBUTOR_LIMIT, analyzes only those repositories that have a number of contributors not more than CONTRIBUTOR_LIMIT.

3. The last constant has been the most successful, in tackling this problem single-handedly, in the simplest way. SLEEP_VAL is the amount of seconds you want the program to do nothing for. As can been seen in the program, this is added before every statement of git API calls in a loop, and this can help as it reduces the number of git calls per second, as the program just stalls for SLEEP_VAL seconds. Increasing SLEEP_VAL would make the program slower, but would ensure that the API limit won't been reached. This should be set to 0 if no sleep is wanted (i.e. in case of HubSpot)

The conditional statements using the first two constants stated above are only attempts at providing a fix for analyzing large companies. My code works for companies that are not too large on github, like 'HubSpot', and thus, these variables and their uses have been commented out.

However, if large companies are targeted, my code does work with an appropriate SLEEP_VAL (who's usage is not commented out), for example, SLEEP_VAL = 0.5 if ORGANIZATION_NAME = "Github". DO NOTE that this may take a very long time!!

Note that running the program multiple times without reasonably wide breaks in between might also result in violating the API rate limit
