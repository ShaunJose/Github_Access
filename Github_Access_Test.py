import sys
import pytest
from Github_Access import *
from Test_Classes import NamedUser, Repository, FollowedUser, LocatedUser

#attribute used for multiple tests
EMPTY_SET = set()

#helper function. Checks if two lists have identical elemetns in the same order
#Returns True if equal, False otherwise.
def lists_equal(list_1, list_2):

    index = 0
    for elem in list_1:
        if index >= len(list_2):
            return False
        if elem != list_2[index]:
            return False
        index += 1

    if index == len(list_2):#make sure list 2 has been fully traversed
        return True
    else:
        return False


#Testing lists_equal method
def test__lists_equal():

    #empty list check
    list_1 = []
    list_2 = []

    assert lists_equal(list_1, list_2)

    #test list_1 longer than list_2
    list_1 = ["Woo", "Wooo"]
    list_2 = []

    assert not lists_equal(list_1, list_2)

    #test lists_2 longer than list_1
    list_1 = []
    list_2 = ["Woo", "Wooo"]

    assert not lists_equal(list_1, list_2)

    #test list_1 halfway similar to list_2
    list_1 = ["I", "am", "setting", "up"]
    list_2 = ["I", "am", "setting", "up", "tests"]

    assert not lists_equal(list_1, list_2)

    #test list_1 halfway similar to list_2
    list_1 = ["I", "am", "setting", "up", "tests"]
    list_2 = ["I", "am", "setting"]

    assert not lists_equal(list_1, list_2)

    #test list_1 and list_2 equal lengths and equal
    list_1 = ["I", "am", "setting", "up", "similar", "lists"]
    list_2 = ["I", "am", "setting", "up", "similar", "lists"]

    assert lists_equal(list_1, list_2)

    #test list_1 and list_2 equal lengths and unequal
    list_1 = ["I", "am", "not", "setting", "up", "similar", "lists"]
    list_2 = ["I", "am", "setting", "up", "dissimilar", "lists"]

    assert not lists_equal(list_1, list_2)


###########################################################################
#Testing Test_Classes.py methods

#testing attributes and methods of classes 'NamedUser' and 'Repository'
def test__NamedUser_And_Repostiory():

    #create users, choose user and set repositories of some users
    users = [NamedUser(""), NamedUser("Soulja_Boy"), NamedUser("Fresh Prince")]
    user = users[1]
    repos = [Repository(user, "World"), Repository(users[0], "Wine"), Repository(user, "Einstein"), Repository(user, "Flesh")]

    # LOGIN NAME TESTING:
    result = [users[0].login, users[1].login, users[2].login]
    expected_result = ["", "Soulja_Boy", "Fresh Prince"]
    assert lists_equal(result, expected_result)

    # REPO OWNER TESTING:
    result = [repos[0].owner, repos[1].owner, repos[2].owner, repos[3].owner]
    expected_result = [user, users[0], user, user]
    assert lists_equal(result, expected_result)

    # REPO FULL_NAME TESTING:
    result = [repos[0].full_name, repos[1].full_name, repos[2].full_name, repos[3].full_name]
    expected_result = ["Soulja_Boy/World", "/Wine", "Soulja_Boy/Einstein", "Soulja_Boy/Flesh"]
    assert lists_equal(result, expected_result)

    # REPO TESTING:
    #setting repos once
    user.add_repos([repos[0], repos[2], repos[3]])

    result = user.get_repos()
    expected_result = [repos[0], repos[2], repos[3]]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET

    #set same repos multiple times
    user.add_repos(repos)
    user.add_repos(repos)
    user.add_repos(repos)

    result = user.get_repos()
    expected_result = repos

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET

    # CONTRIBUTOR TESTING:
    #choose repo and set contributors
    repo = repos[2]
    repo.add_contributors([users[2]])

    result = repo.get_contributors()
    expected_result = [users[2]]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET

    #set duplicate contributors
    repo.add_contributors([users[2], users[0]])
    repo.add_contributors([users[0]])
    repo.add_contributors([users[0], users[2]])

    result = repo.get_contributors()
    expected_result = [users[0], users[2]]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET


#testing FollowedUser attribute
def test__FollowedUser():

    users = [FollowedUser(0), FollowedUser(127), FollowedUser(54), FollowedUser(103), FollowedUser(307), FollowedUser(1450), FollowedUser(300000), FollowedUser(10)]

    result = [users[0].followers, users[1].followers, users[2].followers, users[3].followers, users[4].followers, users[5].followers, users[6].followers, users[7].followers]
    expected_result = [0, 127, 54, 103, 307, 1450, 300000, 10]

    assert lists_equal(result, expected_result)


