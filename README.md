# Github_Access

### Description:
Using the Github API (in Python) to retrieve and display data regarding developers of Github.


### Tools used:
1. PyGithub.
   Install: pip install PyGithub

2. Pytest.
   Install: pip install -U pytest*


### Idea behind Project:
Who are the github employees that work together on outside projects or help each other on personal projects?

NOTE: can be done for any company other than github, by changing value of ORGANIZATION_NAME variable on top of the file 'Github_Access.py'


### Data Gathering (Plan for now):
All the member's who work in github, and recorded on github.com/github, are gathered as github users.

Their location, as well as repositories are gathered as well.


### Visualization (Plan for now):
1. Nodes are employees of github.

2. Color-coded nodes, based on location.

3. Links between nodes who have worked on the same repositories

4. Clicking on the node display's employee's information
