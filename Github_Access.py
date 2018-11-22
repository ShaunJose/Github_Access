from github import Github
import sys

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
    Get all the repository names from a list of repository objects.

    @param objects_list: A list of repository objects

    return: a list of names of all the repository objects in objects_list
    """

    names = []
    for obj in objects_list:
        name = obj.full_name
        names.append(name)

    return names


# Main method
if __name__ == "__main__":
    # declaring my access token --> (given no permissions)
    access_token = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

    # creating github instance using token
    g = Github(access_token)

    #getting organisation 'github'
    github = g.get_organization("github")

    #getting members of github as a list of 'NamedUser' objects, with their logins
    member_objects = list(github.get_members())

    #get the member's github login ids
    members = get_logins_from_users(member_objects)

    #size of github comapny
    print("Size: " + str(len(members)))

    #print all logins lines by line
    for member in members:
        print(member)

    #get first member
    mem_login = members[0]
    first_mem = g.get_user(mem_login)

    #get member's repository objects
    repo_objects = list(first_mem.get_repos())

    #get member's repos' names
    repos = get_names_from_repos(repo_objects)

    #print all repo_names line by line
    for repo in repos:
        print(repo)