#testing LocatedUser attribute
def test__LocatedUser():

    users = [LocatedUser("Kingston"), LocatedUser("Miami"), LocatedUser("Florida"), LocatedUser("Good ol' Dublin"), LocatedUser("Shank Village"), LocatedUser("Up high in the sky")]

    result = [users[0].location, users[1].location, users[2].location, users[3].location, users[4].location, users[5].location, ]
    expected_result = ["Kingston", "Miami", "Florida", "Good ol' Dublin", "Shank Village", "Up high in the sky"]

    assert lists_equal(result, expected_result)


###########################################################################
#Testing Github_Access.py methods

#testing method get_logins_of_users
def test__get_logins_from_users():

    # Normal and empty login Check
    user_object_list = [NamedUser("abc"), NamedUser("zzz"), NamedUser("Shaun"), NamedUser("a"), NamedUser("Z"), NamedUser("")]

    expected_logins = ["abc", "zzz", "Shaun", "a", "Z", ""]
    received_logins = get_logins_of_users(user_object_list)

    # Check if expected == result is True
    assert lists_equal(expected_logins, received_logins)

    # Duplicate logins check
    user_object_list = [NamedUser("abcd"), NamedUser("abcd"), NamedUser("Joseph"), NamedUser("abcd")]

    expected_logins = ["abcd", "abcd", "Joseph", "abcd"]
    received_logins = get_logins_of_users(user_object_list)

    # Check if expected == result is True
    assert lists_equal(expected_logins, received_logins)

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
    member.add_repos(repos)

    # setting up contributors of repos
    repos[0].add_contributors([members[0], non_members[0], members[2], members[3], non_members[3]])
    repos[1].add_contributors([non_members[1], members[2], members[0]])
    repos[2].add_contributors([members[0], non_members[1], non_members[3], members[3], members[1]])

    # set result and expected_result
    result = get_member_repos_contribs(member, members)
    expected_result = ["a", "Shaun", "abc", "zzz"]

    # testing sets as ordering doesn't matter
    assert set(result) - set(expected_result) == EMPTY_SET


#testing get_all_contributors_from_org
def test__get_all_contributors_from_org():

    # Setting member objects
    members = [NamedUser("abc"), NamedUser("zzz"), NamedUser("Shaun"), NamedUser("Solitary Man")]

    # Setting non-member objects
    non_members = [NamedUser("cba"), NamedUser("Satan"), NamedUser("sudo"), NamedUser("Tom")]

    #Create list of repository objects
    repos = [Repository(members[0], "Test_Repo"), Repository(members[0], "Repo_fun"), Repository(members[0], "Famous_Repo"), Repository(members[1], "Nobody_Cares"), Repository(members[1], "Random Name"), Repository(members[2], "World's most valued repo"), Repository(members[3], "My life")]

    #add contributors :D
    repos[0].add_contributors([members[0], non_members[3], members[2]])
    repos[1].add_contributors([members[1], non_members[0], members[0]])
    repos[2].add_contributors([non_members[0], non_members[1], members[2], non_members[2]])
    repos[3].add_contributors([members[2], non_members[0], members[1]])
    repos[4].add_contributors([non_members[1], non_members[0], non_members[2], members[0]])
    repos[5].add_contributors([members[1], members[2], non_members[0], non_members[0]])
    repos[6].add_contributors([members[3]])

    result = get_all_contributors_from_org(members)
    expected_result = [ [members[1], members[2]], [members[0], members[2]], [members[1]], [] ]

    #Testing sets here as ordering doesnt matter
    index = 0
    for list in result:
        assert set(list) - set(expected_result[index]) == EMPTY_SET
        index += 1


#testing get_num_of_followers
def test__get_num_of_followers():

    #Empty users test
    users = []

    result = get_num_of_followers(users)
    expected_result = []

    assert lists_equal(result, expected_result)

    #Normal Test
    users = [FollowedUser(0), FollowedUser(127), FollowedUser(54), FollowedUser(103), FollowedUser(307), FollowedUser(1450), FollowedUser(300000), FollowedUser(10)]

    result = get_num_of_followers(users)
    expected_result = [0, 127, 54, 103, 307, 1450, 300000, 10]

    assert lists_equal(result, expected_result)


