from github import Github

# declaring an access token
access_token = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

# creating github instance using token
g = Github(access_token)

#getting my profile
me = g.get_user()

#printing stuff about my profile
print("User's Name: " + me.name)
print("About the user: " + me.bio)
