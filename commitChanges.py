from dotenv import load_dotenv
import requests
import base64
import os
import json
from datetime import datetime

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


def isWipeDay(today: datetime):

    with open("activity.json", "r") as activity:
        data = dict(json.load(activity))
        lastWipe = data.get("last_wipe")

    # the activity hasn't been wiped today and today is sunday 
    if lastWipe != str(today.date()) and today.weekday() == 0:
        with open("activity.json", "w") as activity:
            data = {"last_wipe": str(today.date())}
            activity.write(json.dumps(data, indent=4)) # writes only the last wipe day
        return True
    else:
        return False


def commitActivity():

    isWipeDay(datetime.today())
    fileContent = loadActivity()
    sha = getFileSHA()

    data = {
        "message": "activity updated by api",
        "content": fileContent,
        "sha": sha
    }

    response = requests.put(api_url, headers=headers, data=json.dumps(data))
    return response.json(), response.ok


commitActivity()