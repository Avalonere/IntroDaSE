from github import Github

token = "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"
g = Github(token)
user = g.get_user()
followers = user.get_following()
for follower in followers:
    follower_repos = follower.get_repos()
    for repo in follower_repos:
        with open("repos.txt", "a") as f:
            f.write(follower.login + ": " + repo.name + "\n")
