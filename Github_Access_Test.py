import pytest
from github import Github


def test_me():
  # declaring an access token
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
