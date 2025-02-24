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
OUTPUT=os.getenv("OUTPUT")

api_url = f"https://api.github.com/repos/{GHUSER}/{REPO}/contents/{REPOPATH}"

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def getFileSHA():
    # returns the file's SHA hash by requesting it to GitHub's API
    response = requests.get(api_url, headers=headers)
    return response.json()["sha"]
    

def loadActivity():
    # returns a Dict object of the content of activity.json
    with open(OUTPUT, "rb") as activity:
        return activity.read()
        

def toJS(b: bytes):
    return b"var data = " + b

def encode(file_str) -> bytes:
    return base64.b64encode(file_str).decode("utf-8")


def isWipeDay(today: datetime) -> bool:
    # returns True if the file should be cleaned
    content = loadActivity().decode("utf-8")
    data = dict(json.loads(content))
    lastWipe = data.get("last_wipe")

    # the activity hasn't been wiped today and today is sunday 
    # sunday = 6
    if lastWipe != str(today.date()) and today.weekday() == 6:
        with open(OUTPUT, "w") as activity:
            data = {"last_wipe": str(today.date()), "activity": []}
            activity.write((json.dumps(data, indent=4))) # writes only the last wipe day
        return True
    else:
        return False


def commitActivity():

    # sends a post request with the content of the activity.json file
    # https://docs.github.com/en/rest
    # calls isWipeDay() the clean the file if today is a sunday and the file hasn't been clean today

    isWipeDay(datetime.today())

    fileContent = loadActivity()
    fileContent = toJS(fileContent)
    fileContent = encode(fileContent)

    sha = getFileSHA()

    data = {
        "message": "activity updated by api",
        "content": fileContent,
        "sha": sha
    }

    response = requests.put(api_url, headers=headers, data=json.dumps(data))
    return response.json(), response.ok


if __name__ == "__main__":
    commitActivity()