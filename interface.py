
"""
How to run this code.
Go to your terminal for Mac and install requests mofule: pip install request.
Since it is a python code
from your terminal run: python terminal.py
"""
import requests 
import json

# This function takes as input a GitHub user ID
# The output is a list of the names of the repositories and
# the number of commits that are in each of the listed repositories.

def numberReposandCommits(userID):
    url = "https://api.github.com/users/" + userID + "/repos"
    req = requests.get(url)
    content = req.json()
    repositories = []
    increment = 0

    for REPO in content:
        url2 = "https://api.github.com/repos/" + userID + "/" + REPO["name"] + "/commits"
        req2 = requests.get(url2)
        increment += 1
        commits = len(req2.json())
        repositories.append({"Repo":REPO["name"], "Number of commits": commits})
        print("Repo: " + REPO["name"] + " Number of commits: " + str(commits))
        #if increment == 5: break

    userData = {
        "id": userID,
        "requestStatus": req.status_code,
        "numberOfRepos": increment,
        "status": repositories
    } 

    return userData

# You can select any valid user
user = "richkempinski"
#user = "adiawara"
numberReposandCommits(user)
