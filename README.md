# Github_Access


## Please refer to instructions to run (which will also point to limitations).

### Description:
Using the Github API (in Python) and d3.js, to retrieve and display data regarding developers in the organization (set to 'HubSpot').

Note: Change ORGANIZATION_NAME to choose organization in question (refer to limitations at the end of the file)


### Tools used:
1. PyGithub.
   Install: **pip install PyGithub**

2. Pytest.
   Install: **pip install -U pytest**

3. http-server (on command line, to open up and http-server) (IMPORTANT)
   Install: **npm install http-server -g** OR **brew install http-server -g**

4. d3.js.
   Sourced in html file, no initialization required for this.

5. jQuery.
   Also sourced in index.html. No initialization needed.


### Testing:
Testing is done using "dummy classes" in 'Test_Classes.py', which is used to create objects similar to github objects, such as NamedUser, Repository, etc, with similar attributes and functions as the Github objects.


### Idea behind Project:
Who are the employees in the organization that work together on outside projects or help each other with personal projects?
Representing connections between employees of any organization who have worked together on personal or non-organization-owned repositories


### Data Gathering:
All the members who work at the organization, and recorded on github.com, are gathered as github users.

Data, about them as well as their repositories, are gathered.


### Visualization:
1. Nodes are employees of the organization.

2. Color-coded nodes, based on popularity (attribute based on number of followers).

3. Links between nodes who have worked on the same repositories

4. Dragging a node displays the node's (employee's) information


### Limitations:

##### Github_Access.py (Data Gathering):

'HubSpot' is an organization which is not as "big" on github, as compared to others. Other organizations which are small or have "light" repositories with not too many contributors can be analyzed as well, by changing ORGANIZATION_NAME

Analyzing a "big" organization (i.e. an organization with lots of members on github) could cause issues. For example, organizations like 'Google' and 'Github', on github, have so much data about the connections between it's employees that it causes this program to reach an API rate limit due to amount of data being pulled (which tends to be more than the maximum allowable limit per second). Also, for 'Bloomberg', a repository exists with such a large number of contributors, that github takes it as infinite, and such a large amount of data is impossible to process. To tackle this, a few things have been added, that could help to limit the quantity of repositories, number of contributors or the amount of data being pulled per second: (the most useful to tackle the API rate limit being point 3)

1. A constant 'REPO_LIMIT' (at the top of 'Github_Access.py') can been used to limit the number of repositories being checked per member of the organization, so as to limit the amount of data being pulled. This must be set to -1 if you intend for the program to check all repositories of each member of the organization on github.

2. Another constant CONTRIBUTOR_LIMIT, analyzes only those repositories that have a number of contributors not more than CONTRIBUTOR_LIMIT.

3. The last constant has been the most successful, in tackling this problem single-handedly, in the simplest way. SLEEP_VAL is the amount of seconds you want the program to do nothing for. As can been seen in the program, this is added before every statement of git API calls in a loop, and this can help as it reduces the number of git calls per second, as the program just stalls for SLEEP_VAL seconds. Increasing SLEEP_VAL would make the program slower, but would ensure that the API limit won't been reached. This should be set to 0 if no sleep is wanted (i.e. in case of HubSpot)

The conditional statements using the first two constants stated above are only attempts at providing a fix for analyzing large companies. My code works for companies that are not too large on github, like 'HubSpot', and thus, these variables and their uses have been commented out.

However, if large companies are targeted, my code does work with an appropriate SLEEP_VAL (who's usage is not commented out), for example, SLEEP_VAL = 0.5 if ORGANIZATION_NAME = "Github". DO NOTE that this may take a very long time!!

Note that running the program multiple times without reasonably wide breaks in between might also result in violating the API rate limit


##### index.html (Visualization):

If you decided to gather data from a big company, space out the nodes a little less, by decreasing the value of the constant REPEL_FORCE which determined how much the nodes repel from each other. This needs to be decreased in order to create space for the nodes on the screen, by "squishing" them a little more.

INFO_WIDTH AND INFO_HEIGHT are the height and width of the canvas where information about the user will be displayed, when clicked on.

X_BORDER is the spacing between the graph canvas and the info canvas.

Y_BORDER is the spacing between the graph canvas and the screen.

Set these up to meet your desires :D


### Instructions:

1. *(Optional)* Set constants in Github_Access.py as per instructed in Limitations, and save file. (default constants set work fine)

2. Run file.
Terminal: **python Github_Access.py**

3. *(Optional)* Set constants in index.html as per instructed in Limitations, and save file. (default constants set work fine

  IMPORTANT:
4. Open index.html to see visualizations. (Tricky).
   - Double clicking on index.html won't work, as it doesn't grab data from an http server, but locally. In other words, the url from where the data is being read (in this case, it's the url of the data.json file), has to start with "http://" rather than "file://", as you cannot make an AJAX call to a local resource (GET request needs http url).

   - Since data.json is a local file, we need a workaround. This can be done by running a web server locally, and then making the AJAX call to the http resource.

   - To run index.html, in terminal, type in the command: **http-server** (This assumes all tools used have been installed or implemented in the environment).

   - Then open the url "localhost:8080" where 8080 is the port number opened due to the command http-server, using the web browser of your choice :) (Note that port is usually 8080, but may differ based on OS)
