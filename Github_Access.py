from github import Github
import sys

# declaring my access token
access_token = "1f24b75e991ab17fa02a3bb1df8dec255e77fbd6"

# creating github instance using token
g = Github(access_token)

#getting my profile
me = g.get_user()

print("-----------------------------") #delimiter

#printing stuff about my profile
print("User's Name: " + me.name)
print("About the user: " + me.bio)

print("-----------------------------") #delimiter

#getting someone else's profile
god = g.get_user("god")

#printing stuff about user "god"
name = god.name

print("Information about " + name)

#printing out Location
print("Location: " + god.location)

#fetching all of God's Repositories and info regarding them, and displaying it
repos = god.get_repos()
ctr = 1;
print("Repositories, Forks and Issues: ")
for repo in repos:
    sys.stdout.write(str(ctr) + ". " + repo.name)
    #Forks from current repo
    forks_count = repo.forks_count
    if(forks_count == 0):
        sys.stdout.write(" - No forks from this repo. ")
    else:
        sys.stdout.write(" - " + str(forks_count) + " fork/s from this repo. ")
    sys.stdout.flush()
    #Issues in current repo
    issues_count = repo.open_issues_count
    if(issues_count == 0):
        print("No issues in this repo")
    else:
        print(str(issues_count) + " issue/s in this repo")
    #increment counter
    ctr = ctr + 1

#if god.has_issues():
#    issue_urls = god.issue_urls()
