from dotenv import load_dotenv
import requests
import base64
import os
import json

load_dotenv()

GHUSER=os.getenv("GHUSER")
REPO=os.getenv("REPO")
REPOPATH=os.getenv("REPOPATH")
BRANCH=os.getenv("BRANCH")
TOKEN=os.getenv("TOKEN")

api_url = f"https://api.github.com/repos/{GHUSER}/{REPO}/contents/{REPOPATH}"

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def getFileSHA():
    response = requests.get(api_url, headers=headers)
    return response.json()["sha"]
    

def loadActivity():
    with open("activity.json", "rb") as activity:
        data = base64.b64encode(activity.read()).decode("utf-8")
    return data


def commitActivity():
    filecontent = loadActivity()
    sha = getFileSHA()
    data = {
        "message": "activity updated by api",
        "content": filecontent,
        "sha": sha
    }
    response = requests.put(api_url, headers=headers, data=json.dumps(data))
    return response.json(), response.ok
