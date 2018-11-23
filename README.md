# Github_Access


### Description:
Using the Github API (in Python) and d3.js, to retrieve and display data regarding developers in the organization 'HubSpot'.

Note: Change ORGANIZATION_NAME to choose organization in question (refer to limitations at the end of the file)


### Tools used:
1. PyGithub.
   Install: pip install PyGithub

2. Pytest.
   Install: pip install -U pytest*


### Idea behind Project:
Who are the employees in HubSpot that work together on outside projects or help each other with personal projects?
Representing connections between employees of HubSpot who have worked together on personal or non-HubSpot-owned repositories


### Data Gathering (Plan for now):
All the member's who work at HubSpot, and recorded on github.com/HubSpot, are gathered as github users.

Data, about them as well as their repositories, are gathered.


### Visualization (Plan for now):
1. Nodes are employees of HubSpot.

2. Color-coded nodes, based on location.

3. Links between nodes who have worked on the same repositories

4. Clicking on the node displays employee's information


### Limitations:
'HubSpot' is an organization which is not as "big" on github, as compared to others. Other organizations which are small or have "light" repositories with not too many contributors can be analyzed as well, by changing ORGANIZATION_NAME

Analyzing a "big" organization (i.e. an organization with lots of members on github) could cause issues. For example, organizations like 'Google' and 'Github', on github, have so much data about the connections between it's employees that it causes this program to reach an API rate limit due to amount of data being pulled (which tends to be more than the maximum allowable limit per second). Also, for 'Bloomberg', a repository exists with such a large number of contributors, that github takes it as infinite, and such a large amount of data is impossible to process. To tackle this, a couple of things have been added, in comments, that could help to limit the quantity of repositories and number of contributors:

1. A constant 'REPO_LIMIT' (at the top of 'Github_Access.py') can been used to limit the number of repositories being checked per member of the organization, so as to limit the amount of data being pulled. This must be set to -1 if you intend for the program to check all repositories of each member of the organization on github.

2. Another constant CONTRIBUTOR_LIMIT, analyzes only those repositories that have a number of contributors not more than CONTRIBUTOR_LIMIT.

The conditional statements using the two constants stated above are only attempts at providing a fix for large companies. My code works for companies that are not too large on github, like 'HubSpot', and thus, these variables and their uses have been commented out.
