from github import Github
import sys

# declaring my access token --> (given no permissions)
access_token = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

# creating github instance using token
g = Github(access_token)

#getting organisation 'github'
github = g.get_organization("github")

#getting members of github as a list of 'NamedUser' objects, with their logins
member_objects = list(github.get_members())
