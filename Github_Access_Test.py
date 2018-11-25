import pytest
from Github_Access import *
from Test_Classes import NamedUser, Repository # used to test methods in Github_Access.py

#attribute used for multiple tests
EMPTY_SET = set()

#helper function. Checks if two lists have identical elemetns in the same order
#Returns True if equal, False otherwise.
def listsEqual(list_1, list_2):

    index = 0
    for elem in list_1:
        if elem != list_2[index]:
            return False
        index += 1

    return True


###########################################################################
#Testing Test_Classes.py methods

#testing attributes and methods of classes 'NamedUser' and 'Repository'
def test__NamedUser_And_Repostiory():

    #create users, choose user and set repositories of some users
    users = [NamedUser(""), NamedUser("Soulja_Boy"), NamedUser("Fresh Prince")]
    user = users[1]
    repos = [Repository(user, "World"), Repository(users[0], "Wine"), Repository(user, "Einstein"), Repository(user, "Flesh")]

    # LOGIN NAME TESTING:
    assert users[0].login == ""
    assert users[1].login == "Soulja_Boy"
    assert users[2].login == "Fresh Prince"

    # REPO OWNER TESTING:
    assert repos[0].owner == user
    assert repos[1].owner == users[0]
    assert repos[2].owner == user
    assert repos[3].owner == user

    # REPO FULL_NAME TESTING:
    assert repos[0].full_name == "Soulja_Boy/World"
    assert repos[1].full_name == "/Wine"
    assert repos[2].full_name == "Soulja_Boy/Einstein"
    assert repos[3].full_name == "Soulja_Boy/Flesh"

    # REPO TESTING:
    #setting repos once
    user.set_repos([repos[0], repos[2], repos[3]])

    result = user.get_repos()
    expected_result = [repos[0], repos[2], repos[3]]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET

    #set same repos multiple times
    user.set_repos(repos)
    user.set_repos(repos)
    user.set_repos(repos)

    result = user.get_repos()
    expected_result = repos

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET

    # CONTRIBUTOR TESTING:
    #choose repo and set contributors
    repo = repos[2]
    repo.set_contributors([users[2]])

    result = repo.get_contributors()
    expected_result = [users[2]]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET

    #set duplicate contributors
    repo.set_contributors([users[2], users[0]])
    repo.set_contributors([users[0]])
    repo.set_contributors([users[0], users[2]])

    result = repo.get_contributors()
    expected_result = [users[0], users[2]]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET


###########################################################################
#Testing Github_Access.py methods

#testing method get_logins_from_users
def test__get_logins_from_users():

    # Normal and empty login Check
    user_object_list = [NamedUser("abc"), NamedUser("zzz"), NamedUser("Shaun"), NamedUser("a"), NamedUser("Z"), NamedUser("")]

    expected_logins = ["abc", "zzz", "Shaun", "a", "Z", ""]
    received_logins = get_logins_from_users(user_object_list)

    # Check if expected == result is True
    assert listsEqual(expected_logins, received_logins)

    # Duplicate logins check
    user_object_list = [NamedUser("abcd"), NamedUser("abcd"), NamedUser("Joseph"), NamedUser("abcd")]

    expected_logins = ["abcd", "abcd", "Joseph", "abcd"]
    received_logins = get_logins_from_users(user_object_list)

    # Check if expected == result is True
    assert listsEqual(expected_logins, received_logins)

    # None login check --> Not applicable. Every github user will have a login
    #user_object_list = [NamedUser(), NamedUser(), NamedUser()]


#testing method get_member_repos_contribs
def test__get_member_repos_contribs():

    # Setting member objects
    members = [NamedUser("abc"), NamedUser("zzz"), NamedUser("Shaun"), NamedUser("a"), NamedUser("Z"), NamedUser("")]

    # Setting non-member objects
    non_members = [NamedUser("cba"), NamedUser("Satan"), NamedUser("sudo"), NamedUser("Tom")]

    # Member who's contributors are being fetched
    member = members[2]

    #Create list of repository objects
    repos = [Repository(member, "Test_Repo"), Repository(member, "Repo_fun"), Repository(member, "Famous_Repo")]

    # Set up repositories of the member
    member.set_repos(repos)

    # setting up contributors of repos
    repos[0].set_contributors([members[0], non_members[0], members[2], members[3], non_members[3]])
    repos[1].set_contributors([non_members[1], members[2], members[0]])
    repos[2].set_contributors([members[0], non_members[1], non_members[3], members[3], members[1]])

    # set result and expected_result
    result = get_member_repos_contribs(member, members)
    expected_result = ["a", "Shaun", "abc", "zzz"]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET
