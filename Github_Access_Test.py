import pytest
from github import Github
from Github_Access import *
from Test_Classes import NamedUser


#helper func. Checks if two lists have identical elemetns in the same order
#Returns True if equal, False otherwise.
def listsEqual(list_1, list_2):

    index = 0
    for elem in list_1:
        if elem != list_2[index]:
            return False
        index += 1

    return True


#testing method get_logins_from_users
def test_get_logins():

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
#NOTE: Cannot test this method, as code in get_member_repos_contribs() is DIRTY (i.e. results can keep changing over time)
#def test_get_contribs():
