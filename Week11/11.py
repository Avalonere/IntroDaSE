from github import Github

token = "token"
g = Github(token)
user = g.get_user()
followers = user.get_following()
for follower in followers:
    follower_repos = follower.get_repos()
    for repo in follower_repos:
        with open("repos.txt", "a") as f:
            f.write(follower.login + ": " + repo.name + "\n")