#testing get_popularity
def test__get_popularity():

    #Empty followers and boundaries test
    followers = []
    boundaries = []

    result = get_popularity(followers, boundaries)
    expected_result = []

    assert lists_equal(result, expected_result)

    #Empty followers test
    followers = []
    boundaries = [7,12,24,2423,423432]

    result = get_popularity(followers, boundaries)
    expected_result = []

    assert lists_equal(result, expected_result)

    #Empty boundaries test
    followers = [7, 32, 423, 4, 523, 3, 5, 324, 353]
    boundaries = []

    result = get_popularity(followers, boundaries)
    expected_result = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    assert lists_equal(result, expected_result)

    #Normal Test
    result = get_popularity(followers, boundaries)
    expected_result = [0, 2, 1, 2, 2, 3, 4, 1]

    followers = [0, 127, 54, 103, 307, 1450, 300000, 10]

    #setting up boundaries for popularity
    boundaries = [10, 100, 1000, 100000]

    result = get_popularity(followers, boundaries)
    expected_result = [0, 2, 1, 2, 2, 3, 4, 1]

    assert lists_equal(result, expected_result)


#testing get_locations_of_users
def test__get_locations_of_users():

    #Empty users test
    users = []

    result = get_logins_of_users(users)
    expected_result = []

    assert lists_equal(result, expected_result)

    #Normal Test
    users = [LocatedUser("Kingston"), LocatedUser("Miami"), LocatedUser("Florida"), LocatedUser("Good ol' Dublin"), LocatedUser("Shank Village"), LocatedUser("Up high in the sky")]

    result = get_locations_of_users(users)
    expected_result = ["Kingston", "Miami", "Florida", "Good ol' Dublin", "Shank Village", "Up high in the sky"]

    assert lists_equal(result, expected_result)


#testing create_graph
def test__create_graph():
    #NOTE: First four param arrays have to have the same length!

    #Empty parameters test
    usernames = []
    followers = []
    popularity = []
    locations = []
    connections = [[]]

    result = create_graph(usernames, followers, popularity, locations, connections)
    expected_result = { "nodes": [], "links": []}

    assert lists_equal(result["nodes"], expected_result["nodes"])
    assert lists_equal(result["links"], expected_result["links"])

    #Normal parameters test
    usernames = ["Shaun", "Harry", "Susan", "Ron", "Pete", "Jan"]
    followers = [101, 201, 301, 401, 501, 601]
    popularity = [1, 2, 3, 4, 5, 6]
    locations = ["Dublin", "Boston", "Mumbai", "Sweet Cali", "Vegas", "Copenhagen"]
    connections = [ ["Harry", "Jan"], ["Susan", "Ron", "Shaun"], ["Jan", "Pete", "Harry"], ["Shaun", "Pete"], [], ["Susan"] ]

    result = create_graph(usernames, followers, popularity, locations, connections)
    expected_result = { "nodes" :
                        [ { "username": "Shaun",
                            "followers": 101,
                            "popularity": 1,
                            "location": "Dublin"},
                          { "username": "Harry",
                            "followers": 201,
                            "popularity": 2,
                            "location": "Boston"},
                          { "username": "Susan",
                            "followers": 301,
                            "popularity": 3,
                            "location": "Mumbai"},
                          { "username": "Ron",
                            "followers": 401,
                            "popularity": 4,
                            "location": "Sweet Cali"},
                          { "username": "Pete",
                            "followers": 501,
                            "popularity": 5,
                            "location": "Vegas"},
                          { "username": "Jan",
                            "followers": 601,
                            "popularity": 6,
                            "location": "Copenhagen"}],
                        "links" :
                        [ { "source" : "Shaun",
                            "target" : "Harry"},
                          { "source" : "Shaun",
                            "target" : "Jan"},
                          { "source" : "Harry",
                            "target" : "Susan"},
                          { "source" : "Harry",
                            "target" : "Ron"},
                          { "source" : "Harry",
                            "target" : "Shaun"},
                          { "source" : "Susan",
                            "target" : "Jan"},
                          { "source" : "Susan",
                            "target" : "Pete"},
                          { "source" : "Susan",
                            "target" : "Harry"},
                          { "source" : "Ron",
                            "target" : "Shaun"},
                          { "source" : "Ron",
                            "target" : "Pete"},
                          { "source" : "Jan",
                            "target" : "Susan"} ] }

    assert lists_equal(result["nodes"], expected_result["nodes"])
    assert lists_equal(result["links"], expected_result["links"])
