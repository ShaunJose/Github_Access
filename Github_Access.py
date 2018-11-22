from github import Github
import sys

# declaring my access token --> (given no permissions)
ACCESS_TOKEN = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

# creating github instance using token
g = Github(ACCESS_TOKEN)

#organisation that's being targetted here
ORGANIZATION_NAME = "github"


# Get logins from a list of objects
def get_logins_from_users(objects_list):
    """
    Get all the logins from a list of user objects.

    @param objects_list: A list of user objects

    return: a list of logins of all the user objects in objects_list
    """

    logins = []
    for obj in objects_list:
        login_id = obj.login
        logins.append(login_id)

    return logins


# Get names from a list of repository objects
def get_names_from_repos(objects_list):
    """
    Gets all the repository names from a list of repository objects.

    @param objects_list: A list of repository objects

    return: a list of names of all the repository objects in objects_list
    """

    names = []
    for obj in objects_list:
        name = obj.full_name
        names.append(name)

    return names


# Get contributors to all repos of a member
def get_member_repos_contribs(login_id):
    """
    Returns all contributors to all repositories of a github user

    @param login_id: A github user's login id

    return: a set of all the lgoins of all the contributors to all repositories, including the github user him/herself provided the user contributed to atleast one repo
    """

    # get user
    member = g.get_user(login_id)
    #get member's repository objects
    repo_objects = list(member.get_repos())
    #get member's repos' names
    repos = get_names_from_repos(repo_objects)

    contributors = []
    temp = []

    for repo_name in repos:
        repo = g.get_repo(repo_name)
        temp = list(repo.get_contributors()) # getting contributor objects
        contributors += get_logins_from_users(temp) # getting logins

    return set(contributors)


# Main method
if __name__ == "__main__":

    #getting organisation 'github'
    organization = g.get_organization(ORGANIZATION_NAME)

    #getting members of github as a list of 'NamedUser' objects, with their logins
    member_objects = list(organization.get_members())

    #get the member's github login ids
    members = get_logins_from_users(member_objects)

    #TODO; delete
    #size of github comapny
    print("Size: " + str(len(members)))

    #TODO: get rid of this
    #print all logins lines by line
    for member in members:
        print(member)

    #get contributors from all repos
    contributors = get_member_repos_contribs(members[0])

    #TODO: get rid of
    for contrib in contributors:
        print contrib

    #TODO: get rid of
    if members[0] in contributors:
        print("Yay!")

    # remove the owner of the repo as a contributor
    if members[0] in contributors:
        contributors.remove(members[0])


    workmate_contribs = list(contributors.intersection(members))

    for contrib in workmate_contribs:
        print contrib

    #TODO: add links between members[0] and workmate_contribs
