# file of classes used for testing methods

import sys

# used for testing logins and contibutors
class NamedUser:

    def __init__(self, login):
        self.login = login
        self.repos = [] # list of Repository objects

    # add repositories for a user
    # This method adds repositoires to the already exisitng list of repos
    def add_repos(self, repos):
        """
        Sets repos of a particular user

        @param repos: Takes a list of Repository objects of the user used to call the method

        return: None
        """

        self.repos.extend(repos)

        #knock off duplicate repos
        self.repos = list(set(self.repos))


    #Returns repos of a user
    def get_repos(self):
        """
        Gives out repositories of a user

        return: List of Repository objects
        """

        return self.repos


# used for testing contibutors
class Repository:

    # creates repository object, taking the owner as a NamedUser object
    def __init__(self, owner, name):
        self.owner = owner
        self.full_name = owner.login + "/" + name
        self.contributors = [] # not even the owner himself (may be cases)

    # takes a list of NamedUser objects as contributors
    # This methods adds contributors, to the already existing contributors list
    def add_contributors(self, contributors):
        """
        Adds contributors of a repository

        @param contributors: The list of user objects who have contributed to the repo used to call this function

        return: None.
        """

        self.contributors.extend(contributors)

        #knock off duplicate contributors
        self.contributors = list(set(self.contributors))


    # Returns list of contributors of a repo
    def get_contributors(self):
        """
        Gives out contributors of a repo

        return: A list of NamedUser objects who have contributed to the Repository used to call this function
        """

        return self.contributors


# used for testing followers
class FollowedUser:

    def __init__(self, followers):
        self.followers = followers


#used for testing locations
class LocatedUser:

    def __init__(self, location):
        self.location = location
