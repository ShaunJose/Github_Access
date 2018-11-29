# Data Gatherng
import sys
from github import Github
from time import sleep
import json

# declaring my access token --> (given no permissions)
ACCESS_TOKEN = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

# creating github instance using token
g = Github(ACCESS_TOKEN)

# organisation that's being targetted here
ORGANIZATION_NAME = "HubSpot"

# popularity segregation based on number of followers of a github user
POPULARITY_BOUNDARIES = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000]

#max number of contributors for a repository
#CONTRIBUTOR_LIMIT = 400

# number of repositories check per user. set to -1 for no limit
#REPO_LIMIT = 45

# amount you want to suspend programming time for. Should be set to 0 if aiming for no sleep
SLEEP_VAL = 0


# Get logins from a list of objects
def get_logins_of_users(objects_list):
    """
    Get all the logins from a list of user objects.

    @param objects_list: A list of user objects

    return: a list of logins of all the user objects in objects_list
    """

    logins = []
    for obj in objects_list:
        sleep(SLEEP_VAL) #to avoid github API rate limit violation
        login_id = obj.login
        logins.append(login_id)

    return logins


# Get contributors to all repos of a member
def get_member_repos_contribs(member, member_objects):
    """
    Returns a list of all the contributors to REPO_LIMIT/all repositories of a github user, that are in the organization specified by ORGANIZATION_NAME

    @param login_id: A github user's login id

    return: a list of the logins of all the contributors to REPO_LIMIT/all repositories, provided they are in the organization specified in ORGANIZATION_NAME
    """

    #get member's repository objects
    repos = list(member.get_repos())

    contributors = []
    temp = []
    #iter_cnt = 0;

    for repo in repos:
        #if iter_cnt == REPO_LIMIT:
        #    break
        sleep(SLEEP_VAL) #to avoid github API rate limit violation
        temp = list(repo.get_contributors()) # getting contributor objects
        #if(len(temp) <= CONTRIBUTOR_LIMIT):
        contribs_in_org = list(set(temp).intersection(member_objects))
        contributors += get_logins_of_users(contribs_in_org) # getting logins
        #iter_cnt += 1

    # converting it to a set knocks of all duplicates
    return list(set(contributors))


# Get contributors from the organization
def get_all_contributors_from_org(members):
    """
    Gets contributors' logins of REPO_LIMIT/all organization employees repos

    @param members: A list of member objects of the organization

    return: A list of the login ids of CONTRIBUTOR_LIMIT/all contributors to each member's repositories (all of them or constrained by REPO_LIMIT), except for the owner of the repo himself/herself.
    """
    all_contributors = []

    print("Members done processing:")

    # getting connections and contributors for each member of the org
    cnt=0 # this keeps track of how may users have been processed
    for curr_mem in members:
        #get contributors' usernames
        contributors = get_member_repos_contribs(curr_mem, members)
        # remove the owner of the repo as a contributor
        if curr_mem in contributors:
            contributors.remove(curr_mem)
        all_contributors.append(contributors)
        cnt+=1
        print str(cnt) + "/" + str(len(members))

    return all_contributors


# Get number of followers of users
def get_num_of_followers(users):
    """
    Get the number of followers for each of the user

    @param users: A list of github NamedUser objects

    return: A list of corresponding number of followers per user
    """

    followers = []

    for user in users:
        sleep(SLEEP_VAL)
        followers.append(user.followers)

    return followers


# Get popularity of each user
def get_popularity(followers, boundaries):
    """
    Get the popularity of each user, based on boundaries

    @param followers: List of number of followers

    @param boundaries: A list of integer boundaries which dictate popularity. This list must be in ascending order

    return: A corresponding list of popularity from 0 to (len(boundaries) - 1), with 0 being lowest popularity
    """

    popularity = []

    for num_foll in followers:
        index = 0
        for boundary in boundaries:
            if num_foll < boundary:
                popularity.append(index)
                break
            index += 1
        if index == len(boundaries): #if followers not lower than any boundary
            popularity.append(len(boundaries)) #append highest popularity!

    return popularity


#Get locations of github users
def get_locations_of_users(users):
    """
    Get locations of github users.

    @param users: List of github NamedUser objects

    return: List of corresponding locations of users.
    """

    locations = []

    for user in users:
        sleep(SLEEP_VAL)
        locations.append(user.location)

    return locations


#Create graph with the information given in params, in format
def create_graph(usernames, followers, popularity, locations, connections):
    """
    Creates a graph, displaying information about github users in a well-formatted way.

    @param usernames: List of usernames of github users

    @param followers: List of corresponding number of followers per user

    @param popularity: List of correspinging level of popularity per user

    @param locations: List of correspinging location of each user

    @param connections: List of contributors for each repository

    return: A dicitonary with two arrays -> nodes, containting dictionaries with attributes (username, number of followers, popularity, location) and links, containg dictionaries with attributes (source, target), using connections.

    Do note that, if the length of all lists are not the same, this method will break, which won't happen when passing information fetched straight from the Github API.
    """

    #dictionary with two empty arrays
    graph = { "nodes": [], "links": [] }

    #loop limit
    max = len(usernames)

    #populate nodes array appropriately
    for index in range(max):
        node_elem = {}
        node_elem["username"] = usernames[index]
        node_elem["followers"] = followers[index]
        node_elem["popularity"] = popularity[index]
        node_elem["location"] = locations[index]
        graph["nodes"].append(node_elem)

    #populate links array appropriately
    for index in range(max):
        curr_user = usernames[index]
        conn_arr = connections[index]
        for curr_conn in conn_arr:
            link_elem = { "source": curr_user,
                          "target": curr_conn }
            graph["links"].append(link_elem)

    return graph


# Main method --> Keep it small :)
if __name__ == "__main__":

    #getting organisation 'github'
    organization = g.get_organization(ORGANIZATION_NAME)

    #getting members of github as a list of 'NamedUser' objects.
    members = list(organization.get_members())

    #get a list of lists with contributors from HubSpot to a repository of a HubSpot employee, except for the owner of the repository
    all_contributors = get_all_contributors_from_org(members)

    # get the members' github login ids
    usernames = get_logins_of_users(members)

    # get the members' number of followers
    followers_count = get_num_of_followers(members)

    # get the members' popularity base on followers_count and POPULARITY_BOUNDARIES
    popularity = get_popularity(followers_count, POPULARITY_BOUNDARIES)

    # get the members' locations
    locations = get_locations_of_users(members)

    graph = create_graph(usernames, followers_count, popularity, locations, all_contributors)

    #write graph to JSON file
    with open('data.json', 'w') as outfile:
        json.dump(graph, outfile)

    print("'data.JSON' created")
