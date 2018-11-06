import pytest
from github import Github

#Test if I can retrieve information about myself correctly
def test_me():
  # declaring my access token
  access_token = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

  # creating github instance using token
  g = Github(access_token)

  #getting my profile
  me = g.get_user()

  #saving user's name and bio
  expected_name = "Shaun Alfred Jose"
  expected_bio = "Integrated Computer Science Student at Trinity College Dublin"

  #Checking details about my profile
  assert (me.name == expected_name)
  assert (me.bio == expected_bio)


#Test if I can retrieve information about another user correctly
def test_other_user():
    # declaring my access token
    access_token = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

    # creating github instance using token
    g = Github(access_token)

    #getting user's profile
    user = g.get_user("god");

    #Test name and location
    assert user.name == "God"
    assert user.location == "Up high in the sky"

    #Test Repositories, forks and issues
    #Saving results. NOTE: THESE ARE CURRENT RESULTS, WHICH MAY CHANGE IN THE FUTURE!
    repo_names = ["animals", "earth", "light", "man", "rails", "solar_system", "water"]
    forks = [4, 3, 7, 17, 0, 2, 1]
    issues = [5, 5, 4, 18, 0, 1, 3]
    index = 0

    #Checking if the results are fetched correctly
    for repo in user.get_repos():
        #name check
        assert repo.name == repo_names[index]
        #number of forks check
        assert repo.forks_count == forks[index]
        #num of issues check
        assert repo.open_issues_count == issues[index]
        #update index
        index = index + 1
