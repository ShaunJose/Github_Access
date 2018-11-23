from github import Github
from time import sleep
import sys

# declaring my access token --> (given no permissions)
ACCESS_TOKEN = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

# creating github instance using token
g = Github(ACCESS_TOKEN)

#organisation that's being targetted here
ORGANIZATION_NAME = "HubSpot"

#max number of contributors for a repository
#CONTRIBUTOR_LIMIT = 400

# number of repositories check per user. set to -1 for no limit
#REPO_LIMIT = 45

# amount you want to suspend programming time for. Should be set to 0 if aiming for no sleep
SLEEP_VAL = 0


# Get logins from a list of objects
def get_logins_from_users(objects_list):
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
        contributors += get_logins_from_users(contribs_in_org) # getting logins
        #iter_cnt += 1

    # converting it to a set knocks of all duplicates
    return list(set(contributors))


# Main method
if __name__ == "__main__":

    #getting organisation 'github'
    organization = g.get_organization(ORGANIZATION_NAME)

    #getting members of github as a list of 'NamedUser' objects.
    members = list(organization.get_members())

    #list of lists with contributors from HubSpot to a repository of a HubSpot employee
    all_contributors = []

    cnt=0 # this keeps track of how may users have been processed
    for curr_mem in members:
        #get contributors' usernames
        contributors = get_member_repos_contribs(curr_mem, members)
        # remove the owner of the repo as a contributor
        if curr_mem in contributors:
            contributors.remove(curr_mem)
        all_contributors.append(contributors)
        cnt+=1
        print cnt

    #temprorary
    print all_contributors

    #TODO:

    # get the member's github login ids
    # usernames = get_logins_from_users(members)

    # Get some information about the user, like location or whatever and use color for those properties. Get number of followers and such (Look at bookmarks). Make methods for both functions and add tests if possible (make classes similar to Named User with attributes like loocation..)

    # make the graph using a function, passing in usernames, other properties (make a function for it maybe, passing in member objects) and all_contributors

    # graph is a dicitonary with two arrays -> nodes (username, other properties) and links (source, target), using all_contributors.

    # add tests for the graph making function

    # save graph to JSON file
